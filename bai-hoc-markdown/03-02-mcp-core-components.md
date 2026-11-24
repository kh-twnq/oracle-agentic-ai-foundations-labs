# MCP Primitives, Connection Lifecycle và JSON-RPC

Mô-đun 03 · Bài 02 · Oracle Student Guide, trang 97–103 · [Mục lục](README.md)

MCP phân biệt **tools** để thực thi hành động, **resources** để ứng dụng đọc dữ liệu qua URI, và **prompts** để lấy mẫu tương tác tái sử dụng. Việc khám phá các mục này dựa vào năng lực server công bố.

1. Khi khởi tạo, client và server trao đổi phiên bản và capabilities. Client báo đã sẵn sàng bằng notification.
2. Client gọi `tools/list` để lấy tên, mô tả và schema đầu vào. Các phương thức khám phá khác phục vụ resources và prompts.
3. Client gọi `tools/call` với tên và arguments. Server thực thi và phản hồi bằng kết quả theo giao thức.
4. Client đóng kết nối khi hết phiên sử dụng.

Thông điệp dùng JSON-RPC 2.0. Yêu cầu cần phản hồi có `id` để ghép cặp với kết quả hoặc lỗi. Notification không mang `id`. Với stdio, host thường khởi chạy một tiến trình con và trao đổi qua stdin/stdout. Với Streamable HTTP, client kết nối tới endpoint HTTP và phản hồi có thể truyền theo luồng.

## JSON-RPC request và result

Trong MCP, model thường chọn **tool**, ứng dụng quyết định **resources** nào đưa vào context, còn **prompts** có thể được người dùng chọn từ giao diện host. Đây là cách phân vai trong bài, còn từng host có cách trình bày riêng.

Ở bước **discovery**, `tools/list` trả về `result.tools`; mỗi mục mang `name`, `description` và `inputSchema`. Với `tools/call`, client gửi `params.name` và `params.arguments`. Kết quả tool có thể chứa `content`, chẳng hạn một phần tử text. Phân biệt lỗi giao thức với trường hợp request hợp lệ nhưng nghiệp vụ từ chối xử lý.

Ví dụ dưới đây minh họa một request riêng sau khi phiên đã initialize.

```json
{
  "jsonrpc": "2.0",
  "id": 17,
  "method": "tools/call",
  "params": {
    "name": "multiply",
    "arguments": {"a": 9, "b": 7}
  }
}
```

Với **stdio**, giữ stdout cho protocol messages và gửi log kỹ thuật sang stderr. Với **Streamable HTTP**, endpoint hỗ trợ request qua HTTP và có thể trả theo luồng. Việc xác thực và quyền truy cập thuộc cấu hình triển khai.

**Tự kiểm tra.** Tìm trong trace bản mô tả đầu vào của một tool và thông điệp chứa đối số thực tế của lần gọi.
