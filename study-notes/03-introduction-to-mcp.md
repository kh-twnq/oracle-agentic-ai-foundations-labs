# Introduction to MCP

Module 3 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), pp. 91–121 · [Index](README.md)

## The MCP Integration Model

**Model Context Protocol (MCP)** defines a shared interface through which AI applications access tools, resources, and prompts. With `N` applications and `M` services, a separate adapter for every pair can require up to `N × M` integrations. A common protocol gives each application and service a shared integration point, represented by the `N + M` model. (pp. 91–96)

| Component | Responsibility |
| --- | --- |
| **Host** | Runs the AI application, coordinates model interactions, and creates MCP clients. |
| **MCP client** | Maintains the connection to one server and exchanges protocol messages. |
| **MCP server** | Publishes capabilities and executes the tools it provides. It can run locally or remotely. |

| Primitive | Purpose |
| --- | --- |
| **Tools** | Functions that perform actions. A model can select one based on its description and the task. |
| **Resources** | URI-addressed data that the host can read and add to context. |
| **Prompts** | Reusable templates that shape interactions. |

Tools let the host present a common tool interface to the model while server implementations vary. (pp. 97–98, 121)

![The MCP client sends a tool request to the server, which executes the implementation and returns the result.](images/03-mcp-tool-layer.png)

## Connection Lifecycle and JSON-RPC 2.0

1. **Initialize.** The client and server negotiate a protocol version and capabilities. The client then sends an initialized notification.
2. **Discover.** `tools/list` returns tool names, descriptions, and an `inputSchema` for each tool. Resources and prompts have corresponding discovery methods.
3. **Operate.** The host supplies available tool definitions to the model. When the model requests a tool, the client sends `tools/call` with a name and arguments, and the server returns its result.
4. **Shutdown.** The client closes the transport when the connection is no longer needed. (pp. 99–102)

**JSON-RPC 2.0** defines the message format. A request contains a `method` and optional `params`. Its `id` correlates it with a `result` or `error` response. Notifications omit the request ID. Tool responses can carry output in `content` for the host to return to the model. (pp. 100–102)

| Transport | Communication model |
| --- | --- |
| **stdio** | The host can launch a local server process and exchange messages through standard input and output. |
| **Streamable HTTP** | The client sends HTTP requests to a server endpoint. The server can stream responses through Server-Sent Events (SSE), and the service can require HTTP authentication. |

The same protocol message structure can travel through either transport. (p. 103)

## Tool Discovery and Agent Integration

`FastMCP` can expose registered functions with `@mcp.tool()`. In a LangChain host, `MultiServerMCPClient` manages MCP server connections, and `get_tools()` discovers tools and presents them in a form the agent can use. The server owns the tool implementation. The host coordinates the agent loop and returns the server's result to the model. (pp. 104–114)

A direct function call has lower integration overhead for simple local logic. MCP is useful when several applications share a tool, its implementation runs remotely, or another team owns it. (pp. 110–115, 121)

## MCP Transport and Downstream Services

An MCP connection and a server's downstream API connection are different boundaries. OCI Usage MCP Server can communicate with its local MCP client over stdio while using an OCI configuration profile to authenticate an HTTPS request to the OCI Usage REST API. The `get_summarized_usage` schema covers tenancy, time range, `granularity`, `group_by`, and `query_type`. The MCP client invokes the tool through the shared protocol, and the server owns the authenticated OCI request. (pp. 116–121)
