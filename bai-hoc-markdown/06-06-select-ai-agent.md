# Select AI Agent và quy trình trả hàng

Mô-đun 06 · Bài 06 · Oracle Student Guide, trang 229–234 · [Mục lục](README.md)

Select AI Agent điều phối agent trong Oracle AI Database. AI profile cung cấp cấu hình mô hình và ngữ cảnh cho tác vụ. Các API như `DBMS_CLOUD_AI_AGENT` định nghĩa agent, tool, task và team. Workflow phân tích yêu cầu, dùng tool, đánh giá kết quả rồi lưu ngữ cảnh cần cho các lượt sau.

Công cụ có thể dùng RAG để truy xuất tài liệu, NL2SQL để tra cứu đối tượng đã duyệt, PL/SQL để thực hiện nghiệp vụ hoặc REST để tích hợp dịch vụ ngoài. Thao tác trên dữ liệu chịu quyền và kiểm toán của cơ sở dữ liệu.

Trong bài trả hàng, tool đọc đơn, workflow kiểm tra điều kiện trong cửa sổ 30 ngày, rồi PL/SQL cập nhật trạng thái khi đạt yêu cầu. Agent chỉ nên xác nhận đã duyệt sau khi tool xác nhận cập nhật thành công. Một bước gửi thông báo cần có công cụ và bằng chứng thực thi riêng.

Trong workspace cục bộ, bài mô phỏng nằm ở `customer_return_local.py` và kết quả kiểm tra ở `results/customer-return-local.json`.
