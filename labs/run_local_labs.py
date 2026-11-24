import ast
import asyncio
import csv
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
from threading import Thread

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from fixture_model import start

ROOT = Path(__file__).resolve().parent
COURSE = ROOT / "oracle-university" / "agentic-ai-foundations"
RESULTS = ROOT / "results"
SAMPLE_CASES = {
    "LangChain/core_building_blocks.py": ("Your name is Alex.", "Chain Output"),
    "LangChain/first_agent.py": ("120", "40", "84", "divide by zero"),
    "MCP/first_agent_with_mcp.py": ("Found 4 tools", "120", "40", "84"),
    "OpenAI/01_hello_responses.py": ("RESPONSE", "deterministic local fixture"),
    "OpenAI/02_stateful_conversation.py": ("Alice", "software engineer"),
    "OpenAI/03_web_search.py": ("Paris", "no live web result"),
    "OpenAI/04_first_agent.py": ("deterministic local fixture",),
    "OpenAI/05_function_tools.py": ("The result is 40.", "Area: 84.", "divide by zero"),
    "OpenAI/06_multi_agent_handoffs.py": ("Answered by: Math Tutor", "Answered by: History Tutor", "Answered by: Science Tutor"),
    "OpenAI/07_guardrails.py": ("Blocked!",),
    "OpenAI/08_customer_support.py": ("Order_Status_Agent:", "Refund_Agent:", "FAQ_Agent:", "Blocked:"),
    "OCI/oci_first_agent.py": ("120", "40"),
    "OCI/oci_first_agent_simple.py": ("get_weather", "San Francisco", "Tokyo", "Foggy", "Sunny"),
    "OCI/oci_first_agent_sdk.py": ("120", "40", "84"),
}


def output(subpath):
    return RESULTS / (subpath.replace("/", "-").removesuffix(".py") + ".log")


def run_course_sample(subpath, base, env):
    path = COURSE / subpath
    args = [sys.executable, str(path)]
    if subpath.startswith("OCI/"):
        args = [sys.executable, str(Path(__file__).resolve()), "--oci-fixture", str(path), base]
    completed = subprocess.run(args, env=env, cwd=ROOT, capture_output=True, text=True, timeout=90)
    combined = completed.stdout + completed.stderr
    result = output(subpath)
    result.write_text(combined, encoding="utf-8")
    missing = [term for term in SAMPLE_CASES[subpath] if term.casefold() not in combined.casefold()]
    if completed.returncode or missing:
        raise AssertionError(f"exit={completed.returncode}, missing={missing}; see {result.relative_to(ROOT)}")


def run_oci_fixture(path, url):
    source = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in source.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id
            values = {"OCI_BASE_URL": url, "OCI_PROJECT_ID": "local-fixture-project"}
            if name in values:
                node.value = ast.copy_location(ast.Constant(values[name]), node.value)
    exec(compile(ast.fix_missing_locations(source), str(path), "exec"), {"__name__": "__main__", "__file__": str(path)})


def load_sample(relative):
    path = COURSE / relative
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


async def math_mcp_session():
    server = StdioServerParameters(command=sys.executable, args=[str(COURSE / "MCP/mcp_math_server.py")])
    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = {tool.name: tool.inputSchema for tool in (await session.list_tools()).tools}
            assert set(tools) == {"add", "multiply", "divide", "square_root"}
            assert set(tools["divide"]["required"]) == {"a", "b"}
            calls = [
                ("add", {"a": 42, "b": 58}, "100"),
                ("multiply", {"a": 15, "b": 8}, "120"),
                ("divide", {"a": 120, "b": 3}, "40"),
                ("square_root", {"number": 84}, "9.16"),
                ("divide", {"a": 100, "b": 0}, "zero"),
                ("square_root", {"number": -1}, "negative"),
            ]
            evidence = []
            for name, args, expected in calls:
                result = await session.call_tool(name, args)
                text = " ".join(part.text for part in result.content if part.type == "text")
                assert expected in text.casefold(), (name, args, text)
                evidence.append({"tool": name, "input": args, "result": text})
            invalid = await session.call_tool("multiply", {"a": 5})
            assert invalid.isError
            evidence.append({"tool": "multiply", "input": {"a": 5}, "schema_error": True})
    (RESULTS / "mcp-math.json").write_text(json.dumps(evidence, indent=2) + "\n")


