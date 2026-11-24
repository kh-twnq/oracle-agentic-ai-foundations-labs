# Hai cách xây dựng với OCI Enterprise AI Agents

Mô-đun 05 · Bài 03 · Oracle Student Guide, trang 178–181 · [Mục lục](README.md)

Với **OCI Responses API**, ứng dụng tiếp tục chạy ở môi trường hiện có và gọi điểm cuối OCI. Dịch vụ quản lý suy luận của mô hình, phiên và các công cụ được hỗ trợ. Cách này dùng cú pháp tương thích OpenAI với endpoint và xác thực của OCI.

Với **Hosted Agentic Apps**, bạn đóng gói ứng dụng và phần điều phối của mình vào container. OCI cung cấp HTTP endpoint và quản lý hạ tầng thực thi, gồm mạng, lưu trữ và scaling theo cấu hình. Cách này phục vụ agent đã có logic hoặc framework riêng.

Trong cả hai cách, nhóm phát triển vẫn xác định chỉ dẫn, tool được phép gọi, nguồn tri thức và kết quả nghiệp vụ. Nhà cung cấp runtime xử lý phần hạ tầng tương ứng. OCI Logging, Monitoring và Audit phục vụ theo dõi và kiểm toán theo cấu hình triển khai.

**Tự kiểm tra.** Xác định lựa chọn cho một ứng dụng web đã có máy chủ riêng và cho một agent LangGraph cần triển khai độc lập qua HTTP.
