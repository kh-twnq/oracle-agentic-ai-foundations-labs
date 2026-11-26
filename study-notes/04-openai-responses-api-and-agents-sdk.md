# OpenAI Responses API and Agents SDK

Module 4 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), pp. 123–162 · [Index](README.md)

## Agenda

1. [OpenAI Agent Stack](#1-openai-agent-stack)
2. [OpenAI Responses API](#2-openai-responses-api)
3. [OpenAI Agents SDK](#3-openai-agents-sdk)
4. [Tools and Function Calling](#4-tools-and-function-calling)
5. [Multi-Agent Systems with Handoffs](#5-multi-agent-systems-with-handoffs)
6. [Guardrails and Safety](#6-guardrails-and-safety)
7. [Putting it all together](#7-putting-it-all-together)

Student Guide agenda, p. 124. See [Module Review](#module-review) for variations of the five skill-check questions.

## 1. OpenAI Agent Stack

The **OpenAI agent stack** separates the application, the runtime, and the model API. The application owns business rules and permissions. The **Responses API** sends input to a model and returns structured output. The **Agents SDK** coordinates multi-step agent runs on top of the API. (pp. 125–129)

| Interface | Who controls the next step? | Typical use |
| --- | --- | --- |
| **Responses API directly** | Application code interprets responses and decides which calls to make next. | A single answer, a workflow with predefined steps, or a custom loop the application already manages. |
| **Agents SDK** | The configured runner manages the agent loop, including application function tools and handoffs. | **Workflows that need agent orchestration, guardrails, or collaboration between agents.** |

The Responses API also supports tool calling and multi-turn context. With direct API calls, the application handles any custom tool execution and follow-up requests itself. The choice depends on how much orchestration the application wants the SDK to manage.

![The OpenAI agent stack includes the Responses API, Agents SDK, guardrails, and tracing.](images/04-openai-agent-stack.png)

## 2. OpenAI Responses API

`client.responses.create()` takes a model and text or structured input. The response contains **output items** for structured processing, including messages or function calls. `response.output_text` is a convenience property for reading the response text. (pp. 130–132)

### Continuing a conversation

**`previous_response_id` links a new request to an earlier response so the model can continue with the prior conversation context.** The follow-up sends its new input and references the preceding response's `id`. This avoids manually resending the full earlier history with each request. (pp. 133–135)

```python
first = client.responses.create(
    model=model,
    input="Explain how an order return works.",
)

second = client.responses.create(
    model=model,
    previous_response_id=first.id,
    input="What happens if the order contains two items?",
)
```

Each request can supply its own top-level `instructions`. If the same instructions should apply again, pass them on the follow-up request. Prior input tokens in the chain still count toward input billing. An application can also manage history itself by passing the relevant earlier items in `input`. [Conversation state](https://developers.openai.com/api/docs/guides/conversation-state)

### Tools in a response

Available built-in tools can include Web Search, File Search, Code Interpreter, Computer Use, and Image Generation. The application declares which tools are available for the request. The model may request a tool or answer directly. For an application-defined function, the application executes the function and returns its result in a follow-up request. (pp. 133–135)

## 3. OpenAI Agents SDK

`Agent` holds instructions, a model, and tools. The **Runner** sends input to the model, executes requested function tools, and passes their results back. It repeats the loop until the run finishes or reaches a stopping condition. (pp. 136–141)

`Runner.run_sync()` runs synchronously. `Runner.run()` is asynchronous. The completed run exposes its final result as `result.final_output`. (pp. 138–141)

## 4. Tools and Function Calling

| Tool type | Who does the work? |
| --- | --- |
| **Hosted Tools** | The platform provides and executes a capability such as Web Search or Code Interpreter. |
| **Function Tools** | The application's Python function performs the operation. `@function_tool` exposes its definition to the agent. |
| **Agents as Tools** | `Agent.as_tool()` exposes a specialist agent. Its result returns to the agent that called it. |

### Function tool schemas

**`@function_tool` uses Python parameter type hints to generate the tool's input schema automatically.** For example, `get_order(order_id: str, include_items: bool)` yields an input shape with a string and a boolean. The docstring can describe the tool and its arguments so the model knows when and how to call it. Type hints describe inputs for both synchronous and asynchronous functions. [Agents SDK tools](https://openai.github.io/openai-agents-python/tools/)

The schema describes valid arguments. The function body performs the actual work and enforces business rules. For example, an order ID can have the right type while referring to an order the caller has no permission to view.

The runner passes intermediate tool results back to the model, so later calls can depend on them. (pp. 142–148) [Tool execution in LangChain](02-langchain-for-ai-agents.md#3-langchain-agent-under-the-hood)

## 5. Multi-Agent Systems with Handoffs

**Triage** routes a request to a suitable specialist. The orchestration pattern determines who controls the current run after routing. (pp. 149–152)

| Pattern | Who controls the turn? | How it is configured |
| --- | --- | --- |
| **Manager pattern** | **The manager keeps control, delegates bounded tasks to specialists, and can combine their results into the final answer.** | Expose specialists to the manager through `Agent.as_tool()`. |
| **Handoff** | The specialist becomes the active agent and can respond directly to the user. | List targets in `handoffs`. Use `handoff_description` to describe when to route to a specialist. |

For example, a support manager can ask an Orders specialist for delivery status and a Returns specialist for the return policy, then combine their results. If the Returns specialist should handle the rest of the user's turn directly, the triage agent can hand off to it. Specialists can have their own tools in either pattern. [Agent orchestration](https://openai.github.io/openai-agents-python/multi_agent/)

## 6. Guardrails and Safety

**Input guardrails** validate a request. A blocking check finishes before the agent starts. A concurrent check can overlap with agent work, so the run can begin before the guardrail result is known. **Output guardrails** check the final result. (pp. 153–154)

An `@input_guardrail` can return `GuardrailFunctionOutput` with `tripwire_triggered` set to stop the run. Pydantic can represent the structured result of a checker agent. (pp. 155–156)

### Tracing

**Tracing records what happened during an agent run so developers can monitor execution and debug failures.** A **trace** groups related operations. A **span** represents an individual operation, such as a model generation, a function tool call, a handoff, or a guardrail check. (pp. 155–156)

For example, if a returns request is slow, inspect the spans to see whether the delay came from a model call, a guardrail, or the order lookup. The guardrail can stop the run. Its span records what happened. [Agents SDK tracing](https://openai.github.io/openai-agents-python/tracing/)

## 7. Putting it all together

A customer support system combines an input guardrail, a triage agent, and specialists for order status, refunds, or frequently asked questions. The guardrail checks scope. Triage selects the specialist. The specialist calls the appropriate function or search tool and uses the result in its answer. (pp. 157–162)

A trace connects the routing decision to the selected tool and the final answer. It also shows whether latency came from a model call, a guardrail, or the function itself. (pp. 159–161)

## Module Review

### Q1. Manager pattern and handoffs

See [Multi-Agent Systems with Handoffs](#5-multi-agent-systems-with-handoffs).

- **What does the central manager do?** It delegates tasks to specialized agents, receives their results, and retains control of the turn.
- **When would you use a handoff?** When the specialist should become the active agent and handle the rest of the current turn directly.
- **What does `Agent.as_tool()` return control to?** The specialist's result goes back to the calling agent, which can decide what to do next.
- **Does the manager pattern determine how specialists schedule or use their tools?** The pattern determines who controls the turn. Tools, permissions, and execution scheduling depend on the agent and application configuration.

### Q2. Type hints and function tool definitions

See [Function tool schemas](#function-tool-schemas).

- **Why do type hints matter in `@function_tool`?** The SDK reads them to derive the expected types and generate the tool's input schema.
- **What does the docstring contribute?** It explains what the tool does and can describe individual arguments to help the model choose and call it.
- **Can an asynchronous function be used as a tool?** Yes. Type hints define the arguments. The function definition determines whether its implementation is synchronous or asynchronous.
- **Who checks whether the caller may access an order?** The tool or application service enforces that permission. The schema can describe an order ID as a string.

### Q3. Tracing and debugging

See [Tracing](#tracing).

- **Why enable tracing?** It shows the steps an agent took and helps locate failures, unexpected routing, or slow operations.
- **What is the difference between a trace and a span?** A trace groups related operations. A span records an individual operation, such as a tool call or handoff.
- **Where would you look if an agent selected the right specialist but answered with stale data?** Follow the handoff to the specialist, then inspect the data lookup and the result returned to the agent, when those details were captured.
- **Which component stops a disallowed request, and which records it?** A guardrail can stop the run when its tripwire triggers. Tracing records the guardrail event for inspection.

### Q4. Conversation chaining

See [Continuing a conversation](#continuing-a-conversation).

- **What does `previous_response_id` do?** It links the new request to the prior response, letting the model continue with the earlier context.
- **Which ID goes into the next request?** The `id` of the response you want to continue from. It identifies a response in the chain.
- **Do earlier top-level `instructions` carry over automatically?** Top-level `instructions` apply to the request that supplies them. Send them again when the follow-up should use the same instructions.
- **Does sending only the new input make prior context free?** Earlier input tokens in the chain still count toward input billing. The response ID saves you from manually resending the full history.

### Q5. Responses API versus Agents SDK

See [OpenAI Agent Stack](#1-openai-agent-stack).

- **When is the Agents SDK the better fit in the course framework?** When the application needs a runner to manage agent steps, guardrails, or coordination between agents.
- **When is the Responses API directly sufficient?** When the application needs one response or already controls a workflow whose steps it can manage itself.
- **Can a direct Responses API integration use custom tools?** Yes. The model can request the function. The application executes it and returns the result in a follow-up API call.
- **Does a multi-turn chat by itself require the Agents SDK?** The Responses API can continue context through `previous_response_id`. The SDK becomes useful when the application also needs orchestration, such as a tool loop or handoffs.
