# Introduction to AI Agents

Module 1 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), pp. 9–54 · [Index](README.md)

## Agents, Chatbots, and Workflows

An **AI agent** uses a model to select the next step toward a goal. A tool result can change the model’s next decision and the resulting execution path. (pp. 9–16)

| System | What determines the next step? |
| --- | --- |
| **Chatbot** | The model generates a reply from the conversation and available context. |
| **Workflow** | Application rules determine the sequence of operations and the branches to follow. |
| **AI agent** | The model proposes an action based on the goal and current state. The application executes actions within its configured boundaries. |

## The Agent Execution Loop

The **Agent Runtime** runs the agent, and **orchestration** coordinates the model, tools, and state within each run. The execution loop has four stages. (pp. 15–21)

1. **Perceive.** The runtime receives the input or feedback and updates the run state.
2. **Reason.** The model uses the available context to propose a tool call or produce a final answer.
3. **Act.** The application validates the structured call and invokes the registered tool implementation.
4. **Observe.** The runtime adds the tool result to the context used for the next decision.

A **tool schema** describes the input the model can supply. The **tool implementation** performs the actual operation under the application's permissions. **State** records progress within a run, including messages and results. Short-term memory retains session context. Long-term memory can retrieve relevant information from earlier sessions or a knowledge base. The runtime can stop when the goal is met, an iteration limit is reached, an error requires a fallback, or the run needs human review. (pp. 17–21, 53–54)

![A model proposes actions, tools execute them, and orchestration coordinates the loop.](images/01-agent-components.png)

Model selection balances instruction following, reasoning capability, latency, and cost. A smaller model can handle routing while a more capable model handles a complex decision. An agent may call the model several times per request, so per-call cost and latency accumulate across the run. (pp. 19–21)

## Reasoning Patterns

| Pattern | Mechanism and trade-off |
| --- | --- |
| **Chain-of-Thought (CoT)** | Breaks a problem into intermediate reasoning steps. Its conclusions depend on the facts available to the model. |
| **ReAct (Reasoning + Acting)** | Interleaves decisions with tool calls and observations. New evidence can change the next action. |
| **Tree-of-Thoughts (ToT)** | Explores and evaluates multiple candidate paths. Additional branches require more evaluations. |

In a multi-step agent, one tool's output can become the next tool's input. That dependency makes the order of calls and the contents of the run state important. A trace can expose the tool name, arguments, and result for inspection. (pp. 22–27, 39–45) [Tool execution in LangChain](02-langchain-for-ai-agents.md#model-requests-and-tool-execution)

Agent frameworks encapsulate recurring orchestration mechanics. LangChain and LangGraph support stateful workflows, OpenAI Agents SDK provides orchestration, tracing, and guardrails, CrewAI groups agents by role, and Smolagents provides a lightweight agent framework. (pp. 28–30)

## Defense in Depth

Tools that read or modify external systems expand the impact of an agent run. **Prompt injection** introduces instructions through data the model reads. **Tool misuse** involves a call outside its authorized purpose. **Memory poisoning** persists harmful or misleading data across runs. **Data exfiltration** discloses protected data, and **runaway execution** consumes excess time, calls, or budget. (pp. 46–50)

| Control layer | Responsibility |
| --- | --- |
| **Input Validation** | Check input format and request rate. Treat retrieved content as untrusted data. |
| **LLM Guardrails** | Define behavioral limits and available tools. Escalate cases that need human review. |
| **Tool Boundaries** | Apply least privilege, validate arguments, isolate execution, and require human approval where appropriate. Idempotency limits duplicate effects when a write is retried. |
| **Output Filtering** | Check for sensitive data, personally identifiable information (PII), relevance, and supporting evidence. |
| **Observability** | Record traces, errors, latency, and cost. Redact sensitive values and monitor execution budgets. |

The runtime can enforce iteration limits. The tool's execution boundary is where the application can validate authorization before an operation takes effect. (pp. 51–54)
