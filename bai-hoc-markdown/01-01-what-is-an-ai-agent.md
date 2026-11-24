# AI agent là gì?

Mô-đun 01 · Bài 01 · Oracle Student Guide, trang 11–16 · [Mục lục](README.md)

Chatbot tiếp nhận câu hỏi và sinh câu trả lời. Workflow truyền thống thực thi các bước đã định trong mã. AI agent nhận một mục tiêu và chọn bước kế tiếp dựa trên yêu cầu, các công cụ được cấp và kết quả của những bước đã chạy. Cả ba có thể xuất hiện trong cùng một sản phẩm.

LLM xử lý ngôn ngữ và đề xuất bước tiếp theo. Khi được đặt trong một agent, đầu ra của mô hình có thể trở thành yêu cầu gọi công cụ. Ứng dụng thực thi lời gọi, đưa kết quả về cho mô hình, rồi lặp lại hoặc trả lời. Quy trình thường đi qua tiếp nhận đầu vào, quyết định, thực thi và quan sát kết quả.

**Ví dụ.** Khi tìm chuyến bay, agent có thể hỏi lại ngày khởi hành, tra lịch bay rồi so sánh kết quả. Nếu API trả về danh sách trống, bước sau có thể là hỏi người dùng có thể đổi ngày hay không. Một chatbot chỉ có kiến thức từ mô hình sẽ thiếu dữ liệu lịch bay tại thời điểm hỏi.

**Tự kiểm tra.** Với yêu cầu xem trạng thái đơn hàng rồi đổi địa chỉ giao hàng, bước nào lấy dữ liệu và bước nào thay đổi dữ liệu?
