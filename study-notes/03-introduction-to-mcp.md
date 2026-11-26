# Introduction to MCP

Module 3 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), pp. 91–121 · [Index](README.md)

## Agenda

1. [What is Model Context Protocol?](#1-what-is-model-context-protocol)
2. [MCP Core Components](#2-mcp-core-components)
3. [Add MCP Server to your first Agent](#3-add-mcp-server-to-your-first-agent)
4. [Real World MCP Walkthrough](#4-real-world-mcp-walkthrough)

Student Guide agenda, p. 92.

[Module Review](#module-review) covers variations of all five quiz questions.

## 1. What is Model Context Protocol?

**Model Context Protocol (MCP) is an open standard that connects AI applications to external tools, data sources, and systems.** For tools, **MCP standardizes how a client discovers what a server offers and calls a specific tool**. A Java host can call a Python MCP server through the same protocol.

The host still coordinates the agent loop. The server can call an existing REST API inside a tool handler, as in the OCI example below.

Anthropic introduced MCP in November 2024. The project is part of the Linux Foundation's Agentic AI Foundation. (pp. 93–94)

### The integration problem

| Integration model | Cost for N applications and M services | 3 applications and 4 services |
| --- | --- | --- |
| Pairwise connectors | Up to `N × M` adapters, one per application–service pair. | 12 adapters |
| Shared MCP protocol | `N + M` protocol integrations, one per application or service. | 7 integrations |

**`N + M` counts protocol implementations.** A host still needs a client connection for each server it uses. (pp. 95–96)

## 2. MCP Core Components

| Role | Responsibility |
| --- | --- |
| **Host** | Runs the AI application, coordinates the model, and manages MCP clients. |
| **MCP client** | Handles protocol communication with one server. |
| **MCP server** | Publishes capabilities, **executes the tools it provides**, and returns their results. |

A server can expose **Tools** for actions, **Resources** for URI-addressed data, and **Prompts** for reusable templates. The host decides how to present available capabilities to the model and the user. (pp. 96–98)

### Connection lifecycle

1. **Initialize.** The client uses `initialize` to negotiate a protocol version and exchange capabilities with the server. The client then sends an initialized notification.
2. **Discover.** **`tools/list` returns tool names, descriptions, and `inputSchema` definitions.** Resources and prompts have their own discovery methods.
3. **Operate.** **The client uses `tools/call` to invoke a specific tool by name with its arguments.** The server runs the tool and returns the result.
4. **Shutdown.** The client closes the connection. (pp. 99–102)

A client can subscribe to resource updates with `resources/subscribe` if the server supports subscriptions. When that resource changes, the server can send `notifications/resources/updated`.

### Tool input schema

**`inputSchema` is the JSON Schema for a tool's arguments.** It describes the expected structure, field types, required fields, and any declared constraints. The client can use it to construct valid tool requests.

For example, `get_order` can declare that `order_id` is a string and must be present.

```json
{
  "type": "object",
  "properties": {
    "order_id": {
      "type": "string"
    }
  },
  "required": ["order_id"]
}
```

The client then sends actual values in the `arguments` field of the `tools/call` parameters.

```json
{
  "name": "get_order",
  "arguments": {
    "order_id": "ORD-42"
  }
}
```

Connection configuration determines transport and authentication. Deployment determines where the server runs.

### Messages and transports

MCP uses **JSON-RPC 2.0** to structure messages. A request has a `method` and optional `params`. A request ID correlates the request with its result or error response. A notification omits the ID. Tool results can include a `content` field. (pp. 100–102)

| Transport | Communication channel |
| --- | --- |
| **stdio** | A local process exchanges messages with the client through standard input and output. |
| **Streamable HTTP** | A client sends HTTP requests to an endpoint. Responses can use Server-Sent Events (SSE), and the service can require HTTP authentication. |

**JSON-RPC defines the message structure. The transport carries the messages.** Tool discovery and invocation serve the same purpose on either transport. (p. 103)

## 3. Add MCP Server to your first Agent

Moving a local tool to MCP changes where the tool handler runs. The model can propose a tool call. The host coordinates the agent loop, and the MCP client sends the request. **The MCP server runs the tool handler and returns the result.** (pp. 104–115)

![The MCP client sends the request. The server executes the tool and returns the result.](images/03-mcp-tool-layer.png)

`FastMCP` can expose functions registered with `@mcp.tool()`. **`MultiServerMCPClient` manages independent connections to the configured servers. Its `get_tools()` method combines the discovered tools into one list the LangChain agent can use.**

For example, the agent can see `get_order` from the Orders server and `check_stock` from the Inventory server. A call to `get_order` goes to the Orders server. The servers run independently and expose their own tools.

Direct calls suit simple local logic. An MCP interface helps when multiple applications share the same tools or when another service owns the implementation. (pp. 107–115, 121)

## 4. Real World MCP Walkthrough

A server can receive an MCP request through one transport and call a downstream service through another. OCI Usage MCP Server illustrates this boundary. (pp. 116–120)

**MCP client → stdio → OCI Usage MCP Server → HTTPS → OCI Usage REST API**

The MCP server uses an OCI configuration profile to authenticate the downstream request. `get_summarized_usage` accepts a tenancy, time range, `granularity`, `group_by`, and `query_type`. These fields belong to the OCI tool. The client discovers and invokes it through the same MCP interface used for other tools. (pp. 118–121)

## Module Review

### Q1. MCP as a standardized tool execution layer

See [What is Model Context Protocol?](#1-what-is-model-context-protocol).

- **Why is MCP called a standardized tool execution layer?** It gives AI applications a common way to discover and invoke tools exposed by external servers.
- **What does `N + M` count?** It counts integrations with the shared protocol. Each of the N applications implements the client side, and each of the M services implements the server side. A running host still connects to the servers it uses.
- **Can a Java application call a Python MCP tool?** Yes. The Java client and Python server communicate through the same protocol, while the Python server executes its own tool handler.
- **How can REST and MCP appear in the same workflow?** The agent's client uses MCP to invoke a tool. The tool handler can use REST to call an existing service.
- **What happens to the agent loop after you add MCP?** The host still coordinates the model, tool calls, and results. MCP supplies the interface for calls to external tool servers.

### Q2. Tool discovery and invocation

See [Connection lifecycle](#connection-lifecycle).

- **What does `tools/call` do?** It requests execution of one tool by name and passes the arguments for that call.
- **Which method tells you what tools and arguments are available?** `tools/list` returns the tool definitions, including their `inputSchema`.
- **When is the protocol version negotiated?** During `initialize`, before normal discovery and invocation.
- **How can a client learn that a resource changed?** If the server supports subscriptions, the client can use `resources/subscribe` and receive `notifications/resources/updated` when the resource changes.

### Q3. Understanding `inputSchema`

See [Tool input schema](#tool-input-schema).

- **What does `inputSchema` describe?** The expected structure and types of tool arguments, including any required fields or other declared constraints.
- **How do you know whether `order_id` is mandatory?** Check whether it appears in `required`. Declaring it as a string under `properties` specifies its type.
- **What is the difference between `inputSchema` and `arguments`?** The schema defines the expected input. `arguments` contains the actual values for a specific call, such as `{"order_id":"ORD-42"}`.
- **Where are authentication, transport, and tool location determined?** Authentication and transport come from the connection configuration. Tool location comes from deployment.

### Q4. Who does what in a tool call?

See [MCP Core Components](#2-mcp-core-components) and [Add MCP Server to your first Agent](#3-add-mcp-server-to-your-first-agent).

- **Which component runs the actual tool implementation?** The MCP server executes the tool handler and returns its result.
- **What is the role of each component in the call?** The model can propose a call. The host coordinates it. The MCP client sends the request. The MCP server executes the handler.
- **What is the difference between JSON-RPC and Streamable HTTP?** JSON-RPC structures the messages. Streamable HTTP is one way to carry them. An MCP client and server can also exchange messages over stdio.
- **Who calls a downstream API?** The server-side handler can call it as part of executing the tool. In the OCI example, the MCP server sends the request to the OCI Usage REST API.

### Q5. One agent, multiple MCP servers

See [Add MCP Server to your first Agent](#3-add-mcp-server-to-your-first-agent).

- **Why can one agent use tools from multiple servers?** `MultiServerMCPClient` manages independent connections to the configured servers and exposes their discovered tools through `get_tools()`.
- **Where does a tool call go after the lists are combined?** It goes to the server that exposed the selected tool. `get_order` goes to the Orders server, while `check_stock` goes to the Inventory server.
- **Do the servers have to share a process or tool names?** Each server can run independently and expose its own tools. The adapter combines the tool definitions for the agent.
- **Is `MultiServerMCPClient` part of the MCP specification?** It is a LangChain adapter. Each underlying client–server interaction uses MCP.
