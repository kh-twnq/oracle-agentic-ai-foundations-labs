# Introduction to MCP

Module 3 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), trang 91–121 · [Mục lục](README.md)

Model Context Protocol (MCP) chuẩn hóa kết nối giữa AI applications và các hệ thống cung cấp tools, data và prompts. Guide bắt đầu với kiến trúc và vòng đời của kết nối, sau đó dùng cùng một protocol cho math tools cục bộ và báo cáo chi phí OCI. (trang 91–93)

## MCP Architecture và Core Primitives

Với custom integration cho từng cặp application và service, số adapter có thể tăng theo `N × M`. Protocol chung cho phép mỗi phía triển khai một integration tương thích, tương ứng với mô hình `N + M` trong slide. Mỗi **host** điều phối application và tạo một hoặc nhiều **MCP clients**. Mỗi client giữ kết nối với một **MCP server**. Server có thể chạy trên cùng máy hoặc từ xa. (trang 94–96)

| Primitive | Vai trò |
| --- | --- |
| **Tools** | Functions để thực hiện hành động. Model thường chọn tool dựa trên nhiệm vụ và description. |
| **Resources** | Dữ liệu có địa chỉ URI mà application có thể đọc để đưa vào context. |
| **Prompts** | Templates tái sử dụng để định hình interaction, chẳng hạn mẫu review hoặc tóm tắt. |

Tools là primitive được dùng nhiều nhất trong các ví dụ của Guide. Host quản lý interaction, còn server công bố capabilities và thực thi các tool mà nó cung cấp. (trang 97–98)

![MCP client gửi tool request đến MCP server, server chạy implementation và trả kết quả.](images/03-mcp-tool-layer.png)

## Connection Lifecycle, JSON-RPC 2.0 và transports

1. **Initialize.** Client và server trao đổi protocol version cùng capabilities. Client gửi notification `initialized` sau khi bắt tay.
2. **Discover.** Client dùng `tools/list` để lấy tool names, descriptions và `inputSchema`. Resources và prompts có các phương thức discovery tương ứng.
3. **Operate.** Khi model chọn một tool, client gửi `tools/call` cùng `name` và `arguments`. Server chạy tool và gửi result về client.
4. **Shutdown.** Client đóng transport khi hoàn thành phiên làm việc. (trang 99–102)

**JSON-RPC 2.0** dùng `method` và `params` trong request. `id` ghép request với response tương ứng, còn response mang `result` hoặc `error`. Notification không có request ID. Ví dụ với math server, result của một phép nhân có thể được trả trong `content` rồi đưa vào context của model. (trang 100–102)

| Transport | Cách giao tiếp |
| --- | --- |
| **stdio** | Host khởi chạy server như child process. Hai phía trao đổi protocol messages qua stdin và stdout trên cùng máy. |
| **Streamable HTTP** | Client gửi HTTP requests đến service endpoint. Server có thể truyền response qua SSE. Transport này phù hợp với remote services và có thể dùng HTTP authentication. |

Protocol message giữ cùng cấu trúc khi thay transport. (trang 103)

## Add MCP to a LangChain agent

Bài lab đưa `add`, `multiply`, `divide` và `square_root` sang Python process riêng. Server dùng `FastMCP`, đăng ký functions bằng `@mcp.tool()` và chạy với `stdio`. Phía LangChain khai báo lệnh khởi chạy và đường dẫn server trong `MultiServerMCPClient`. Client gọi `get_tools()` để discovery, adapter chuyển tools sang dạng dùng được với `create_agent()`, rồi agent chạy theo flow bất đồng bộ. (trang 104–109)

Khi model chọn tool, application vẫn điều phối ReAct loop. Client chuyển lời gọi qua MCP, server thực thi function, và tool result quay về model. Tool registration, schema, execution và implementation của các MCP tools nằm phía server. Từ góc nhìn model, các thông tin cần để reasoning vẫn là tool definitions và tool results. MCP có ích khi nhiều applications cần dùng chung tools hoặc dùng tools do nhóm khác cung cấp. Gọi Python function trực tiếp là cách đơn giản cho math tools cục bộ. (trang 110–115)

## Real-world walkthrough với OCI Usage MCP Server

OCI Usage MCP Server đóng gói OCI Usage REST API, cùng nguồn dữ liệu dùng trong Cost Analysis. Guide chạy package `oracle.oci-usage-mcp-server` bằng `uvx`. Client giao tiếp với process server qua stdio. Server dùng OCI configuration profile để xác thực và gửi request đến OCI qua HTTPS. Hai kết nối này giải thích vì sao MCP transport là local stdio dù dữ liệu đến từ cloud. (trang 116–120)

`get_summarized_usage` nhận tenancy ID, thời gian bắt đầu và kết thúc, `granularity`, `group_by` và `query_type`. Client trực tiếp có thể đọc schema và chạy tool để kiểm tra dữ liệu. Agent có thể chuyển câu hỏi ngôn ngữ tự nhiên thành arguments rồi tóm tắt report. Khi đối chiếu với Cost Analysis, dùng cùng khoảng ngày, granularity và bộ lọc. (trang 119–121) [Hướng dẫn chạy lab và kết quả mẫu](../labs/README.md)
