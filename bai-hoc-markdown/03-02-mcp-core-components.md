# Công cụ, tài nguyên và vòng đời kết nối MCP

Mô-đun 03 · Bài 02 · Oracle Student Guide, trang 97–103 · [Mục lục](README.md)

MCP phân biệt **tools** để thực thi hành động, **resources** để ứng dụng đọc dữ liệu qua URI, và **prompts** để lấy mẫu tương tác tái sử dụng. Việc khám phá các mục này dựa vào năng lực server công bố.

1. Khi khởi tạo, client và server trao đổi phiên bản và capabilities. Client báo đã sẵn sàng bằng notification.
2. Client gọi `tools/list` để lấy tên, mô tả và schema đầu vào. Các phương thức khám phá khác phục vụ resources và prompts.
3. Client gọi `tools/call` với tên và arguments. Server thực thi và phản hồi bằng kết quả theo giao thức.
4. Client đóng kết nối khi hết phiên sử dụng.

Thông điệp dùng JSON-RPC 2.0. Yêu cầu cần phản hồi có `id` để ghép cặp với kết quả hoặc lỗi. Notification không mang `id`. Với stdio, host thường khởi chạy một tiến trình con và trao đổi qua stdin/stdout. Với Streamable HTTP, client kết nối tới endpoint HTTP và phản hồi có thể truyền theo luồng.

**Tự kiểm tra.** Tìm trong trace bản mô tả đầu vào của một tool và thông điệp chứa đối số thực tế của lần gọi.
