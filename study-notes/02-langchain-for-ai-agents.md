# LangChain for AI Agents

Module 2 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), pp. 55–89 · [Index](README.md)

## The LangChain Ecosystem

LangChain provides components for preparing prompts, calling models, interpreting output, and accessing tools or data. A **chain** composes a defined sequence of components. An **agent** uses a model to select actions as the run progresses. **Retrieval-Augmented Generation (RAG)** supplies retrieved material as context for generation. (pp. 55–59)

| Component | Responsibility |
| --- | --- |
| **LangChain** | Composable models, prompts, chains, tools, and memory components. |
| **LangGraph** | Graph-based orchestration for workflows with state, branching, and loops. |
| **LangSmith** | Observability, tracing, testing, and debugging. |
| **Integrations** | Connections to model providers, databases, search APIs, and other services. |

**A unified model interface lets developers switch providers with minimal code changes.** `init_chat_model()` resolves a model identifier with a provider prefix. The application-facing interface is shared, while tool-calling behavior, context limits, and reasoning capabilities depend on the chosen model. Integration packages and credentials depend on the provider. (pp. 60, 71, 89)

## Prompt Templates and LCEL

| Prompt format | Purpose |
| --- | --- |
| `PromptTemplate` | Produces plain text by filling in named variables. |
| `ChatPromptTemplate` | Produces role-based messages, including system instructions, human input, and previous AI responses. |
| Few-shot prompt | Includes input-output pairs that illustrate the expected behavior. |

**LangChain Expression Language (LCEL) connects components with the pipe operator `|`, passing each component's output to the next.** A common chain formats a prompt, sends it to a model, and uses `StrOutputParser()` to extract text from the model response. (pp. 61–62, 89)

![LCEL passes the prompt to the model and the model response to StrOutputParser.](images/02-langchain-chain.png)

## Tool Schemas and Agent Control Flow

A tool allows the agent to request work such as a database query, an API call, or a computation. LangChain supports built-in tools and custom Python functions registered with `@tool`. The function name and type hints contribute to the input schema. The docstring explains when the model should select the tool, and the return annotation describes the expected result. The function body implements the operation. A tool definition exposes `name`, `description`, and `parameters`, including required inputs. (pp. 63–69, 75)

In **ReAct**, a model decision can lead to a tool call. The runtime supplies the resulting observation so the model can decide whether it has enough information to answer. `create_agent()` associates a model with its available tools, and `agent.invoke()` starts a run with the supplied conversation messages. (pp. 70–74)

## Model Requests and Tool Execution

**The initial Model API request contains the user message in `messages` and the available tool definitions in `tools`.** The model can respond with structured `tool_calls`, each containing a tool name, arguments, and a call ID. In this Model API response format, arguments are encoded as a JSON string. (pp. 74–77)

**The model selects the tool and arguments. LangChain resolves the name in the tool registry and executes the function in the application.** It then appends a result as a `tool` message with a matching `tool_call_id`. Subsequent requests carry the conversation history and tool definitions. This lets the model associate each observation with its call and use earlier results in later decisions. The loop ends when the model returns a final text response with no remaining tool calls. (pp. 78–85, 87–89)

## Tracing and Debugging

**Understanding the work behind `agent.invoke()` helps developers debug failures, build custom loops, optimize performance, and operate agents in production.** A trace can identify the tool schema sent to the model, the name and arguments it returned, the function selected by the registry, and the result added to state. These points distinguish a request or selection issue from an execution issue. (pp. 85–89)
