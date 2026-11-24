# Multi-agent orchestration với Handoffs

Mô-đun 04 · Bài 05 · Oracle Student Guide, trang 149–152 · [Mục lục](README.md)

Trong mẫu handoff, agent phân luồng tiếp nhận yêu cầu rồi chuyển vai trò xử lý cho agent chuyên trách. Agent đích có chỉ dẫn và công cụ riêng. `handoff_description` mô tả loại yêu cầu phù hợp, còn danh sách `handoffs` của agent phân luồng giới hạn các đích có thể chuyển đến.

Trong mẫu manager, agent trung tâm gọi các agent chuyên trách làm tool qua `as_tool`. Manager nhận kết quả rồi tổng hợp phản hồi. Handoff phù hợp khi một chuyên gia phụ trách phần còn lại của lượt chạy. Manager phù hợp khi cần hợp nhất nội dung từ nhiều chuyên gia.

## Handoff description và câu hỏi định tuyến

Guide dùng một **Triage Agent** với các **specialist agents** cho môn học. Mỗi specialist nhận instructions riêng về cách trả lời. `handoff_description` giúp Triage Agent chọn đúng đích. Thiết lập `handoffs` của triage agent quy định các agent được phép nhận quyền xử lý. Kiểm tra câu hỏi nằm ngoài mọi nhóm để thấy hành vi fallback mà triage instructions đang quy định.

Khi dùng **manager pattern**, câu trả lời của chuyên gia quay về agent chính qua `as_tool()`. Khi dùng **handoff pattern**, agent đích tiếp tục lượt chạy và có thể tạo final output. Khi kiểm tra một luồng nhiều agent, xem trace có đúng chuyên gia, đúng tool scope và context cần thiết ở đích hay không.

**Thực hành.** Tạo hai chuyên gia toán và lịch sử. Gửi một câu hỏi rõ thuộc mỗi nhóm rồi thử câu hỏi cần cả hai. Xem ai trả lời cuối và có đủ dữ kiện để hoàn thành hay không.

[Lab handoffs](https://github.com/oracle-university-labs/ou-generativeai-pro/blob/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/OpenAI/06_multi_agent_handoffs.py)
