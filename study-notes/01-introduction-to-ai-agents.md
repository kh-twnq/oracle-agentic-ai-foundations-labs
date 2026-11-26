# Introduction to AI Agents

Module 1 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), pp. 9–54 · [Index](README.md)

## Agenda

1. [What is an AI Agent?](#1-what-is-an-ai-agent)
2. [AI Agent Core Components](#2-ai-agent-core-components)
3. [Reasoning Patterns](#3-reasoning-patterns)
4. [Building your first AI Agent](#4-building-your-first-ai-agent)
5. [Safety & Guardrails](#5-safety--guardrails)

Student Guide agenda, p. 10. See [Module Review](#module-review) for related skill-check questions.

## 1. What is an AI Agent?

**An AI agent chooses its next action based on a goal and the information available at that point.** An LLM-based agent combines a model, tools, and an execution loop. Tool results can change the path the agent takes. (pp. 11–16)

| System | What determines the next step? |
| --- | --- |
| Chatbot | The model produces a reply from the conversation and available context. |
| Workflow | **Application rules define the steps and branch conditions in advance.** |
| AI agent | **The model proposes the next action from the goal, current context, and tool results.** The application enforces permissions. |

## 2. AI Agent Core Components

| Component | Responsibility |
| --- | --- |
| **Model** | Interprets the goal, selects a tool and arguments, or produces an answer. |
| **Tools** | Perform operations such as retrieving data or calling an API. A schema tells the model which arguments a tool accepts. |
| **Agent Runtime** | Runs the agent and maintains its state. Orchestration coordinates model calls, tool execution, and stopping conditions. |

![The model proposes an action, tools execute it, and orchestration coordinates the loop.](images/01-agent-components.png)

The **Agent Execution Loop** is `Perceive → Reason → Act → Observe`.

- **Perceive.** Receive the request and relevant context.
- **Reason.** Choose the next step with the information available.
- **Act.** Validate the proposed tool call and execute it if allowed.
- **Observe.** **Receive the result of the previous action and make it available for the next decision.** An observation can be returned data, an empty result, or a tool error.

For example, after a chatbot calls `get_order`, it observes the returned status. A delivered order can lead to a return-policy lookup. An empty result can lead to asking for the order ID again.

The runtime can stop at a final answer, an iteration limit, an error, or a handoff to a person. (pp. 15–21)

**State** records the current run, including its messages and tool results. **Short-term memory** retains session context. **Long-term memory** can supply information from earlier sessions or a knowledge base. Model selection balances capability, cost, and latency, which can accumulate over several calls in one run. (pp. 19–21, 53–54)

## 3. Reasoning Patterns

| Pattern | What it does | Main constraint |
| --- | --- | --- |
| **Chain-of-Thought (CoT)** | Breaks a problem into intermediate reasoning steps. | Its conclusions depend on the information available to the model. |
| **ReAct** | Alternates between reasoning, tool calls, and observations. | Each extra turn adds work, but can incorporate new evidence. |
| **Tree-of-Thoughts (ToT)** | **Explores multiple candidate solution paths and evaluates them before continuing.** | More branches require more evaluations. |

Tree-of-Thoughts can revisit another branch when the current path stalls. Exploring several branches is a search strategy. The evaluations can run sequentially. **Sequential prompting** passes the output of one prompt to the next in a predefined sequence.

ReAct is useful when the next decision depends on the outside world. An observation can change the plan, and a tool result can become input to a later tool call. (pp. 22–27, 43–45)

## 4. Building your first AI Agent

In LangChain, `init_chat_model()` selects the model, and `@tool` registers functions. A tool definition exposes the function name, description, and parameter schema. `create_agent()` binds the model to its tools. `agent.invoke()` passes the user message to the runtime. A tool result can then supply an argument for a later call. (pp. 31–45)

### Defining a tool's input schema

**Python type hints help LangChain generate the input schema for a tool.** In `get_order(order_id: str, include_items: bool = False)`, the schema can describe `order_id` as a required string and `include_items` as an optional boolean with a default. The docstring explains what the tool does and when to use it. The schema describes the shape of a valid request. The tool still checks authorization and business rules before accessing an order. [LangChain tool definitions](https://docs.langchain.com/oss/python/langchain/tools)

LangChain and LangGraph support stateful orchestration. OpenAI Agents SDK provides a runner, tracing, and guardrails. CrewAI organizes agents by role, and Smolagents offers a lightweight framework. The choice depends on how much orchestration the application needs. (pp. 28–30) [Tool execution in LangChain](02-langchain-for-ai-agents.md#3-langchain-agent-under-the-hood)

## 5. Safety & Guardrails

Tools can read data or produce side effects. **Prompt injection** introduces instructions through data. **Tool misuse** uses a tool outside its intended purpose. **Memory poisoning** persists harmful or misleading input. **Data exfiltration** discloses protected information. **Runaway execution** consumes excess time or budget. (pp. 46–50)

| Defense in Depth layer | Control |
| --- | --- |
| **Input validation** | Check format and request rate. Treat retrieved content as untrusted data. |
| **LLM guardrails** | Define behavioral limits and restrict the tools available to the model. |
| **Tool boundaries** | **Restrict what a tool can do and which data it can access.** Enforce least privilege, validate arguments, isolate execution, and require human approval where appropriate. Use idempotency to limit duplicate effects on a retry. |
| **Output filtering** | Check for personally identifiable information (PII), sensitive content, and relevance. |
| **Observability** | Record traces, errors, latency, and cost. Redact sensitive values and monitor run limits. |

For example, validate the format of an incoming order ID at the application boundary. When the order tool runs, check that the caller can access that specific order. A refund tool can also require approval before issuing the refund. Authorization belongs at the point where the operation takes effect. A runtime iteration limit controls how long an agent keeps trying. (pp. 51–54)

## Module Review

### Q1. Defense in depth and tool boundaries

See [Safety & Guardrails](#5-safety--guardrails).

- **Which layer restricts dangerous tool behavior?** Tool boundaries enforce what the tool can do at execution time, including permitted actions, data access, and approval requirements.
- **Where does an order ownership check belong?** At the tool or service boundary. A valid order ID can still identify an order the caller has no permission to read.
- **Which layer checks an incoming request, a final reply, or a run trace?** Input validation checks the request. Output filtering checks the reply for sensitive data. Observability records what happened so operators can inspect it.
- **What can limit duplicate refunds if a call is retried?** An idempotency key lets the refund service recognize a repeated request and avoid issuing the refund twice.

### Q2. Python type hints and tool schemas

See [Defining a tool's input schema](#defining-a-tools-input-schema).

- **Why are type hints useful in an agent tool?** A framework such as LangChain can use them to generate the tool's input schema. The model then receives the names and expected types of the arguments.
- **How can you tell which parameters are required in the example?** `order_id: str` has no default, so the caller must supply it. `include_items: bool = False` has a default, so the caller can omit it.
- **What is the difference between a type hint and a docstring?** The type hint describes an argument's type. The docstring describes what the tool does and helps the model decide when to call it.
- **Does a valid tool schema establish permission to run an action?** Schema validation checks the input shape. The application must check permissions and business rules before executing the action.

### Q3. Reasoning patterns

See [Reasoning Patterns](#3-reasoning-patterns).

- **Which approach explores multiple candidate solution paths?** Tree-of-Thoughts branches, evaluates alternatives, and can return to another branch if the current one stalls. [Tree of Thoughts paper](https://proceedings.nips.cc/paper_files/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract-Conference.html)
- **Which approach breaks a problem into intermediate reasoning steps?** Chain-of-Thought. A typical example works through one sequence of steps.
- **Which approach lets a tool result change the next step?** ReAct alternates between reasoning and acting, using observations from tool calls to inform the next decision.
- **When is sequential prompting a good fit?** When you can define the stages in advance, such as extracting fields, checking them, and formatting the result.

### Q4. AI agent versus fixed workflow

See [What is an AI Agent?](#1-what-is-an-ai-agent).

- **What distinguishes an agent from a fixed workflow?** The agent chooses a next action at runtime from its goal, context, and observations. A fixed workflow applies predefined rules and branches.
- **Can a fixed workflow contain conditional branches?** Yes. A rule such as “if delivered, check return eligibility” is still a predefined branch.
- **Does adding an LLM to one workflow step make the workflow agentic?** The control flow can remain fixed. For example, a predefined final step can use an LLM to summarize an order. The application still defines what runs next.
- **Can an agent have fixed rules?** Yes. For example, the agent can choose whether to look up an order while the application always requires approval before issuing a refund.

### Q5. Observe in the agent loop

See [AI Agent Core Components](#2-ai-agent-core-components).

- **What is the purpose of Observe?** Receive and use the result of the previous action, such as a tool response or error, so the next decision can use that information.
- **How do Perceive and Observe differ in this loop?** Perceive receives the request and relevant context. Observe receives feedback from an action the agent has taken.
- **What can happen after an observation?** The agent can answer, select another tool, ask for missing information, or stop according to its runtime rules.
- **Does observing a tool result train the model?** The result becomes context for the current run. Model training changes model parameters through a separate process.
