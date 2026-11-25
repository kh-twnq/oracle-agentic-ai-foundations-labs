# Agentic AI for Oracle AI Database

Module 6 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), pp. 197–241 · [Index](README.md)

Enterprise agents can retrieve relevant information, carry out authorized operations, and share tools with external applications. **Oracle AI Vector Search** provides semantic retrieval. **Private Agent Factory** and **Select AI Agent** support agent workflows. **Autonomous AI Database MCP Server** exposes tools through MCP. **Autonomous AI Vector Database** is a related capability for vector workloads. (pp. 197–200)

![Oracle AI Database capabilities include AI Vector Search, Agent Factory, Select AI Agent, and Autonomous MCP Server.](images/06-oracle-ai-database.png)

## Embeddings and Semantic Search

**Keyword search** matches terms in the stored data. **Semantic search** retrieves content based on similarity in an embedding space. For text, a tokenizer breaks input into tokens, including subword units. An embedding model maps them to a fixed-dimensional vector. Query and document vectors must use a compatible embedding space for their distances to be meaningful. (pp. 201–204)

**Oracle AI Vector Search** stores vectors alongside relational data. SQL can restrict results to rows that satisfy business predicates, then rank the eligible rows by vector similarity. (pp. 205, 217–222)

## Vector Search Data Flow

1. **Prepare content.** Extract text and split long documents into chunks that fit the embedding model's input limits. Chunking allows retrieval to return relevant portions of a document.
2. **Generate embeddings.** An ONNX model loaded with `DBMS_VECTOR.LOAD_ONNX_MODEL` can support in-database embedding through `VECTOR_EMBEDDING`. An external provider can generate embeddings outside the database. Oracle also supports text extraction, chunking, and embedding through `UTL_TO_TEXT`, `UTL_TO_CHUNKS`, and `UTL_TO_EMBEDDINGS`.
3. **Store and index.** Store embeddings with the source content or its identifier and metadata. HNSW and IVF are vector index types. Hybrid vector indexes support combinations of search methods.
4. **Retrieve.** Embed the query, score eligible rows, and return the top-k results. Retrieval-Augmented Generation (RAG) can pass those results to the model as context. (pp. 206–211)

A `VECTOR` column can declare dimensionality and element format. Formats include `FLOAT32`, `FLOAT64`, `INT8`, and `BINARY`. A dense vector stores every position. A sparse vector stores the positions and values of nonzero elements. (p. 210)

| Metric | Meaning |
| --- | --- |
| **Cosine** | Measures differences in vector direction. |
| **Euclidean (L2)** | Measures straight-line distance. |
| **Manhattan (L1)** | Sums absolute differences across dimensions. |
| **Dot product** | Produces a score that depends on direction and magnitude. |

With a distance metric, lower values rank as closer. Dot-product ordering follows the interpretation of the score. **Exact similarity search** evaluates eligible vectors directly with a function such as `VECTOR_DISTANCE`. Relational filtering defines the eligible set, and vector distance determines the ranking within it. (pp. 211, 217–222)

## Private Agent Factory

**Oracle AI Database Private Agent Factory** provides pre-built agents, a visual workflow builder, and enterprise data integrations. Single Sign-On (SSO), role-based access, and prompt guardrails support governance. Its container-based architecture can use Podman and connects to Oracle AI Database and a model provider. (pp. 223–225)

| Component | Data and execution model |
| --- | --- |
| **Knowledge Agent** | Uses embeddings to retrieve approved documents from sources such as files, SharePoint, websites, or OCI Object Storage. Answers can link to supporting material. |
| **Data Analysis Agent** | Generates and executes SQL against accessible tables and views, then presents results or visualizations. |
| **Agent Builder** | Defines workflows as visual nodes that can connect tools, MCP integrations, custom Python components, and multiple agents. |

The connected sources and permissions determine the data available to these agents. (pp. 226–228)

## Select AI Agent

**Select AI Agent** coordinates agent workflows near data in Oracle AI Database. An **AI profile** supplies model configuration and data context. `DBMS_CLOUD_AI_AGENT` defines agents, tools, tasks, and teams. The database can enforce role-based access, Virtual Private Database (VPD) policies, and auditing where data is accessed. (pp. 229–231)

**Planning** selects the steps, **Tool Use** executes actions, **Reflection** evaluates the results, and **Memory Management** retains relevant context across turns. Tools can retrieve context through RAG, convert natural language into SQL through **NL2SQL**, run custom PL/SQL operations, or call external REST integrations. (pp. 232–234)

## Autonomous AI Database MCP Server

**Autonomous AI Database MCP Server** is a managed, multi-tenant capability of Autonomous AI Database Serverless. An MCP client uses Streamable HTTP over HTTPS to reach the endpoint for a region and database OCID. The server exposes Select AI Agent tools such as NL2SQL, RAG, and custom PL/SQL. (pp. 235–236, 239–240)

Database credentials identify the caller, and database roles and policies govern the tools and data that caller can access. An AI profile can supply schema metadata to NL2SQL, reducing schema discovery during the request. MCP provides the discovery and invocation interface across this boundary. (pp. 237–241) [MCP connection lifecycle](03-introduction-to-mcp.md#connection-lifecycle-and-json-rpc-20)
