# Introduction to MCP

Module 3 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), pp. 91–121 · [Index](README.md)

## Agenda

1. [What is Model Context Protocol?](#1-what-is-model-context-protocol)
2. [MCP Core Components](#2-mcp-core-components)
3. [Add MCP Server to your first Agent](#3-add-mcp-server-to-your-first-agent)
4. [Real World MCP Walkthrough](#4-real-world-mcp-walkthrough)

Student Guide agenda, p. 92.

## 1. What is Model Context Protocol?

**Model Context Protocol (MCP) is an open standard that connects AI applications to external tools, data sources, and systems.** It lets a compatible client communicate with a compatible server through a shared interface. Anthropic introduced MCP in November 2024. The project is part of the Linux Foundation's Agentic AI Foundation. (pp. 93–94)

### The integration problem

| Integration model | Cost for N applications and M services | 3 applications and 4 services |
| --- | --- | --- |
| Pairwise connectors | Up to `N × M` adapters, one per pair. | 12 adapters |
| Shared MCP protocol | `N + M` protocol integrations, one per application or service. | 7 integrations |

The count describes integration implementations. A host may still maintain a separate runtime connection to each server it uses. (pp. 95–96)

## 2. MCP Core Components

| Role | Responsibility |
| --- | --- |
| **Host** | Runs the AI application, coordinates the model, and creates MCP clients. |
| **MCP client** | Maintains a connection with one server and exchanges protocol messages. |
| **MCP server** | Publishes capabilities and executes the tools it provides. |

A server can expose **Tools** for actions, **Resources** for URI-addressed data, and **Prompts** for reusable templates. The host decides how to present available capabilities to the model and the user. (pp. 96–98)

### Connection lifecycle

1. **Initialize.** Client and server negotiate a version and capabilities. The client then sends an initialized notification.
2. **Discover.** `tools/list` returns names, descriptions, and `inputSchema`. Resources and prompts have their own discovery methods.
3. **Operate.** `tools/call` sends a name and arguments. The server runs the tool and returns the result.
4. **Shutdown.** The client closes the connection. (pp. 99–102)

MCP uses **JSON-RPC 2.0** for structured messages. A request has a `method` and optional `params`. An `id` matches a request with its `result` or `error`. A notification omits the request ID. Tool results can include a `content` field. (pp. 100–102)

| Transport | Communication channel |
| --- | --- |
| **stdio** | A local process exchanges messages with the client through standard input and output. |
| **Streamable HTTP** | A client sends HTTP requests to an endpoint. Responses can use Server-Sent Events (SSE), and the service can require HTTP authentication. |

The transport carries the JSON-RPC messages. Tool discovery and invocation have the same roles on either transport. (p. 103)

## 3. Add MCP Server to your first Agent

Moving a local tool to MCP changes the execution boundary. The model still sees a tool definition. The host still owns the agent loop. The MCP client sends the call to a server, which owns the implementation and returns the result. (pp. 104–115)

![The MCP client sends the request. The server executes the tool and returns the result.](images/03-mcp-tool-layer.png)

`FastMCP` can publish functions registered with `@mcp.tool()`. `MultiServerMCPClient` connects a LangChain host to servers, and `get_tools()` exposes discovered tools in a form the agent can use. Direct calls suit simple local logic. A protocol boundary helps when tools are shared across applications or owned by a different service. (pp. 107–115, 121)

## 4. Real World MCP Walkthrough

A server can receive an MCP request through one transport and call a downstream service through another. OCI Usage MCP Server illustrates this boundary. (pp. 116–120)

**MCP client → stdio → OCI Usage MCP Server → HTTPS → OCI Usage REST API**

The MCP server uses an OCI configuration profile to authenticate the downstream request. `get_summarized_usage` accepts a tenancy, time range, `granularity`, `group_by`, and `query_type`. These fields belong to the OCI tool. The client can discover and call it through the same MCP interface used for other tools. (pp. 118–121)
