import json
import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from itertools import count

ids = count(1)
history = {}


def flatten(value):
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return " ".join(flatten(item) for item in value)
    if isinstance(value, dict):
        return flatten(value.get("text", value.get("content", "")))
    return str(value)


def observed_number(result):
    match = re.search(r"-?\d+(?:\.\d+)?", result)
    if not match:
        raise ValueError(f"Expected a numeric tool result, received {result!r}")
    return float(match[0])


def calculate(query, names, results):
    query = query.lower()
    if "calculate_bmi" in names:
        return "calculate_bmi", {"weight_kg": 70, "height_m": 1.75}
    if "get_weather" in names and "weather" in query:
        if results:
            return "\n".join(results)
        cities = [name for name in ("San Francisco", "Tokyo", "London", "New York", "Sydney") if name.lower() in query]
        return [("get_weather", {"city": city}) for city in cities]
    if not {"multiply", "divide"}.issubset(names):
        return None
    if "rectangle" in query:
        if not results:
            return "multiply", {"a": 12, "b": 7}
        if len(results) == 1:
            return "square_root", {"number": observed_number(results[-1])}
        return f"Area: {observed_number(results[0]):g}. Square root: {observed_number(results[-1]):.3f}."
    if "multiplied by 8, then divided by 3" in query:
        if not results:
            return "multiply", {"a": 15, "b": 8}
        if len(results) == 1:
            return "divide", {"a": observed_number(results[-1]), "b": 3}
        return f"The result is {observed_number(results[-1]):g}."
    match = re.search(r"(\d+)\s*(\+|multiplied by|divided by)\s*(\d+)", query)
    if match:
        a, op, b = match.groups()
        if results:
            return results[-1]
        operation = {"+": "add", "multiplied by": "multiply", "divided by": "divide"}[op]
        return operation, {"a": int(a), "b": int(b)}
    return None


def answer(payload, messages):
    tools = payload.get("tools") or []
    names = {
        tool.get("function", tool).get("name")
        for tool in tools if tool.get("type") == "function"
    }
    query = next((flatten(x.get("content", "")) for x in reversed(messages) if x.get("role") == "user"), "")
    q = query.lower()
    instructions = str(payload.get("instructions") or "")
    instructions += " ".join(flatten(x.get("content", "")) for x in messages if x.get("role") in {"system", "developer"})
    results = [flatten(x.get("output", x.get("content", ""))) for x in messages
               if x.get("type") == "function_call_output" or x.get("role") == "tool"]

    if "is_support_question" in instructions:
        valid = any(word in q for word in ("order", "refund", "policy"))
        return json.dumps({"is_support_question": valid, "reasoning": "Fixture: topic classification."})
    if "is_on_topic" in instructions:
        return json.dumps({"is_on_topic": "gravity" in q, "reasoning": "Fixture: topic classification."})

    handoffs = {
        "transfer_to_order_status_agent": "where is my order",
        "transfer_to_refund_agent": "refund",
        "transfer_to_faq_agent": "amazon return policy",
        "transfer_to_math_tutor": ("15%", "quadratic formula"),
        "transfer_to_history_tutor": "great wall",
        "transfer_to_science_tutor": "photosynthesis",
    }
    for name, keywords in handoffs.items():
        keywords = (keywords,) if isinstance(keywords, str) else keywords
        if name in names and any(keyword in q for keyword in keywords):
            return name, {}

    if "lookup_order" in names:
        return results[-1] if results else ("lookup_order", {"order_id": "ORD-001"})
    if "process_refund" in names:
        return results[-1] if results else ("process_refund", {"order_id": "ORD-002", "reason": "Book arrived damaged"})
    math = calculate(query, names, results)
    if math is not None:
        return math

    if "my name" in q:
        people = " ".join(flatten(x.get("content", "")) for x in messages if x.get("role") == "user")
        if "name is Alice" in people:
            return "Your name is Alice, and you work as a software engineer."
        if "Alex" in people:
            return "Your name is Alex."
    if "15% of 240" in q:
        return "15% of 240 is 36."
    if "capital of france" in q:
        return "Paris."
    if any(word in q for word in ("latest developments", "bitcoin", "amazon return policy")):
        return "Offline fixture: no live web result is available."
    return "An agent uses a model and tools in a loop. This is a deterministic local fixture response."


def as_items(value):
    if isinstance(value, str):
        return [{"role": "user", "content": value}]
    return value or []


def responses(payload):
    serial = next(ids)
    ref = f"resp_local_{serial}"
    prior = history.get(payload.get("previous_response_id"), [])
    messages = prior + as_items(payload.get("input"))
    history[ref] = messages
    result = answer(payload, messages)
    if isinstance(result, (tuple, list)):
        calls = [result] if isinstance(result, tuple) else result
        output = [
            {"type": "function_call", "id": f"fc_local_{serial}_{i}", "call_id": f"call_local_{serial}_{i}",
             "name": name, "arguments": json.dumps(args), "status": "completed"}
            for i, (name, args) in enumerate(calls)
        ]
    else:
        output = [{"type": "message", "id": f"msg_local_{serial}", "role": "assistant", "status": "completed",
                   "content": [{"type": "output_text", "text": result, "annotations": []}]}]
    return {
        "id": ref, "object": "response", "created_at": 0, "status": "completed",
        "model": payload.get("model", "fixture"), "output": output, "parallel_tool_calls": False,
        "tool_choice": "auto", "tools": payload.get("tools") or [],
        "usage": {"input_tokens": 1, "input_tokens_details": {"cached_tokens": 0},
                  "output_tokens": 1, "output_tokens_details": {"reasoning_tokens": 0}, "total_tokens": 2},
    }


def chat(payload):
    serial = next(ids)
    result = answer(payload, payload["messages"])
    reply = {"role": "assistant", "content": result}
    finish = "stop"
    if isinstance(result, tuple):
        name, args = result
        reply = {"role": "assistant", "content": None, "tool_calls": [
            {"id": f"call_local_{serial}", "type": "function",
             "function": {"name": name, "arguments": json.dumps(args)}}
        ]}
        finish = "tool_calls"
    return {
        "id": f"chatcmpl_local_{serial}", "object": "chat.completion", "created": 0,
        "model": payload.get("model", "fixture"),
        "choices": [{"index": 0, "message": reply, "finish_reason": finish}],
        "usage": {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2},
    }


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            payload = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            if self.path == "/v1/responses":
                body = responses(payload)
            elif self.path == "/v1/chat/completions":
                body = chat(payload)
            else:
                self.send_error(404)
                return
            if self.path == "/v1/responses":
                calls = [item["name"] for item in body["output"] if item["type"] == "function_call"]
            else:
                calls = [item["function"]["name"] for item in body["choices"][0]["message"].get("tool_calls", [])]
            self.server.tool_events.extend(calls)
            encoded = json.dumps(body).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(encoded)))
            self.end_headers()
            self.wfile.write(encoded)
        except (KeyError, TypeError, ValueError) as error:
            self.send_error(400, str(error))


def start():
    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    server.tool_events = []
    return server
