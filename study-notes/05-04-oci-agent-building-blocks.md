# OCI Agent Building Blocks

Mô-đun 05 · Bài 04 · Oracle Student Guide, trang 182–186 · [Mục lục](README.md)

OCI Responses API tiếp nhận yêu cầu theo dạng tương thích OpenAI và hỗ trợ gọi tool qua nhiều bước. Tài liệu mô tả **File Search** để truy xuất tài liệu, **Code Interpreter** để chạy Python trong môi trường cách ly, **function calling** cho hàm nghiệp vụ và **MCP calling** để kết nối server MCP.

- **Short-term memory.** Responses API và Conversations API giữ ngữ cảnh giữa các lượt của một hội thoại.
- **Long-term memory.** Có thể liên hệ thông tin qua nhiều phiên bằng định danh chủ thể trong một project. Cần tách chủ thể đúng để bộ nhớ phục vụ đúng người dùng.
- **Context compaction.** Cô đọng lịch sử dài để giảm số token và duy trì các chi tiết cần cho lượt tiếp theo.

Các API cấp thấp có thể dùng trực tiếp khi cần cấu hình chi tiết hơn. **Files** quản lý tệp, **Vector Stores** lập chỉ mục và truy xuất tài liệu, **Containers** cung cấp môi trường thực thi cách ly.

## Chọn đúng API cho dữ liệu và execution

Guide đề cập **multi-model routing**, lưu state và **context compaction** trong nhóm OCI Responses API. Context compaction giúp giảm phần hội thoại cần đưa vào request khi lịch sử dài. Với long-term memory, `subject_id` trong project liên kết dữ liệu đến đúng subject. Kiểm tra chính sách memory trước khi lưu nội dung nhạy cảm hoặc đưa nội dung sang phiên khác.

**File Search** thường cần file đã nạp và vector store để truy xuất semantic matches. **Files API** xử lý vòng đời file. **Vector Stores API** phục vụ chunking, embeddings, semantic retrieval và metadata filtering. **Containers API** dành cho xử lý hoặc tool execution cần runtime cách ly. **Function calling** nối vào business logic, còn **MCP calling** nối vào tool được công bố theo protocol.

Ví dụ, với trợ lý tài liệu, dữ liệu lâu dài nằm trong file và vector store. Lịch sử hỏi đáp nằm trong conversation. Một tác vụ phân tích dữ liệu có thể tạo file kết quả trong môi trường chạy code, tùy cấu hình và phạm vi quyền.

**Tự kiểm tra.** Phân loại thông tin người dùng vừa nhắc, sở thích cần nhớ giữa nhiều phiên và các đoạn tài liệu cần tìm theo ngữ nghĩa.
