# Tạo agent bằng LangChain

Mô-đun 02 · Bài 02 · Oracle Student Guide, trang 63–72 · [Mục lục](README.md)

Bài lab mở rộng lời gọi mô hình bằng công cụ Python. Mỗi công cụ cần tên rõ, docstring giải thích mục đích và type hint cho tham số. Framework chuyển mô tả này thành schema gửi kèm yêu cầu mô hình. Lời gọi do mô hình tạo sẽ được ánh xạ về hàm Python đã đăng ký.

Khởi tạo mô hình, định nghĩa hai phép nhân và chia bằng `@tool`, rồi truyền chúng vào `create_agent`. Gửi câu hỏi trong khóa `messages` của `agent.invoke`. Với phép tính nhiều bước, framework trả kết quả của phép nhân về mô hình để nó chọn tham số cho phép chia. Kiểm tra mẫu số ngay trong hàm và biểu đạt lỗi đủ rõ để agent xử lý.

**Thực hành.** Gửi yêu cầu nhân 14 với 9 rồi chia cho 7. Trong lịch sử phải lần lượt thấy 126 và 18. Thử mẫu số 0 để xác nhận kết quả lỗi xuất hiện ở đúng lời gọi.

[Lab LangChain agent](https://github.com/oracle-university-labs/ou-generativeai-pro/blob/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/LangChain/first_agent.py)