async def oci_usage_discovery():
    server = StdioServerParameters(command="uvx", args=["oracle.oci-usage-mcp-server"])
    with (RESULTS / "oci-usage-mcp-discovery.log").open("w") as log:
        async with stdio_client(server, errlog=log) as (read, write):
            async with ClientSession(read, write) as session:
                init = await session.initialize()
                tools = {tool.name: tool.inputSchema for tool in (await session.list_tools()).tools}
                assert "get_summarized_usage" in tools, tools
    result = {"server": init.serverInfo.name, "protocol_version": init.protocolVersion, "tools": tools}
    (RESULTS / "oci-usage-mcp-discovery.json").write_text(json.dumps(result, indent=2) + "\n")


def synthetic_usage():
    samples = [
        {"time_usage_started": "2026-01-01T00:00:00Z", "service": "Compute", "computed_amount": 12.50, "currency": "USD"},
        {"time_usage_started": "2026-01-01T00:00:00Z", "service": "Object Storage", "computed_amount": 1.50, "currency": "USD"},
        {"time_usage_started": "2026-01-02T00:00:00Z", "service": "Compute", "computed_amount": 7.50, "currency": "USD"},
    ]
    for mode in ("client", "agent"):
        prefix = "01" if mode == "client" else "02"
        module = load_sample(f"Real World MCP/{prefix}_oci_usage_mcp_{mode}.py")
        pivot = module.build_pivot(module.extract_items({"data": {"items": samples}}))
        assert pivot["column_totals"] == {"Compute": 20.0, "Object Storage": 1.5}
        assert pivot["grand_total"] == 21.5
        path = RESULTS / f"oci-usage-{mode}-synthetic.csv"
        module.write_daily_service_csv(pivot, path)
        with path.open(newline="") as f:
            report = list(csv.reader(f))
        assert float(report[-1][-1]) == 21.5, report[-1]
    assert (RESULTS / "oci-usage-client-synthetic.csv").read_bytes() == (RESULTS / "oci-usage-agent-synthetic.csv").read_bytes()


def main():
    if len(sys.argv) == 4 and sys.argv[1] == "--oci-fixture":
        run_oci_fixture(Path(sys.argv[2]), sys.argv[3])
        return
    if not COURSE.is_dir():
        raise SystemExit("Oracle lab sources are missing. Run git submodule update --init from the repository root.")
    RESULTS.mkdir(exist_ok=True)
    server = start()
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_port}/v1"
    env = dict(os.environ)
    env.pop("OPENAI_ORG_ID", None)
    env.pop("OPENAI_PROJECT_ID", None)
    env.update(
        OPENAI_API_KEY="local-fixture",
        OPENAI_BASE_URL=base,
        OPENAI_AGENTS_DISABLE_TRACING="1",
        LANGSMITH_TRACING="false",
        LANGCHAIN_TRACING_V2="false",
        OCI_GENAI_API_KEY="local-fixture",
        REGION="local-fixture",
        MODEL_ID="fixture-model",
        PROJECT_ID="local-fixture-project",
        PATH=str(Path(sys.executable).parent) + os.pathsep + env.get("PATH", ""),
    )
    results = []

    def record(name, fn, mode):
        try:
            fn()
            results.append({"lab": name, "status": "passed", "mode": mode})
            print(f"PASS {name} ({mode})", flush=True)
        except Exception as error:
            results.append({"lab": name, "status": "failed", "mode": mode, "detail": str(error)})
            print(f"FAIL {name}: {error}", flush=True)

    try:
        record("MCP math server", lambda: asyncio.run(math_mcp_session()), "real local stdio")
        for subpath in SAMPLE_CASES:
            def exercise():
                count = len(server.tool_events)
                run_course_sample(subpath, base, env)
                calls = server.tool_events[count:]
                if subpath.endswith("core_building_blocks.py"):
                    assert "calculate_bmi" in calls, calls
                if subpath.endswith("05_function_tools.py"):
                    assert calls == ["add", "multiply", "divide", "multiply", "square_root", "divide"], calls
                if subpath.endswith("oci_first_agent_simple.py"):
                    assert calls == ["get_weather", "get_weather"], calls
            record(subpath, exercise, "deterministic local model fixture")
        record("OCI Usage MCP discovery", lambda: asyncio.run(asyncio.wait_for(oci_usage_discovery(), timeout=140)), "real local stdio")
        record("OCI Usage pivot and CSV", synthetic_usage, "synthetic usage records")
    finally:
        server.shutdown()
        server.server_close()
        (RESULTS / "local-summary.json").write_text(json.dumps(results, indent=2) + "\n")
    if any(case["status"] == "failed" for case in results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
