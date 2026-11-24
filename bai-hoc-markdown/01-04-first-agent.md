# Xây dựng AI agent đầu tiên

Mô-đun 01 · Bài 04 · Oracle Student Guide, trang 28–45 · [Mục lục](README.md)

Bài thực hành dùng LangChain cho một agent toán học. Môi trường gồm Python, gói tích hợp mô hình và gói LangChain. Các ví dụ trong workshop minh họa cùng một vòng lặp ở nhiều framework, gồm LangChain/LangGraph, OpenAI Agents SDK, CrewAI và Smolagents.

1. Khởi tạo chat model bằng `init_chat_model`.
2. Đăng ký phép cộng, nhân, chia và căn bậc hai bằng `@tool`. Tên hàm và docstring cho mô hình biết chức năng. Type hint giúp framework dựng schema. Thân hàm thực hiện phép tính và kiểm tra đầu vào.
3. Truyền mô hình và các tool vào `create_agent`. Gửi câu hỏi bằng `agent.invoke` với danh sách tin nhắn.
4. Đọc tin nhắn cuối để lấy đáp án và xem các tin nhắn tool để theo dõi phép tính trung gian.

Hãy thử tính tổng của 27 và 45 trong một lần gọi. Với bài nhân 18 với 5 rồi chia cho 6, kiểm tra bước chia dùng kết quả 90 để ra 15. Với bài căn bậc hai của diện tích hình chữ nhật 9 × 4, kết quả trung gian là 36 và kết quả cuối là 6. Thử thêm phép chia cho 0 để xem cách tool báo lỗi.

## Tool schema và ba kịch bản trong guide

Trong Python, **decorator** đăng ký hàm với framework. **Type hints** cho đối số giúp dựng input schema. **Docstring** mô tả khi nào nên gọi tool, còn **return annotation** mô tả kiểu dữ liệu dự kiến. Một helper kiểu `run_agent` có thể dùng chung để gửi câu hỏi và in final message sau khi `agent.invoke` trả về.

| Kịch bản trong guide | Tool trace cần quan sát |
| --- | --- |
| Cộng 42 và 58 | `add` trả 100. |
| Nhân 15 với 8 rồi chia 3 | `multiply` trả 120, sau đó `divide` nhận 120 và 3, trả 40. |
| Hình chữ nhật 12 × 7 | Tính diện tích 84 rồi gọi `square_root` trên 84 để ra khoảng 9,165. |

Kiểm tra đầu vào cho cả `divide` với mẫu số 0 và `square_root` với số âm. Khi đổi framework, xác định nơi khai báo schema, nơi gọi hàm và nơi đọc final answer. LangGraph cho phép biểu diễn flow bằng graph, Agents SDK có orchestration và tracing, CrewAI tổ chức agent theo vai trò, còn Smolagents là lựa chọn nhỏ gọn để quan sát internals.

[Lab LangChain của Oracle](https://github.com/oracle-university-labs/ou-generativeai-pro/blob/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/LangChain/first_agent.py)
