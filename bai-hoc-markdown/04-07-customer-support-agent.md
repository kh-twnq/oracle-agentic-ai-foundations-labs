# Bài tổng hợp về agent hỗ trợ khách hàng

Mô-đun 04 · Bài 07 · Oracle Student Guide, trang 157–161 · [Mục lục](README.md)

Hệ thống có một agent tiếp nhận yêu cầu và ba agent chuyên trách. Agent đơn hàng đọc trạng thái qua hàm ứng dụng. Agent hoàn tiền dùng tool nghiệp vụ trong bài lab. Agent FAQ dùng công cụ tìm kiếm. Input guardrail kiểm tra yêu cầu có thuộc phạm vi hỗ trợ hay không.

Với câu hỏi về mã đơn `ORD-001`, agent tiếp nhận chuyển yêu cầu đến chuyên gia trạng thái. Chuyên gia yêu cầu tool tra cứu. Runner cung cấp dữ liệu trả về để chuyên gia viết câu trả lời. Trace giúp thấy thời gian dành cho việc kiểm tra đầu vào, định tuyến, gọi tool và tạo kết quả.

## Đọc trace của yêu cầu tra đơn hàng

| Pha | Dữ liệu và quyết định cần kiểm tra |
| --- | --- |
| Input guardrail | Câu hỏi về đơn hàng thuộc phạm vi support. |
| Triage | Nhận mã `ORD-001` và handoff đến Order Status Agent. |
| Tool call | Chuyên gia gửi mã đơn tới `lookup_order` và nhận dữ liệu trong fixture. |
| Final output | Chuyên gia diễn đạt trạng thái giao hàng từ tool result. |

Cùng cấu trúc, câu hỏi về policy đi vào FAQ và yêu cầu hoàn tiền đi vào Refunds Agent. Mỗi nhánh có tools riêng. Bài minh họa một lượt tra đơn với bốn lần gọi model tính cả kiểm tra đầu vào và routing. Phép tra dictionary cục bộ chỉ chiếm phần thời gian nhỏ. Điều đó cho thấy cách dùng trace để quyết định nên tối ưu số lần gọi model, kích thước context hay thời gian thực thi tool.

**Thực hành.** Dùng dữ liệu giả để thử một mã đơn tồn tại, một mã không tồn tại và một yêu cầu lạc chủ đề. Kiểm tra agent đích, đối số dùng để tra và nội dung cuối. Với nhánh hoàn tiền, giữ quy tắc xét duyệt và chống gửi trùng trong tầng nghiệp vụ.

[Lab hỗ trợ khách hàng](https://github.com/oracle-university-labs/ou-generativeai-pro/blob/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/OpenAI/08_customer_support.py)

Trong workspace cục bộ, trace của lần chạy thử nằm ở `results/OpenAI-08_customer_support.log`.
