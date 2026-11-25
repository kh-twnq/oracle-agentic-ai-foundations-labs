# Agentic AI for Oracle AI Database

Module 6 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), pp. 197–241 · [Index](README.md)

## Agenda

1. [Agentic AI for Oracle AI Database](#1-agentic-ai-for-oracle-ai-database)
2. [Introduction to Oracle AI Vector Search](#2-introduction-to-oracle-ai-vector-search)
3. [Oracle AI Vector Search Workflow](#3-oracle-ai-vector-search-workflow)
4. [Oracle AI Vector Search Demo](#4-oracle-ai-vector-search-demo)
5. [Introduction to Oracle AI Database Private Agent Factory](#5-introduction-to-oracle-ai-database-private-agent-factory)
6. [Introduction to Select AI Agent](#6-introduction-to-select-ai-agent)
7. [Oracle Autonomous AI Database MCP Server](#7-oracle-autonomous-ai-database-mcp-server)

Student Guide agenda, p. 198.

## 1. Agentic AI for Oracle AI Database

An enterprise agent may need to retrieve relevant information, execute an authorized database operation, and make its tools available to other applications. Oracle AI Database provides different capabilities for those responsibilities. (pp. 199–200)

| Capability | Responsibility |
| --- | --- |
| **Oracle AI Vector Search** | Ranks data by semantic similarity alongside relational filtering. |
| **Private Agent Factory** | Provides a visual environment for building agent workflows. |
| **Select AI Agent** | Coordinates agent workflows close to the data. |
| **Autonomous AI Database MCP Server** | Publishes database tools for external MCP clients. |

Autonomous AI Vector Database is a related capability for vector workloads. (p. 200)

![Oracle AI Database capabilities include AI Vector Search, Agent Factory, Select AI Agent, and Autonomous MCP Server.](images/06-oracle-ai-database.png)

## 2. Introduction to Oracle AI Vector Search

**Keyword search** matches terms. **Semantic search** retrieves content close to the query in meaning. A tokenizer splits text into tokens, including subword units. An embedding model maps the tokens to a fixed-dimensional vector. Query and document vectors must share a compatible embedding space for their distances to be meaningful. (pp. 201–204)

Oracle AI Vector Search stores embeddings alongside relational data. A SQL query can apply business filters and rank the remaining rows by vector similarity. (p. 205)

## 3. Oracle AI Vector Search Workflow

1. **Prepare.** Extract text and split long documents into chunks that fit the embedding model's input limit. Smaller units allow retrieval to return relevant parts of a document.
2. **Embed.** In-database embedding can use an ONNX model loaded by `DBMS_VECTOR.LOAD_ONNX_MODEL` and invoked through `VECTOR_EMBEDDING`. An external provider can also generate embeddings. The document processing chain can use `UTL_TO_TEXT`, `UTL_TO_CHUNKS`, and `UTL_TO_EMBEDDINGS`.
3. **Store and index.** Keep vectors with source identifiers and metadata. HNSW and IVF are vector index types. Hybrid vector indexes support combinations of search methods.
4. **Retrieve.** Embed the query, rank candidates, and return the top-k results. RAG can place the retrieved content in the model's context. (pp. 206–211)

A `VECTOR` column can declare dimensions and formats such as `FLOAT32`, `FLOAT64`, `INT8`, or `BINARY`. A dense vector stores every position. A sparse vector stores the positions and values of nonzero elements. (p. 210)

| Metric | What it measures |
| --- | --- |
| **Cosine** | Difference in vector direction. |
| **Euclidean (L2)** | Straight-line distance. |
| **Manhattan (L1)** | Sum of absolute differences across dimensions. |
| **Dot product** | A score based on direction and magnitude. |

Lower distance means a closer match. Dot-product ordering depends on how the score is interpreted. (p. 211)

## 4. Oracle AI Vector Search Demo

**Exact similarity search** evaluates the distance between the query vector and each eligible vector. The query and stored content use a compatible embedding model. `VECTOR_DISTANCE` supplies the ranking value. A relational predicate limits eligible rows before the results are ranked and reduced to top-k. (pp. 212–222)

## 5. Introduction to Oracle AI Database Private Agent Factory

Private Agent Factory provides pre-built agents, a visual workflow builder, and data integrations. Single Sign-On (SSO), role-based access, and prompt guardrails support governance. Its container deployment can use Podman on-premises or in the cloud, with connections to Oracle AI Database and a model provider. (pp. 223–225)

| Component | What it works with |
| --- | --- |
| **Knowledge Agent** | Approved documents from files, SharePoint, websites, or OCI Object Storage. Embeddings support retrieval and answers can reference the source. |
| **Data Analysis Agent** | Accessible tables and views. The agent generates SQL and presents the result or a visualization. |
| **Agent Builder** | Visual workflow nodes. Tools, MCP integrations, custom Python components, and multiple agents can participate. |

Connected sources and permissions determine what these agents can access. (pp. 226–228)

## 6. Introduction to Select AI Agent

**Select AI Agent** coordinates agent workflows close to the data. An **AI profile** supplies model configuration and data context. `DBMS_CLOUD_AI_AGENT` defines agents, tools, tasks, and teams. Database roles and Virtual Private Database (VPD) policies govern access. Auditing records database activity. (pp. 229–231)

Planning selects steps. Tool Use executes the actions. Reflection checks the results. Memory Management retains relevant context across turns. A run can use RAG to retrieve content, **NL2SQL** to generate SQL, PL/SQL to perform business operations, or REST to connect to external systems. (pp. 232–234)

## 7. Oracle Autonomous AI Database MCP Server

The **Oracle Autonomous AI Database MCP Server** runs as a managed, multi-tenant capability of Autonomous AI Database Serverless. An MCP client connects over Streamable HTTP via HTTPS to the endpoint for a region and database OCID. The server publishes Select AI Agent tools such as NL2SQL, RAG, and custom PL/SQL. (pp. 235–240)

Database credentials identify the caller. Database roles and policies determine which tools and data are accessible. An AI profile can provide schema metadata to NL2SQL and reduce discovery during the request. MCP defines how the external client discovers and invokes the tools. (pp. 237–241) [MCP Core Components](03-introduction-to-mcp.md#2-mcp-core-components)
