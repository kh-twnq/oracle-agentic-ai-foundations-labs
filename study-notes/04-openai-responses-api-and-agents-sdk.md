# OpenAI Responses API and Agents SDK

Module 4 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), pp. 123–162 · [Index](README.md)

## API and Runtime Responsibilities

The **Responses API** accepts model input, makes declared tools available, and returns structured output. The **Agents SDK** uses the Responses API and adds agent configuration, a runner, handoffs, guardrails, and tracing. The application defines its business rules and controls the permissions of operations that affect external systems. (pp. 123–129)

| Approach | Ownership of the execution loop |
| --- | --- |
| **Responses API directly** | The application interprets responses and manages any additional steps. This suits short flows or applications that need explicit control over each transition. |
| **Agents SDK** | The application configures agents, tools, and handoff targets. The Runner coordinates model calls, tool execution, and agent transitions. |

![The OpenAI agent stack includes the Responses API, Agents SDK, guardrails, and tracing.](images/04-openai-agent-stack.png)

## Responses, Tools, and Conversation State

`client.responses.create()` associates input with a model. Input can be text or structured data. The response exposes individual output items, while `response.output_text` provides convenient access to the text. **Conversation chaining** uses `previous_response_id` to connect a new turn to the context of an earlier response. (pp. 130–133)

The platform can provide built-in tools such as **Web Search**, **File Search**, **Code Interpreter**, **Computer Use**, and **Image Generation**. The application declares which tools are available. The model selects a tool when the task requires one. (pp. 134–135)

## Runner and Function Calling

An `Agent` holds instructions, a model, and tools. `Runner.run_sync()` executes synchronously, and `Runner.run()` supports asynchronous execution. The Runner sends the input to the model, executes requested tools, and passes their results back into the loop. A completed run exposes its final result through `result.final_output`. (pp. 136–141)

| Tool type | Where the work happens |
| --- | --- |
| **Hosted Tools** | The platform provides and executes capabilities such as Web Search or Code Interpreter. |
| **Function Tools** | The application executes Python functions registered with `@function_tool`. Type hints and docstrings describe the interface exposed to the model. |
| **Agents as Tools** | `as_tool()` exposes a specialist agent as a tool. Its result returns to the agent that called it. |

A tool result can supply an argument for a later call. The Runner preserves that dependency, while application functions retain their own validation and business logic. (pp. 142–148) [Tool execution in LangChain](02-langchain-for-ai-agents.md#model-requests-and-tool-execution)

## Handoff and Manager Pattern

| Pattern | Who owns the remainder of the run? |
| --- | --- |
| **Handoff** | A triage agent routes the request and transfers control to a specialist. `handoff_description` states when to select a specialist, and `handoffs` defines the available targets. |
| **Manager pattern** | A central agent retains control, calls specialists via `as_tool()`, and uses their results to compose the final response. |

Handoffs fit requests with one primary owner. The manager pattern fits work that requires results from several specialists. (pp. 149–152, 157–162)

## Guardrails and Tracing

**Input guardrails** validate requests. Blocking execution waits for the check to finish before the agent starts. Concurrent execution can reduce waiting time by starting agent work before the check completes. **Output guardrails** check the final result against quality, policy, or data-handling requirements. An `@input_guardrail` can return `GuardrailFunctionOutput` with `tripwire_triggered` to stop a run. Pydantic represents structured validation results. (pp. 153–155)

**Tracing** records agent invocations, tool arguments, handoffs, guardrail decisions, latency, and token usage. Each span represents one operation, which allows developers to isolate the duration of a model call or tool execution. (pp. 156, 159–162)
