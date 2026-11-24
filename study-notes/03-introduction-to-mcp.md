# Introduction to MCP

Student Guide · What You’ve Learned · trang 121 · [Mục lục](README.md)

- **Model Context Protocol (MCP)** chuẩn hóa kết nối giữa AI applications và tool servers. Ba primitives là **Tools**, **Resources** và **Prompts**. Tools là loại được dùng nhiều nhất trong các ví dụ.
- **Dynamic tool discovery** dùng `tools/list` để đọc tools lúc chạy. MCP server thực thi tool và trả kết quả qua client, còn application điều phối lượt chạy.
- **LLM** vẫn chọn tool và arguments như trong flow tool calling thông thường. MCP chuẩn hóa đường đi từ client đến server và tool.
- **MCP** phù hợp khi nhiều ứng dụng cần dùng lại external tools. Với hàm cục bộ đơn giản, gọi trực tiếp có thể đủ.

![MCP client liên lạc với MCP server, server chạy tool và trả kết quả.](images/03-mcp-tool-layer.png)
