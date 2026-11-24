# Guardrails và tracing trong Agents SDK

Mô-đun 04 · Bài 06 · Oracle Student Guide, trang 153–156 · [Mục lục](README.md)

Guardrail đầu vào kiểm tra phạm vi yêu cầu và định dạng. Guardrail đầu ra kiểm tra kết quả trước khi trả cho người dùng. Với thao tác nhạy cảm, kiểm tra quyền ngay tại tool ghi dữ liệu, vì kiểm tra đầu ra xảy ra sau khi tác vụ đã chạy. Guardrail đầu vào có thể chặn trước agent chính hoặc chạy song song tùy cấu hình.

Bài lab dùng agent kiểm tra nhỏ với kiểu dữ liệu Pydantic có trường Boolean. Hàm gắn `@input_guardrail` gọi agent kiểm tra, rồi trả `GuardrailFunctionOutput` với cờ `tripwire_triggered` nếu yêu cầu nằm ngoài phạm vi. Ứng dụng xử lý trường hợp tripwire để báo rõ loại câu hỏi được hỗ trợ.

Trace hiển thị các lần gọi mô hình, tool, chuyển giao và kiểm tra, giúp tìm lỗi định tuyến hoặc bước gây chậm. Khi ghi trace, che tham số nhạy cảm và nội dung cần giới hạn truy cập.

[Lab guardrails](https://github.com/oracle-university-labs/ou-generativeai-pro/blob/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/OpenAI/07_guardrails.py)
