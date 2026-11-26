# LangChain for AI Agents

Module 2 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), pp. 55–89 · [Index](README.md)

## Agenda

1. [Introduction to LangChain](#1-introduction-to-langchain)
2. [Build your first agent using LangChain](#2-build-your-first-agent-using-langchain)
3. [LangChain Agent under the hood](#3-langchain-agent-under-the-hood)

Student Guide agenda, p. 56. See [Module Review](#module-review) for variations of the five skill-check questions.

## 1. Introduction to LangChain

LangChain supplies components for composing LLM applications. A **chain** connects a defined sequence of steps. An **agent** lets the model select the next action during a run. **Retrieval-Augmented Generation (RAG)** places retrieved material in the model's context. (pp. 57–59)

| Component | Purpose |
| --- | --- |
| **LangChain** | Composes models, prompts, chains, tools, and memory. |
| **LangGraph** | Represents state, branches, and loops as a graph. |
| **LangSmith** | Supports tracing, inspection, testing, and debugging. |
| **Integrations** | Connect to model providers, databases, search APIs, and other services. |

### Unified model interface

**A unified model interface lets developers switch providers with minimal changes to the application code.** `init_chat_model()` accepts a provider-prefixed model identifier. Application code can continue calling `model.invoke(...)` while the selected integration translates the request for its provider. (pp. 60, 71, 89)

Changing providers can still require a different integration package, credentials, and model settings. Check whether the new model supports the features the application uses, such as tool calling or structured output. Response quality, context limits, cost, and latency can vary. Fine-tuning, if needed, is a separate operation. [LangChain models](https://docs.langchain.com/oss/python/langchain/models)

### Prompt templates and LCEL

`PromptTemplate` fills variables in text. `ChatPromptTemplate` builds role-based messages for system instructions, human input, and previous AI responses. A **few-shot prompt** uses input-output pairs to demonstrate the expected behavior. (p. 61)

**LangChain Expression Language (LCEL) uses the pipe operator `|` to compose components. Each step's output becomes the next step's input.** In a typical sequence, the prompt template builds messages, the model generates a response, and `StrOutputParser()` extracts text from that response. (pp. 62, 89)

```python
chain = prompt | model | StrOutputParser()
answer = chain.invoke({"question": "What is the return policy?"})
```

The first component receives the input to `invoke()`. The last component determines the chain's output. If another component needs a different shape, add a step to transform the data. A retrieval chain can also include a retriever that gets documents from a vector store. LCEL connects the steps, and the vector store handles storage and search. [RunnableSequence](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableSequence)

![LCEL passes a prepared prompt to the model and the response to StrOutputParser.](images/02-langchain-chain.png)

## 2. Build your first agent using LangChain

A basic model call returns an output from its input. An agent can act, observe the result, and use that observation to decide what to do next. This is **ReAct**. It suits tasks that depend on current data or intermediate results. (pp. 63–65, 70)

| Tool metadata or implementation | Purpose |
| --- | --- |
| `@tool` | Registers a Python function as a callable tool. |
| Function name and type hints | Identify the tool and define the input fields and types. |
| Docstring | Describes what the tool does and when to select it. |
| Return annotation | Describes the expected result type. |
| Function body | Performs the operation when the application calls the function. |

The tool definition sent to the model describes its name, purpose, and accepted arguments. In the API format used by the course, these appear as `name`, `description`, and `parameters`. The parameter schema identifies required inputs. `create_agent()` configures the agent with its model and tools. `agent.invoke()` starts a run with the supplied messages. (pp. 66–74)

## 3. LangChain Agent under the hood

### First model request

**On the first model call, LangChain sends the user message and the available tool definitions.** The model can also receive system instructions and earlier messages, if the application supplied them. In the API format shown in the course, the messages go in `messages` and the tool definitions go in `tools`. (pp. 74–77)

For an order-status request, the model might receive the question “Where is order ORD-42?” and a definition for `get_order` that says it takes an `order_id` string. The definition describes how to request the operation. The application's Python implementation and order database stay on the application side.

### Tool call and execution

**The model can propose a tool call. LangChain runs the registered Python function in the application.** The model returns a tool name, arguments, and a call ID. In the API response shown in the course, the arguments are encoded as a JSON string. LangChain's normalized `AIMessage.tool_calls` presents the parsed arguments as a dictionary. (pp. 78–85, 87–89) [LangChain models](https://docs.langchain.com/oss/python/langchain/models)

1. The model requests `get_order` with `order_id="ORD-42"`.
2. The runtime resolves the name to the registered tool and runs it with the supplied arguments. The application can enforce permissions or require approval for selected actions.
3. The runtime records the result as a `ToolMessage`. Its `tool_call_id` links it to the original request.
4. The next model call receives the updated messages. The model can answer using the result or request another tool.

If a model provides a final answer on its first call, the runtime may finish without executing any tool. [LangChain agents](https://docs.langchain.com/oss/python/langchain/agents)

### Debugging and production optimization

**Understanding the steps behind `agent.invoke()` helps developers isolate failures and measure where time and cost accumulate.** Inspect the tool definitions, the model's proposed arguments, the executed function, and the result added to the message history. The same sequence helps when you need to customize the loop. (pp. 85–89)

| Symptom | Where to look first |
| --- | --- |
| The model chooses the wrong tool. | Check the tool descriptions and which tools were exposed for that call. |
| The model supplies invalid arguments. | Compare the requested arguments with the input schema and validation error. |
| The tool runs but the answer ignores its result. | Check that the tool result was added to the next model request with the matching call ID. |
| The run is slow or expensive. | Measure model calls and tool calls separately. Check the number of iterations and the size of the context sent on each call. |

## Module Review

### Q1. Unified model interface

See [Unified model interface](#unified-model-interface).

- **Why does LangChain provide a unified interface?** It keeps common operations such as `invoke()` consistent, so switching providers can require fewer changes to the calling code.
- **What may still need to change when switching providers?** The model configuration, integration package, and credentials. Also check support for features your application depends on.
- **Can two providers return different results for the same input?** Yes. The common interface standardizes how the application calls a model. Each model can behave differently.
- **Does changing the provider train the model on your application data?** Switching selects a different model integration. Fine-tuning is a separate process.

### Q2. LCEL and chains

See [Prompt templates and LCEL](#prompt-templates-and-lcel).

- **What does the `|` operator do in LCEL?** It composes components so the output of one step becomes the input of the next.
- **What flows through `prompt | model | StrOutputParser()`?** Prompt variables become model messages. The model returns a response. The parser extracts its text.
- **What if the next component needs a different input shape?** Add a transformation step that produces the shape it expects.
- **What is the role of LCEL in a retrieval chain?** LCEL connects the retrieval and generation steps. The retriever obtains relevant documents from its data source, which can be a vector store.

### Q3. Debugging and optimizing agent runs

See [Debugging and production optimization](#debugging-and-production-optimization).

- **Why learn what happens inside `agent.invoke()`?** It helps you locate failures and identify which model calls, tool calls, or repeated steps drive latency and cost.
- **Where should you look if the model selects the wrong tool?** Inspect the tools exposed on that call, their descriptions, and the messages the model received.
- **Where should you look if a tool ran successfully but the answer missed its result?** Check whether the tool result was included in the next model call and linked to the correct call ID.
- **What should you measure before trying to speed up a run?** The number and duration of model calls and tool calls, plus context size. The slowest part may be a downstream service or several agent iterations.

### Q4. What the first model request contains

See [First model request](#first-model-request).

- **What does the first model request include in the course example?** The user's message and the available tool definitions. System instructions or earlier messages may also be included when supplied.
- **What does the model learn about `get_order` on that request?** Its name, description, and accepted arguments. These let the model decide whether to request it and how to supply the `order_id`.
- **When is the order status added to the conversation?** After the application runs `get_order` and adds the result as a tool message for the next model call.
- **Can the agent finish after its first model call?** Yes. The model can return a final answer when the available context is enough.

### Q5. Tool request versus tool execution

See [Tool call and execution](#tool-call-and-execution).

- **Why does the model return a tool call?** It proposes an action by naming a tool and supplying arguments. The application owns and executes the registered function.
- **Can it request a custom Python function?** Yes, when the application registers it as a tool and exposes its definition to the model.
- **How does the runtime associate multiple tool results with their requests?** Each `ToolMessage` uses the `tool_call_id` of the request it answers.
- **When is manual approval needed?** When the application configures an approval rule for that action. For example, it can allow order lookups directly and require approval before issuing a refund.
