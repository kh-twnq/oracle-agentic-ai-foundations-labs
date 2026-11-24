# Công cụ và function calling trong Agents SDK

Mô-đun 04 · Bài 04 · Oracle Student Guide, trang 142–148 · [Mục lục](README.md)

Agents SDK có công cụ do nền tảng cung cấp, công cụ từ hàm ứng dụng và agent được sử dụng như công cụ. Công cụ hosted phục vụ các tác vụ như tìm tài liệu hoặc tìm kiếm web. Nếu agent chính cần hỏi một chuyên gia rồi tự tổng hợp, có thể thêm agent chuyên gia bằng `as_tool`.

Dùng `@function_tool` cho hàm Python. Type hint và docstring cung cấp schema và mô tả cho mô hình. LLM sinh tên hàm và đối số, runner điều phối lời gọi, và hàm thực thi xử lý nghiệp vụ. Kiểm tra dữ liệu và quyền trong hàm trước khi đọc hoặc thay đổi dữ liệu thật.

Cùng ví dụ tính toán, bài LangChain đăng ký bằng `@tool` rồi gọi `agent.invoke`, còn Agents SDK dùng `@function_tool` và `Runner`. Trong cả hai trường hợp, kết quả của phép tính đầu có thể trở thành đầu vào của phép thứ hai.

[Lab function tools](https://github.com/oracle-university-labs/ou-generativeai-pro/blob/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/OpenAI/05_function_tools.py)
