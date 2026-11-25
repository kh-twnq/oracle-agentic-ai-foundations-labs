# Introduction to AI Agents

Module 1 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), pp. 9–54 · [Index](README.md)

## Agenda

1. [What is an AI Agent?](#1-what-is-an-ai-agent)
2. [AI Agent Core Components](#2-ai-agent-core-components)
3. [Reasoning Patterns](#3-reasoning-patterns)
4. [Building your first AI Agent](#4-building-your-first-ai-agent)
5. [Safety & Guardrails](#5-safety--guardrails)

Student Guide agenda, p. 10.

## 1. What is an AI Agent?

**An AI agent chooses its next action based on a goal and the information available at that point.** An LLM-based agent combines a model, tools, and an execution loop. Tool results can change the path the agent takes. (pp. 11–16)

| System | What determines the next step? |
| --- | --- |
| Chatbot | The model produces a reply from the conversation and available context. |
| Workflow | Application rules determine the steps and branches. |
| AI agent | The model proposes an action. The application can execute it within the permissions it has granted. |

## 2. AI Agent Core Components

| Component | Responsibility |
| --- | --- |
| **Model** | Interprets the goal, selects a tool and arguments, or produces an answer. |
| **Tools** | Perform operations such as retrieving data or calling an API. A schema tells the model which arguments a tool accepts. |
| **Agent Runtime** | Runs the agent and maintains its state. Orchestration coordinates model calls, tool execution, and stopping conditions. |

![The model proposes an action, tools execute it, and orchestration coordinates the loop.](images/01-agent-components.png)

The **Agent Execution Loop** is `Perceive → Reason → Act → Observe`. The runtime receives input. The model proposes the next step. The application validates and executes any tool call. The runtime returns the result to the model for the next decision. It can stop at a final answer, an iteration limit, an error, or a handoff to a person. (pp. 15–21)

**State** records the current run, including its messages and tool results. **Short-term memory** retains session context. **Long-term memory** can supply information from earlier sessions or a knowledge base. Model selection balances capability, cost, and latency, which can accumulate over several calls in one run. (pp. 19–21, 53–54)

## 3. Reasoning Patterns

| Pattern | What it does | Main constraint |
| --- | --- | --- |
| **Chain-of-Thought (CoT)** | Breaks a problem into intermediate reasoning steps. | Its conclusions depend on the information available to the model. |
| **ReAct** | Alternates between reasoning, tool calls, and observations. | Each extra turn adds work, but can incorporate new evidence. |
| **Tree-of-Thoughts (ToT)** | Explores and evaluates several candidate paths. | More branches require more evaluations. |

ReAct is useful when the next decision depends on the outside world. An observation can change the plan, and a tool result can become input to a later tool call. (pp. 22–27, 43–45)

## 4. Building your first AI Agent

In LangChain, `init_chat_model()` selects the model, and `@tool` registers functions. A tool definition exposes the function name, description, and parameter schema. `create_agent()` binds the model to its tools. `agent.invoke()` passes the user message to the runtime. A tool result can then supply an argument for a later call. (pp. 31–45)

LangChain and LangGraph support stateful orchestration. OpenAI Agents SDK provides a runner, tracing, and guardrails. CrewAI organizes agents by role, and Smolagents offers a lightweight framework. The choice depends on how much orchestration the application needs. (pp. 28–30) [Tool execution in LangChain](02-langchain-for-ai-agents.md#3-langchain-agent-under-the-hood)

## 5. Safety & Guardrails

Tools can read data or produce side effects. **Prompt injection** introduces instructions through data. **Tool misuse** uses a tool outside its intended purpose. **Memory poisoning** persists harmful or misleading input. **Data exfiltration** discloses protected information. **Runaway execution** consumes excess time or budget. (pp. 46–50)

| Defense in Depth layer | Control |
| --- | --- |
| **Input validation** | Check format and request rate. Treat retrieved content as untrusted data. |
| **LLM guardrails** | Define behavioral limits and restrict the tools available to the model. |
| **Tool boundaries** | Enforce least privilege, validate arguments, isolate execution, and require human approval where appropriate. Use idempotency to limit duplicate effects on a retry. |
| **Output filtering** | Check for personally identifiable information (PII), sensitive content, and relevance. |
| **Observability** | Record traces, errors, latency, and cost. Redact sensitive values and monitor run limits. |

Authorization belongs at the point where the operation takes effect. A runtime iteration limit controls how long an agent keeps trying. (pp. 51–54)
