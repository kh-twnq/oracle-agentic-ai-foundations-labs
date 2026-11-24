# Xây LangChain agent với tool calling

Mô-đun 02 · Bài 02 · Oracle Student Guide, trang 63–72 · [Mục lục](README.md)

Bài lab mở rộng lời gọi mô hình bằng Python tools. Mỗi công cụ cần tên rõ, docstring giải thích mục đích và type hint cho tham số. Framework chuyển mô tả này thành schema gửi kèm yêu cầu mô hình. Lời gọi do mô hình tạo sẽ được ánh xạ về hàm Python đã đăng ký.

Khởi tạo mô hình, định nghĩa hai phép nhân và chia bằng `@tool`, rồi truyền chúng vào `create_agent`. Gửi câu hỏi trong khóa `messages` của `agent.invoke`. Với phép tính nhiều bước, framework trả kết quả của phép nhân về mô hình để nó chọn tham số cho phép chia. Kiểm tra mẫu số ngay trong hàm và biểu đạt lỗi đủ rõ để agent xử lý.

## Setup và các điểm cần quan sát

Bài lab tạo virtual environment, cài LangChain cùng provider integration `langchain-openai` và dùng `python-dotenv` nếu nạp cấu hình từ file `.env`. Giữ `OPENAI_API_KEY` ngoài source code. Phần ReAct có thể nhận một tool để tra dữ liệu hoặc thực thi phép tính tùy mục tiêu. Ở đây, hai tool Python thực hiện đúng một phép toán mỗi lần gọi.

Kết quả `agent.invoke` chứa cả final message và các message trung gian. Với câu hỏi dùng hai phép liên tiếp, xác nhận description phân biệt rõ phép nhân và phép chia, input schema có đủ hai tham số kiểu số và tool thứ hai nhận giá trị do tool thứ nhất trả. Nếu kết quả lỗi được biểu diễn bằng chuỗi, phần gọi phải xử lý trường hợp đó trước khi dùng giá trị như một số.

**Thực hành.** Gửi yêu cầu nhân 14 với 9 rồi chia cho 7. Trong lịch sử phải lần lượt thấy 126 và 18. Thử mẫu số 0 để xác nhận kết quả lỗi xuất hiện ở đúng lời gọi.

[Lab LangChain agent](https://github.com/oracle-university-labs/ou-generativeai-pro/blob/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/LangChain/first_agent.py)
