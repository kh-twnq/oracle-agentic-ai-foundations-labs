# Bài tổng hợp về agent hỗ trợ khách hàng

Mô-đun 04 · Bài 07 · Oracle Student Guide, trang 157–161 · [Mục lục](README.md)

Hệ thống có một agent tiếp nhận yêu cầu và ba agent chuyên trách. Agent đơn hàng đọc trạng thái qua hàm ứng dụng. Agent hoàn tiền dùng tool nghiệp vụ trong bài lab. Agent FAQ dùng công cụ tìm kiếm. Guardrail đầu vào kiểm tra yêu cầu có thuộc phạm vi hỗ trợ hay không.

Với câu hỏi về mã đơn `ORD-001`, agent tiếp nhận chuyển yêu cầu đến chuyên gia trạng thái. Chuyên gia yêu cầu tool tra cứu. Runner cung cấp dữ liệu trả về để chuyên gia viết câu trả lời. Trace giúp thấy thời gian dành cho việc kiểm tra đầu vào, định tuyến, gọi công cụ và tạo kết quả.

**Thực hành.** Dùng dữ liệu giả để thử một mã đơn tồn tại, một mã không tồn tại và một yêu cầu lạc chủ đề. Kiểm tra agent đích, đối số dùng để tra và nội dung cuối. Với nhánh hoàn tiền, giữ quy tắc xét duyệt và chống gửi trùng trong tầng nghiệp vụ.

[Lab hỗ trợ khách hàng](https://github.com/oracle-university-labs/ou-generativeai-pro/blob/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/OpenAI/08_customer_support.py)

Trong workspace cục bộ, trace của lần chạy thử nằm ở `results/OpenAI-08_customer_support.log`.
