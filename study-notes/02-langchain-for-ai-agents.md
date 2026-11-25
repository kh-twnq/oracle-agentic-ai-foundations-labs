# LangChain for AI Agents

Module 2 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), pp. 55–89 · [Index](README.md)

## Agenda

1. [Introduction to LangChain](#1-introduction-to-langchain)
2. [Build your first agent using LangChain](#2-build-your-first-agent-using-langchain)
3. [LangChain Agent under the hood](#3-langchain-agent-under-the-hood)

Student Guide agenda, p. 56.

## 1. Introduction to LangChain

LangChain supplies components for composing LLM applications. A **chain** connects a defined sequence of steps. An **agent** lets the model select the next action during a run. **Retrieval-Augmented Generation (RAG)** places retrieved material in the model's context. (pp. 57–59)

| Component | Purpose |
| --- | --- |
| **LangChain** | Composes models, prompts, chains, tools, and memory. |
| **LangGraph** | Represents state, branches, and loops as a graph. |
| **LangSmith** | Supports tracing, inspection, testing, and debugging. |
| **Integrations** | Connect to model providers, databases, search APIs, and other services. |

**A unified model interface lets developers switch providers with minimal code changes.** `init_chat_model()` accepts a model identifier with a provider prefix. Tool calling, context limits, and reasoning capability still depend on the selected model. Integration packages and credentials are provider-specific. (pp. 60, 71, 89)

### Prompt templates and LCEL

`PromptTemplate` fills variables in text. `ChatPromptTemplate` builds role-based messages for system instructions, human input, and previous AI responses. A **few-shot prompt** uses input-output pairs to demonstrate the expected behavior. (p. 61)

**LangChain Expression Language (LCEL) uses the pipe operator `|` to pass the output of one component to the next.** In a typical chain, a prompt goes to the model, and `StrOutputParser()` extracts the text from the response. (pp. 62, 89)

![LCEL passes a prepared prompt to the model and the response to StrOutputParser.](images/02-langchain-chain.png)

## 2. Build your first agent using LangChain

A basic model call returns an output from its input. An agent can act, observe the result, and use that observation to decide what to do next. This is **ReAct**. It suits tasks that depend on current data or intermediate results. (pp. 63–65, 70)

| Tool metadata | What the model or framework uses it for |
| --- | --- |
| `@tool` | Registers a Python function as a callable tool. |
| Function name and type hints | Identify the tool and define the input fields and types. |
| Docstring | Describes what the tool does and when to select it. |
| Return annotation | Describes the expected result type. |
| Function body | Performs the operation when the application calls the function. |

A tool definition contains `name`, `description`, and `parameters`. The parameters schema identifies required inputs. `create_agent()` binds the model to its tools, and `agent.invoke()` starts a run with the supplied messages. (pp. 66–74)

## 3. LangChain Agent under the hood

**The first Model API request carries the user message in `messages` and the available tool definitions in `tools`.** The model can answer or return `tool_calls` with a name, arguments, and a call ID. In the response format shown here, arguments arrive as a JSON string. (pp. 74–77)

**The model selects the tool and arguments. LangChain resolves the name in the tool registry and executes the function in the application.** The runtime adds the result as a `tool` message. Its `tool_call_id` matches the original request. The next model call receives the updated history, so the model can use that result to choose another action or finish. (pp. 78–85, 87–89)

**Understanding the work behind `agent.invoke()` helps developers debug failures, build custom loops, optimize performance, and operate agents in production.** Inspect the tool definition, the model's arguments, the resolved function, and the message added to the history to locate a failure. (pp. 85–89)
