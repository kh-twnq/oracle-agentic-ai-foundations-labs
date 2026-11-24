# Kết nối agent đầu tiên với MCP server

Mô-đun 03 · Bài 03 · Oracle Student Guide, trang 104–115 · [Mục lục](README.md)

Bài lab chuyển các phép toán từ file agent sang một tiến trình riêng. Server tạo bằng `FastMCP` công bố các hàm cộng, nhân, chia và căn bậc hai. Client LangChain dùng `MultiServerMCPClient` với cấu hình lệnh Python, đường dẫn script và transport `stdio`.

Client chạy bất đồng bộ để khám phá bằng `await client.get_tools()`. Các tool được adapter chuyển sang dạng LangChain hiểu, rồi truyền vào `create_agent`. Khi mô hình chọn một tool, client chuyển lời gọi cho server và đưa kết quả vào vòng lặp. Từ góc nhìn của mô hình, đầu vào vẫn là schema và đầu ra vẫn là kết quả tool.

Việc tách server làm tăng một lớp giao tiếp và thêm lỗi tiến trình cần xử lý. Lợi ích rõ hơn khi nhiều ứng dụng chia sẻ công cụ, công cụ cần được nâng cấp độc lập hoặc năng lực được cung cấp bởi một dịch vụ khác.

## Phần server và phần host

Trong server `FastMCP`, `@mcp.tool()` biến một hàm có type hints và docstring thành tool có thể được khám phá. Entry point dùng `mcp.run(transport="stdio")`. Client lấy đường dẫn server tương đối với script client, khởi chạy tiến trình và lấy tools từ adapter trước khi gọi agent bất đồng bộ.

| Điểm so sánh | Local tool | MCP-backed tool |
| --- | --- | --- |
| Công bố schema | Framework đọc metadata của hàm nội bộ. | Server mô tả tool qua `tools/list`. |
| Thực thi | Runtime gọi Python function trực tiếp. | Client gửi `tools/call`, server chạy implementation. |
| Bảo trì | Agent app phụ trách implementation. | Server có thể được nâng cấp riêng, client giữ protocol tương thích. |

Một phép tính cục bộ có lợi cho việc học vì dễ quan sát chặng kết nối. Mô hình MCP có giá trị thực tế hơn với tools được nhiều ứng dụng dùng chung hoặc do một nhóm khác cung cấp.

**Thực hành.** Xem danh sách bốn tool, gọi một bài toán hai bước rồi kiểm tra trường hợp thiếu đối số. Phân biệt lỗi schema, lỗi phép tính và lỗi kết nối.

[Server toán học](https://github.com/oracle-university-labs/ou-generativeai-pro/blob/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/MCP/mcp_math_server.py) · [Client LangChain](https://github.com/oracle-university-labs/ou-generativeai-pro/blob/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/MCP/first_agent_with_mcp.py)
