# Xây agent bằng Private Agent Factory

Mô-đun 06 · Bài 05 · Oracle Student Guide, trang 223–228 · [Mục lục](README.md)

Private Agent Factory là công cụ trực quan để kết nối mô hình, nguồn dữ liệu và luồng agent. Tài liệu mô tả kiến trúc triển khai bằng container, kết nối Oracle AI Database và một nhà cung cấp mô hình đã cấu hình.

- **Knowledge Agent** phục vụ hỏi đáp trên tài liệu được duyệt. Nội dung có thể đến từ tệp, website hoặc kho lưu trữ. Vector Search tìm đoạn liên quan và câu trả lời có thể kèm liên kết nguồn.
- **Data Analysis Agent** phục vụ dữ liệu có cấu trúc. Nó chuyển câu hỏi thành SQL dựa trên các bảng hoặc view có thể truy cập và có thể hiển thị biểu đồ.
- **Agent Builder** dùng các nút trực quan để phối hợp bước gọi mô hình, tool, nhánh điều kiện và agent chuyên trách. Các bước mở rộng có thể gồm thành phần Python và công cụ MCP.

**Tự kiểm tra.** Phân loại hai yêu cầu đọc quy trình nghỉ phép và tính tổng số ngày nghỉ theo tháng. Xác định tài liệu hoặc bảng nào cần cấp quyền cho từng yêu cầu.
