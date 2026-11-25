# Agentic AI for Enterprises

Module 5 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), pp. 163–195 · [Index](README.md)

## Agent Lifecycle and Runtime Architecture

**Agent logic** describes how an agent selects actions and tools. The **Agent Runtime** provides the environment in which that logic runs. The **application** supplies the request and consumes the result. The agent lifecycle spans development, testing, deployment, operation, and revision. (pp. 163–168)

| Runtime capability | Responsibility |
| --- | --- |
| **Request Handling** | Accept, authenticate, rate-limit, and route requests. |
| **Execution Environment** | Run the agent in a server, container, or serverless environment. |
| **Orchestration & State** | Coordinate steps, sessions, memory, and applicable retries. |
| **Tool Sandbox** | Isolate execution and limit the resources a tool can use. |
| **Integrations** | Manage connections and credentials for APIs and databases. |
| **Scaling & Reliability** | Handle demand, load balancing, and failover. |
| **Observability** | Collect logs, metrics, and traces for inspection. |

A self-managed runtime puts these operational responsibilities on the development team. A managed runtime provides capabilities within the service's scope. The team still defines agent instructions, knowledge sources, tool permissions, and business rules. (pp. 169–171, 178–181)

## Models and Governance in OCI Enterprise AI

OCI Enterprise AI combines **Models**, **Agents**, and **Governance**. Models process information, Agents provide orchestration and execution, and Governance sets controls on access and behavior. (pp. 172–177)

![OCI Enterprise AI combines Models, Agents, and Governance and supports managed API and hosted application options.](images/05-oci-enterprise-ai.png)

| Model type | Function |
| --- | --- |
| **Chat** | Generates responses, reasons over input, and can propose tool calls. |
| **Embed** | Transforms input into vectors for semantic search. |
| **Rerank** | Scores retrieved candidates against a query and reorders them by relevance. |

**On-Demand** draws on shared capacity and suits variable usage. **Dedicated AI Cluster** reserves capacity for a tenancy and supports workloads that require isolation, predictable latency, or eligible custom models. The serving options differ in usage-based charges and capacity commitments. (pp. 174–176)

**Network Security** includes Private Endpoints and Zero Trust Packet Routing (ZPR). **Identity Control** uses Identity and Access Management (IAM) policies to authorize resource access. **AI Behavior** uses guardrails for controls such as content moderation, prompt injection defense, and personally identifiable information (PII) detection. (p. 177)

## OCI Responses API and Hosted Agentic Apps

| Service option | Execution boundary |
| --- | --- |
| **OCI Responses API** | The application runs on its existing infrastructure and calls a managed API for model access, supported tools, and conversation state. |
| **Hosted Agentic Apps** | OCI hosts the application container, including its chosen framework and agent logic. The managed service provides an endpoint and infrastructure capabilities according to the deployment configuration. |

OCI Responses API offers an OpenAI-compatible interface, model routing, tool reasoning, and state management. **File Search** retrieves document content. **Code Interpreter** runs Python in a sandboxed environment. **Function Calling** requests execution of application-provided functions. **MCP Calling** connects to an MCP server. (pp. 178–184)

## Conversation State, Memory, and Supporting APIs

| Capability | Scope |
| --- | --- |
| **Short-term memory** | Context between turns in a conversation, managed through the Conversations API. |
| **Long-term memory** | Context across sessions associated with a `subject_id` in a project. |
| **Context compaction** | A shorter representation of long conversation history that reduces the context the model must process. |

**Files API** manages file objects. **Vector Stores API** supports chunking, embeddings, retrieval, and metadata filtering. **Containers API** provides an isolated execution environment for compatible workloads. (pp. 185–186)

## Authentication and Project Scope

**Generative AI API Key** and **OCI IAM request signing** are authentication approaches described for OCI access. In the OpenAI-compatible interface, `base_url` identifies the OCI endpoint for the region, the model identifier selects a model, and the `OpenAI-Project` header identifies the Generative AI project by its OCI resource identifier (OCID). SDK compatibility preserves the request interface while OCI controls access to the target endpoint, model, and project. (pp. 187–191)

For Hosted Agentic Apps, the container image defines the application and its dependencies. Deployment configuration governs identity, networking, storage, and scaling. An OCI-managed endpoint provides access to the deployed version. (pp. 192–195)
