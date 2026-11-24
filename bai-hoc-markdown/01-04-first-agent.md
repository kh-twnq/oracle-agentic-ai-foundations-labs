# Xây dựng AI agent đầu tiên

Mô-đun 01 · Bài 04 · Oracle Student Guide, trang 28–45 · [Mục lục](README.md)

Bài thực hành dùng LangChain cho một agent toán học. Môi trường gồm Python, gói tích hợp mô hình và gói LangChain. Các ví dụ trong workshop minh họa cùng một vòng lặp ở nhiều framework, gồm LangChain/LangGraph, OpenAI Agents SDK, CrewAI và Smolagents.

1. Khởi tạo chat model bằng `init_chat_model`.
2. Đăng ký phép cộng, nhân, chia và căn bậc hai bằng `@tool`. Tên hàm và docstring cho mô hình biết chức năng. Type hint giúp framework dựng schema. Thân hàm thực hiện phép tính và kiểm tra đầu vào.
3. Truyền mô hình và các tool vào `create_agent`. Gửi câu hỏi bằng `agent.invoke` với danh sách tin nhắn.
4. Đọc tin nhắn cuối để lấy đáp án và xem các tin nhắn tool để theo dõi phép tính trung gian.

Hãy thử tính tổng của 27 và 45 trong một lần gọi. Với bài nhân 18 với 5 rồi chia cho 6, kiểm tra bước chia dùng kết quả 90 để ra 15. Với bài căn bậc hai của diện tích hình chữ nhật 9 × 4, kết quả trung gian là 36 và kết quả cuối là 6. Thử thêm phép chia cho 0 để xem cách tool báo lỗi.

[Lab LangChain của Oracle](https://github.com/oracle-university-labs/ou-generativeai-pro/blob/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/LangChain/first_agent.py)
