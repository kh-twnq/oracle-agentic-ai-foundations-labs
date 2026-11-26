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
