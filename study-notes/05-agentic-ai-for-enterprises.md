# Agentic AI for Enterprises

Module 5 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), pp. 163–195 · [Index](README.md)

## Agenda

1. [Need for Agent Lifecycle and Runtime](#1-need-for-agent-lifecycle-and-runtime)
2. [Introduction to OCI Enterprise AI Platform](#2-introduction-to-oci-enterprise-ai-platform)
3. [Introduction to OCI Enterprise AI Agents](#3-introduction-to-oci-enterprise-ai-agents)
4. [OCI Enterprise AI Agents Building Blocks](#4-oci-enterprise-ai-agents-building-blocks)
5. [Getting Started with OCI Enterprise AI Agents](#5-getting-started-with-oci-enterprise-ai-agents)
6. [OCI Enterprise AI Agents – Deploy and Scale](#6-oci-enterprise-ai-agents--deploy-and-scale)

Student Guide agenda, p. 164.

## 1. Need for Agent Lifecycle and Runtime

**Agent logic** decides what the agent should do. The **Agent Runtime** provides the environment in which that logic runs. The **application** submits inputs and consumes results. The lifecycle includes development, testing, deployment, operation, and revision. (pp. 165–168)

| Runtime capability | Responsibility |
| --- | --- |
| Request handling | Accept, authenticate, rate-limit, and route requests. |
| Execution environment | Run the agent on a server, in a container, or in a serverless environment. |
| Orchestration and state | Coordinate steps, sessions, memory, and retries. |
| Tool sandbox | Isolate execution and limit resources. |
| Integrations | Manage API and database connections and credentials. |
| Scaling and reliability | Handle demand, load balancing, and failover. |
| Observability | Collect logs, metrics, and traces. |

A team can operate these components directly or use a managed runtime. The application team defines the instructions, permissions, and business rules. (pp. 169–171, 178–181)

## 2. Introduction to OCI Enterprise AI Platform

OCI Enterprise AI combines **Models** for processing information, **Agents** for orchestration and execution, and **Governance** for controlling access and behavior. (pp. 172–177)

![OCI Enterprise AI combines Models, Agents, and Governance.](images/05-oci-enterprise-ai.png)

| Model type | Main function |
| --- | --- |
| **Chat** | Generates a response or proposes a tool call. |
| **Embed** | Converts input to a vector used for retrieval. |
| **Rerank** | Scores previously retrieved candidates and reorders them by relevance. |

**On-Demand** draws on shared capacity and suits variable usage. **Dedicated AI Cluster** reserves capacity for a tenancy and suits workloads that require isolation, predictable latency, or eligible custom models. The two options have different capacity and cost commitments. (pp. 174–176)

Network controls include Private Endpoints and Zero Trust Packet Routing (ZPR). Identity and Access Management (IAM) policies govern resource access. Guardrails address content moderation, prompt injection, and personally identifiable information (PII). (p. 177)

## 3. Introduction to OCI Enterprise AI Agents

OCI Enterprise AI Agents offers two managed paths for running agent workloads. (pp. 178–181)

| Option | Where does application logic run? | What does OCI provide? |
| --- | --- | --- |
| **OCI Responses API** | In the application team's own environment. | A managed API for models, supported tools, and conversation state. |
| **Hosted Agentic Apps** | In a container hosted by OCI. | An application endpoint and managed infrastructure according to the deployment configuration. |

## 4. OCI Enterprise AI Agents Building Blocks

OCI Responses API offers an OpenAI-compatible interface for model routing, tool reasoning, and state management. File Search retrieves document content. Code Interpreter runs Python in a sandbox. Function Calling requests an application-provided function, and MCP Calling connects to an MCP server. (pp. 182–184)

| State or memory feature | Scope |
| --- | --- |
| **Short-term memory** | Context across turns in one conversation, managed through the Conversations API. |
| **Long-term memory** | Context across sessions associated with a `subject_id` in a project. |
| **Context compaction** | A shorter representation of long history that reduces the context the model processes. |

Files API manages file objects. Vector Stores API supports chunking, embeddings, retrieval, and metadata filtering. Containers API provides an isolated execution environment. (pp. 185–186)

## 5. Getting Started with OCI Enterprise AI Agents

OCI authentication can use a **Generative AI API Key** or **OCI IAM request signing**. In the OpenAI-compatible interface, `base_url` identifies the regional endpoint, the model identifier selects a model, and the `OpenAI-Project` header identifies the Generative AI project by its OCI resource identifier (OCID). `client.responses.create()` uses that configuration when sending a model request. (pp. 187–191)

## 6. OCI Enterprise AI Agents – Deploy and Scale

A hosted deployment packages agent logic and dependencies in a container image. OCI Container Registry stores the image. The deployment configuration governs identity, networking, storage, and scaling. The managed endpoint directs requests to the deployed application version. (pp. 192–195)
