# Gọi Responses API và nối các lượt hội thoại

Mô-đun 04 · Bài 02 · Oracle Student Guide, trang 130–135 · [Mục lục](README.md)

Ví dụ đầu tiên tạo client Python, gọi `client.responses.create` với `model` và `input`, rồi đọc `response.output_text`. Phản hồi cấu trúc còn có mã định danh và các phần tử đầu ra, tùy loại tác vụ. Giữ khóa API trong môi trường của chương trình chạy lab.

Để nối hai lượt, lưu `id` của phản hồi đầu và dùng `previous_response_id` khi gửi lượt hai. Ví dụ, lượt đầu lưu thông tin dự án mang tên Sao Mai. Lượt sau chỉ hỏi tên của dự án và dùng mã phản hồi làm điểm nối. Cấu hình chỉ dẫn cần thiết ở từng yêu cầu.

Thông qua tham số `tools`, bài học minh họa tìm kiếm web, tìm kiếm tài liệu, môi trường chạy mã, điều khiển giao diện và tạo ảnh. Mỗi công cụ có phạm vi và cấu hình riêng. Với tìm kiếm web, kiểm tra cả câu trả lời lẫn nguồn được trả về.

[Gọi API lần đầu](https://github.com/oracle-university-labs/ou-generativeai-pro/blob/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/OpenAI/01_hello_responses.py) · [Nối hội thoại](https://github.com/oracle-university-labs/ou-generativeai-pro/blob/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/OpenAI/02_stateful_conversation.py) · [Tìm kiếm web](https://github.com/oracle-university-labs/ou-generativeai-pro/blob/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/OpenAI/03_web_search.py)
