# Oracle Agentic AI Foundations labs

The results follow the [Hands-on Workshop Student Guide](https://mylearn.oracle.com/ou/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course). The Oracle course code is available through the `oracle-university/` Git submodule under `agentic-ai-foundations/`, pinned to commit `085b7b13eeae897e3017ad110b703e2dcfd3a38c` of [Oracle University's companion repository](https://github.com/oracle-university-labs/ou-generativeai-pro/tree/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations).

[Study notes and workshop page references](../study-notes/README.md)

## Lab entry points

| Lab | Script |
| --- | --- |
| LangChain, MCP, OpenAI Agents SDK, OCI and OCI Usage MCP | [run_local_labs.py](run_local_labs.py) |
| Oracle AI Vector Search, local ranking and SQL generation | [vector_search_local.py](vector_search_local.py), [vector_search_oracle.py](vector_search_oracle.py) |
| Customer Return Agent exercise | [customer_return_local.py](customer_return_local.py) |

## Results

| Area | Result |
|---|---|
| LangChain, pp. 63–88 | Both published examples ran through a local model fixture. They exercised prompt templates, conversation history, Python tool schemas, and dependent arithmetic. |
| MCP, pp. 99–114 | The published math server ran over stdio. The client discovered four tools and checked valid calls, division by zero, a negative square root, and a missing required argument. The LangChain-to-MCP example used the same local model fixture. |
| OCI Usage MCP, pp. 116–122 | The published server ran over stdio and advertised `get_summarized_usage`. The client and agent aggregations produced matching CSVs totaling USD 21.50 on synthetic records. Live tenancy queries and Cost Analysis reconciliation require an authorized OCI profile. |
| OpenAI, pp. 130–161 | All eight published scripts ran through the Responses API or Agents SDK client against a local fixture. Checks covered conversation chaining, function dispatch, specialist handoffs, and guardrails. Model inference and hosted web search require a live OpenAI connection. |
| OCI Enterprise AI, pp. 187–195 | The three published examples ran through a local fixture using temporary endpoint and project settings. Live inference, deployment, and IAM checks require authorized OCI settings. |
| Vector Search, pp. 213–222 | Both workshop queries ran against the ten-product catalog with real 384-dimensional MiniLM embeddings and paraphrased descriptions. [SQLite results](sample-results/vector-search-local.json) cover the keyword baseline, top 3 by cosine distance, and top 5 under USD 100. [Oracle FreeSQL results](sample-results/vector-search-oracle.json) confirmed both rankings using native `VECTOR_DISTANCE`. |
| Customer Return Agent, p. 234 | A [local SQL-backed exercise](sample-results/customer-return-local.json) confirmed order 5821 was approved, accepted the 30-day boundary, and checked late, missing, and repeated requests. The local rule measures the window from delivery. The trace reflects deterministic Python and SQLite using synthetic orders. |
| Private Agent Factory, Select AI Agent, and Autonomous AI Database MCP, pp. 223–240 | Live verification requires a provisioned environment with database credentials, AI profile, and grants. |

The runner recorded [17 successful local checks](sample-results/local-summary.json). Sample reports are in [sample-results/](sample-results/). Runs write logs and reports to `labs/results/` locally.

### Vector Search comparison with the guide

The local reproduction uses FastEmbed's ONNX implementation of `all-MiniLM-L6-v2`. Rephrasing the product descriptions changes the inputs to the embedding model. With the descriptions on p. 215, a separate local check put Yoga Mat, Fitness Tracker, and Climbing Harness in the top three. The illustration on p. 219 shows Basketball in third place. The p. 215 Climbing Harness description also matches the literal keyword `gear`. With the rephrased descriptions, the literal keyword query returns zero rows and the semantic query ranks Fitness Tracker, Yoga Mat, and Climbing Harness. Swimming Goggles ranked first for the water sports query in both checks.

In Oracle FreeSQL, both queries ran in five two-product batches to fit the worksheet prefill. Oracle applied the price filter and computed each distance. Merging the native distances produced the same order as SQLite for both result sets. The SQL scales and rounds the embedding coordinates to integers for compact worksheet input. The JSON records the resulting distance differences.

## Reproduce the local runs

Use Python 3.11 and run these commands from the repository root.

```sh
git submodule update --init
uv venv --python 3.11 .venv
uv pip install --python .venv/bin/python -r labs/requirements.txt
.venv/bin/python labs/run_local_labs.py
HF_HUB_DISABLE_TELEMETRY=1 .venv/bin/python labs/vector_search_local.py
HF_HUB_DISABLE_TELEMETRY=1 .venv/bin/python labs/vector_search_oracle.py
.venv/bin/python labs/customer_return_local.py
```

The lab runner starts a loopback-only model fixture using test data. It starts the published math and OCI Usage MCP servers over stdio, which can download the OCI Usage package on its first run. In the OCI examples the runner substitutes local connection settings in memory. The Oracle source files on disk retain their published settings. The vector exercise downloads the public embedding model on its first run.

## Live runs

- **OpenAI**. The original scripts use `OPENAI_API_KEY`. Supply an authorized key through the local environment and use the published filenames directly. This is where actual model responses, web search, and hosted traces can be verified.
- **OCI Enterprise AI**. An authorized Generative AI API key, region, model ID, and project OCID are required. The manual version uses `OCI_GENAI_API_KEY`, `REGION`, `MODEL_ID`, and `PROJECT_ID`. The other two examples define region and project variables in the source.
- **OCI Usage MCP**. The public examples expect an authorized profile in `~/.oci/config` with permission to read usage. A local synthetic CSV is already available for comparing the report format.
- **Oracle Database**. [The generated Vector Search query](sample-results/vector-search-oracle.sql) uses `TO_VECTOR` and `VECTOR_DISTANCE` and can run as a read-only statement on Oracle AI Database 26ai. Reproducing the guide's persistent insert requires a writable schema. A live Customer Return Agent also needs an authorized [Select AI profile and agent framework privileges](https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/prerequisites-using-select-ai-agent.html).
