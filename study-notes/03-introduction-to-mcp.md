# Introduction to MCP

*Giới thiệu về MCP*

Module 3 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), tr. 91–121 · [Mục lục](README.md)

## Agenda

*Nội dung học*

1. [Model Context Protocol là gì?](#1-what-is-model-context-protocol)
2. [Các thành phần cốt lõi của MCP](#2-mcp-core-components)
3. [Thêm MCP server vào agent đầu tiên](#3-add-mcp-server-to-your-first-agent)
4. [Ví dụ MCP trong thực tế](#4-real-world-mcp-walkthrough)

Nội dung theo chương trình học ở tr. 92 của Student Guide.

[Ôn tập module](#module-review) bao gồm các biến thể của cả năm câu hỏi kiểm tra.

<a name="1-what-is-model-context-protocol"></a>

## 1. Model Context Protocol là gì?

**Model Context Protocol (MCP) là một chuẩn mở để kết nối ứng dụng AI với các tool, nguồn dữ liệu và hệ thống bên ngoài.** Với tool, **MCP chuẩn hóa cách client tìm hiểu server cung cấp những gì và gọi một tool cụ thể**. Một host viết bằng Java có thể gọi MCP server viết bằng Python qua cùng giao thức.

Host vẫn điều phối vòng lặp của agent. Khi xử lý lời gọi tool, server có thể gọi một REST API hiện có, như trong ví dụ OCI bên dưới.

Anthropic giới thiệu MCP vào tháng 11 năm 2024. Dự án thuộc Agentic AI Foundation của Linux Foundation. (tr. 93–94)

### The integration problem

*Bài toán tích hợp*

| Mô hình tích hợp | Số lượng cần triển khai cho N ứng dụng và M dịch vụ | 3 ứng dụng và 4 dịch vụ |
| --- | --- | --- |
| Kết nối theo từng cặp | Tối đa `N × M` adapter, mỗi cặp ứng dụng và dịch vụ dùng một adapter. | 12 adapter |
| Dùng chung giao thức MCP | `N + M` tích hợp giao thức, mỗi ứng dụng hoặc dịch vụ tích hợp một lần. | 7 tích hợp |

**`N + M` là số phần triển khai giao thức.** Host vẫn cần một kết nối client cho mỗi server mà nó sử dụng. (tr. 95–96)

<a name="2-mcp-core-components"></a>

## 2. Các thành phần cốt lõi của MCP

| Vai trò | Trách nhiệm |
| --- | --- |
| **Host** | Chạy ứng dụng AI, điều phối mô hình và quản lý các MCP client. |
| **MCP client** | Trao đổi thông điệp theo giao thức với một server. |
| **MCP server** | Công bố các khả năng được hỗ trợ, **thực thi những tool do nó cung cấp** và trả kết quả. |

| Khả năng của server | Khám phá và sử dụng | Ví dụ |
| --- | --- | --- |
| **Tools** | `tools/list` và `tools/call`. Mô hình có thể đề xuất một lời gọi, còn host quản lý việc thực thi. | `get_order` tra cứu một đơn hàng. |
| **Resources** | `resources/list` và `resources/read`. Ứng dụng chọn dữ liệu theo URI để đưa vào ngữ cảnh. | Văn bản chính sách trả hàng. |
| **Prompts** | `prompts/list` và `prompts/get`. **Người dùng có thể chọn một mẫu tương tác dùng lại** từ giao diện rồi điền tham số. | Mẫu soạn câu trả lời cho yêu cầu trả hàng. |

Server khai báo các khả năng nó hỗ trợ. Host chọn cách đưa chúng vào ứng dụng. (tr. 96–98) [Kiến trúc MCP](https://modelcontextprotocol.io/docs/learn/architecture)

<a name="connection-lifecycle"></a>

### Vòng đời kết nối

Các bước sau dùng phiên bản MCP `2025-11-25` để minh họa luồng mà lab sử dụng.

1. **Khởi tạo.** Client dùng `initialize` để thỏa thuận phiên bản giao thức và trao đổi thông tin về các khả năng được hỗ trợ với server. Sau đó client gửi thông báo `notifications/initialized`.
2. **Khám phá.** **`tools/list` trả về tên, mô tả và định nghĩa `inputSchema` của các tool.** Resource và prompt có phương thức khám phá riêng.
3. **Vận hành.** **Client dùng `tools/call` để gọi một tool cụ thể theo tên và truyền các đối số.** Server chạy tool rồi trả kết quả.
4. **Kết thúc.** Client đóng kết nối. (tr. 99–102)

Nếu server hỗ trợ đăng ký theo dõi, client có thể dùng `resources/subscribe` để nhận cập nhật của một resource. Khi resource đó thay đổi, server có thể gửi `notifications/resources/updated`.

<a name="tool-input-schema"></a>

### Schema đầu vào của tool

**`inputSchema` là JSON Schema của các đối số mà tool nhận.** Nó mô tả cấu trúc dự kiến, kiểu dữ liệu của các trường, trường bắt buộc và các ràng buộc đã khai báo. Client có thể dùng schema này để tạo yêu cầu gọi tool hợp lệ.

Ví dụ, `get_order` có thể khai báo rằng `order_id` là một chuỗi bắt buộc.

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

Sau đó client gửi các giá trị thực tế trong trường `arguments` của tham số `tools/call`.

```json
{
  "name": "get_order",
  "arguments": {
    "order_id": "ORD-42"
  }
}
```

Cấu hình kết nối xác định cơ chế truyền tải và xác thực. Cách triển khai xác định nơi server chạy.

### Messages and transports

*Thông điệp và cơ chế truyền tải*

MCP dùng **JSON-RPC 2.0** để định dạng thông điệp. Một yêu cầu có `method` và có thể có `params`. ID yêu cầu dùng để ghép yêu cầu với phản hồi kết quả hoặc lỗi. Thông báo không có ID. Kết quả tool có thể chứa trường `content`. (tr. 100–102)

| Cơ chế truyền tải | Kênh giao tiếp |
| --- | --- |
| **stdio** | Client khởi chạy server dưới dạng tiến trình con. Mỗi dòng trên `stdin` và `stdout` chứa một thông điệp JSON-RPC. Server ghi log vào `stderr`. |
| **Streamable HTTP** | Client dùng HTTP POST để gửi thông điệp tới endpoint MCP. Server có thể trả JSON hoặc luồng Server-Sent Events (SSE) cho một yêu cầu. Endpoint có thể hỗ trợ GET để mở luồng SSE riêng. |

Ví dụ, sau khi kết nối đã khởi tạo, client gửi một yêu cầu và nhận phản hồi có cùng `id`.

```json
{"jsonrpc":"2.0","id":7,"method":"tools/call","params":{"name":"get_order","arguments":{"order_id":"ORD-42"}}}
```

```json
{"jsonrpc":"2.0","id":7,"result":{"content":[{"type":"text","text":"Delivered"}]}}
```

Phản hồi lỗi ở cấp giao thức dùng `error` thay cho `result`. Lỗi phát sinh trong quá trình chạy tool có thể nằm trong `result` với `isError: true` để agent xử lý. **JSON-RPC định nghĩa thông điệp. stdio và Streamable HTTP chuyển thông điệp.** (tr. 103) [Đặc tả vòng đời](https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle) · [Tool](https://modelcontextprotocol.io/specification/2025-11-25/server/tools) · [Transport](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)

<a name="3-add-mcp-server-to-your-first-agent"></a>

## 3. Thêm MCP server vào agent đầu tiên

Chuyển một tool cục bộ sang MCP làm thay đổi nơi chạy hàm xử lý của tool. Mô hình có thể đề xuất một lời gọi tool. Host điều phối vòng lặp của agent và MCP client gửi yêu cầu. **MCP server chạy hàm xử lý của tool rồi trả kết quả.** (tr. 104–115)

![MCP client gửi yêu cầu. Server thực thi tool rồi trả kết quả.](images/03-mcp-tool-layer.png)

`FastMCP` có thể cung cấp các hàm đã đăng ký bằng `@mcp.tool()`. **`MultiServerMCPClient` quản lý các kết nối độc lập tới những server đã cấu hình. Phương thức `get_tools()` gộp các tool tìm được thành một danh sách để agent LangChain sử dụng.**

**Khi các MCP server công bố tool trùng tên, host hoặc client phân biệt bằng server nguồn.** Ví dụ, nếu Orders và Inventory đều có `lookup`, host có thể hiển thị `orders_lookup` và `inventory_lookup`, rồi chuyển lời gọi cho đúng kết nối với tên gốc `lookup`. [Định tuyến nhiều MCP server trong LangChain](https://docs.langchain.com/oss/python/langchain/mcp/connections)

Gọi trực tiếp phù hợp với logic cục bộ đơn giản. Giao diện MCP hữu ích khi nhiều ứng dụng dùng chung tool hoặc khi phần triển khai do một dịch vụ khác quản lý. (tr. 107–115, 121)

### Tích hợp server toán học vào LangChain

Trong lab, `mcp_math_server.py` công bố bốn tool toán học. **`mcp.run(transport="stdio")` khởi chạy server và trao đổi thông điệp qua `stdin` và `stdout`.** `first_agent_with_mcp.py` cấu hình server `math` qua `stdio`, gọi `await client.get_tools()`, truyền danh sách vào `create_agent(model, tools)` rồi gọi `await agent.ainvoke(...)`. Khi mô hình chọn một tool, adapter chuyển yêu cầu sang `tools/call` và đưa kết quả trở lại vòng lặp agent. [Mã lab MCP](https://github.com/oracle-university-labs/ou-generativeai-pro/tree/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/MCP)

Chạy [fixture cục bộ](../labs/README.md#reproduce-the-local-runs) để so sánh hai bước. Kết quả khám phá phải có `add`, `multiply`, `divide` và `square_root`. Yêu cầu tính 15 nhân 8 rồi chia 3 phải dùng kết quả 120 làm đầu vào cho phép chia và cho ra 40. [Kết quả khám phá và gọi tool](../labs/sample-results/mcp-math.json)

<a name="4-real-world-mcp-walkthrough"></a>

## 4. Ví dụ MCP trong thực tế

Server có thể nhận yêu cầu MCP qua một cơ chế truyền tải và gọi dịch vụ phía sau qua cơ chế khác. OCI Usage MCP Server minh họa ranh giới này. (tr. 116–120)

**MCP client → stdio → OCI Usage MCP Server → HTTPS → OCI Usage REST API**

MCP server dùng một hồ sơ cấu hình OCI để xác thực yêu cầu gửi tới dịch vụ phía sau. `get_summarized_usage` nhận tenancy, khoảng thời gian, `granularity`, `group_by` và `query_type`. Các trường này thuộc về tool của OCI. Client khám phá và gọi tool qua cùng giao diện MCP dùng cho các tool khác. (tr. 118–121)

<a name="module-review"></a>

## Ôn tập module

### Q1. MCP as a standardized tool execution layer

*Câu 1. MCP là lớp chuẩn hóa cách gọi và thực thi tool*

Xem [Model Context Protocol là gì?](#1-what-is-model-context-protocol).

- **Vì sao MCP được gọi là lớp chuẩn hóa cách gọi và thực thi tool?** MCP cung cấp cho các ứng dụng AI một cách chung để khám phá và gọi tool do các server bên ngoài cung cấp.
- **`N + M` đếm những gì?** Đó là số tích hợp với giao thức chung. Mỗi ứng dụng trong N ứng dụng triển khai phía client. Mỗi dịch vụ trong M dịch vụ triển khai phía server. Khi chạy, host vẫn kết nối tới những server mà nó sử dụng.
- **Ứng dụng Java có thể gọi một MCP tool viết bằng Python không?** Có. Client Java và server Python giao tiếp qua cùng giao thức. Server Python thực thi hàm xử lý tool của nó.
- **REST và MCP có thể xuất hiện trong cùng một workflow như thế nào?** Client của agent dùng MCP để gọi tool. Hàm xử lý tool có thể dùng REST để gọi một dịch vụ hiện có.
- **Vòng lặp của agent thay đổi thế nào sau khi thêm MCP?** Host vẫn điều phối mô hình, các lời gọi tool và kết quả. MCP cung cấp giao diện để gọi các server tool bên ngoài.

### Q2. Tool discovery and invocation

*Câu 2. Khám phá và gọi tool*

Xem [Vòng đời kết nối](#connection-lifecycle).

- **`tools/call` làm gì?** Nó yêu cầu thực thi một tool theo tên và truyền đối số cho lần gọi đó.
- **Phương thức nào cho biết có những tool và đối số nào?** `tools/list` trả về các định nghĩa tool, bao gồm `inputSchema` của chúng.
- **Khi nào phiên bản giao thức được thỏa thuận?** Trong bước `initialize`, trước khi bắt đầu khám phá hoặc gọi tool.
- **Client làm sao biết một resource đã thay đổi?** Nếu server hỗ trợ đăng ký theo dõi, client có thể dùng `resources/subscribe` và nhận `notifications/resources/updated` khi resource thay đổi.

### Q3. Understanding `inputSchema`

*Câu 3. Hiểu `inputSchema`*

Xem [Schema đầu vào của tool](#tool-input-schema).

- **`inputSchema` mô tả điều gì?** Cấu trúc và kiểu dữ liệu dự kiến của các đối số, gồm các trường bắt buộc và những ràng buộc khác đã khai báo.
- **Làm sao biết `order_id` có bắt buộc hay không?** Kiểm tra trường này có xuất hiện trong `required` hay không. Khai báo nó là chuỗi trong `properties` xác định kiểu dữ liệu của nó.
- **`inputSchema` và `arguments` khác nhau thế nào?** Schema định nghĩa đầu vào dự kiến. `arguments` chứa các giá trị thực tế của một lần gọi cụ thể, chẳng hạn `{"order_id":"ORD-42"}`.
- **Xác thực, cơ chế truyền tải và vị trí của tool được xác định ở đâu?** Cấu hình kết nối xác định xác thực và cơ chế truyền tải. Cách triển khai xác định vị trí của tool.

### Q4. Who does what in a tool call?

*Câu 4. Mỗi thành phần làm gì khi gọi tool?*

Xem [Các thành phần cốt lõi của MCP](#2-mcp-core-components) và [Thêm MCP server vào agent đầu tiên](#3-add-mcp-server-to-your-first-agent).

- **Thành phần nào chạy phần triển khai thực tế của tool?** MCP server thực thi hàm xử lý tool và trả kết quả.
- **Từng thành phần có vai trò gì trong lời gọi?** Mô hình có thể đề xuất lời gọi. Host điều phối. MCP client gửi yêu cầu. MCP server thực thi hàm xử lý.
- **JSON-RPC và Streamable HTTP khác nhau thế nào?** JSON-RPC định dạng thông điệp. Streamable HTTP là một cách truyền các thông điệp đó. MCP client và server cũng có thể trao đổi thông điệp qua stdio.
- **Thành phần nào gọi API của dịch vụ phía sau?** Hàm xử lý ở phía server có thể gọi API đó khi chạy tool. Trong ví dụ OCI, MCP server gửi yêu cầu tới OCI Usage REST API.

### Q5. One agent, multiple MCP servers

*Câu 5. Một agent dùng nhiều MCP server*

Xem [Thêm MCP server vào agent đầu tiên](#3-add-mcp-server-to-your-first-agent).

- **Vì sao một agent có thể dùng tool từ nhiều server?** `MultiServerMCPClient` quản lý các kết nối độc lập tới những server đã cấu hình và cung cấp các tool tìm được qua `get_tools()`.
- **Sau khi gộp các danh sách, lời gọi tool được gửi đi đâu?** Lời gọi được chuyển đến server đã công bố tool được chọn. `get_order` được gửi đến server Orders, còn `check_stock` được gửi đến server Inventory.
- **Các server có phải dùng chung tiến trình hoặc tên tool không?** Mỗi server có thể chạy độc lập và cung cấp các tool riêng. Adapter gộp các định nghĩa tool cho agent sử dụng.
- **`MultiServerMCPClient` có thuộc đặc tả MCP không?** Đây là một adapter của LangChain. Mỗi tương tác giữa client và server bên dưới vẫn dùng MCP.
