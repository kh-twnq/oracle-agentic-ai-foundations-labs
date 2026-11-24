# API, công cụ và bộ nhớ của OCI agents

Mô-đun 05 · Bài 04 · Oracle Student Guide, trang 182–186 · [Mục lục](README.md)

OCI Responses API tiếp nhận yêu cầu theo dạng tương thích OpenAI và hỗ trợ gọi công cụ qua nhiều bước. Tài liệu mô tả **File Search** để truy xuất tài liệu, **Code Interpreter** để chạy Python trong môi trường cách ly, **function calling** cho hàm nghiệp vụ và **MCP calling** để kết nối server MCP.

- **Bộ nhớ phiên.** Responses API và Conversations API giữ ngữ cảnh giữa các lượt của một hội thoại.
- **Bộ nhớ dài hạn.** Có thể liên hệ thông tin qua nhiều phiên bằng định danh chủ thể trong một project. Cần tách chủ thể đúng để bộ nhớ phục vụ đúng người dùng.
- **Context compaction.** Cô đọng lịch sử dài để giảm số token và duy trì các chi tiết cần cho lượt tiếp theo.

Các API cấp thấp có thể dùng trực tiếp khi cần cấu hình chi tiết hơn. **Files** quản lý tệp, **Vector Stores** lập chỉ mục và truy xuất tài liệu, **Containers** cung cấp môi trường thực thi cách ly.

**Tự kiểm tra.** Phân loại thông tin người dùng vừa nhắc, sở thích cần nhớ giữa nhiều phiên và các đoạn tài liệu cần tìm theo ngữ nghĩa.
