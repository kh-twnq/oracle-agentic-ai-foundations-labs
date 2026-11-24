# Introduction to MCP

Student Guide · What You’ve Learned · trang 121 · [Mục lục](README.md)

1. **MCP** dùng một protocol chung để kết nối agent với tool server. Slide ví kết nối này như USB cho AI tools.
2. **Core Primitives** gồm Tools, Resources và Prompts. Tools là primitive được dùng phổ biến nhất.
3. **Standardized Tool Layer.** MCP đưa tool call qua đường `client → server → tool` theo protocol chuẩn. Các thao tác vốn được gọi qua local function có thể được cung cấp từ server.
4. **Dynamic Tool Discovery.** Agent dùng `tools/list` để khám phá tools lúc chạy. Với local tools trong ví dụ, application đăng ký hàm trước bằng `@tool`.
5. **Server-Side Execution.** MCP server chạy tool và trả kết quả. Application điều phối lượt chạy.
6. **LLM behavior.** Model dùng cùng cơ chế reasoning và chọn tool khi kết nối qua MCP.
7. **Phạm vi sử dụng.** MCP hữu ích với external services cần tái sử dụng. Gọi hàm trực tiếp có thể đủ cho tool đơn giản chạy cục bộ.

![MCP client liên lạc với MCP server, server chạy tool và trả kết quả.](images/03-mcp-tool-layer.png)
