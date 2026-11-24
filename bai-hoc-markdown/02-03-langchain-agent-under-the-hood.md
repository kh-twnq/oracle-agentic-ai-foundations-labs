# Vòng lặp bên trong LangChain agent

Mô-đun 02 · Bài 03 · Oracle Student Guide, trang 73–88 · [Mục lục](README.md)

1. `agent.invoke` đặt câu hỏi vào trạng thái tin nhắn. LangChain gửi lịch sử và schema của các tool đến API mô hình.
2. Mô hình trả một tool call gồm tên, đối số và mã lời gọi. LangChain phân tích phản hồi, tra tool từ registry và gọi hàm thật.
3. Framework thêm tin nhắn kết quả gắn với mã lời gọi rồi gửi lại lịch sử. Nếu có phép tính tiếp theo, mô hình tạo tool call mới dựa trên kết quả vừa nhận.
4. Khi phản hồi chỉ còn nội dung trả lời, framework kết thúc và trả trạng thái về chương trình gọi.

Trong bài toán nhiều bước, có ba phản hồi từ mô hình khi lần lượt yêu cầu phép nhân, yêu cầu phép chia và kết luận. Số lần gọi mô hình có thể khác số lần chạy hàm. Khi điều tra lỗi, xem schema, đối số thực tế, kết quả tool và tin nhắn cuối. Vị trí đầu tiên chúng sai khác với mong đợi thường chỉ ra lớp cần sửa.

**Thực hành.** In loại của từng tin nhắn trong `result["messages"]` và xác định tool call nào có kết quả được phép chia dùng lại.
