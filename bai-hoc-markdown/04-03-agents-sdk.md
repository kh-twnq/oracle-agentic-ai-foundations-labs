# Khởi tạo và chạy agent bằng Agents SDK

Mô-đun 04 · Bài 03 · Oracle Student Guide, trang 136–141 · [Mục lục](README.md)

Định nghĩa `Agent` bằng tên, chỉ dẫn, mô hình và danh sách công cụ tùy nhu cầu. Chạy bằng `Runner.run_sync` trong ví dụ đồng bộ hoặc `await Runner.run` trong luồng bất đồng bộ. Đọc `result.final_output` để lấy kết quả cuối.

Trong mỗi vòng, runner gửi đầu vào và chỉ dẫn đến mô hình. Nếu có yêu cầu gọi tool, runner thực thi, tích lũy kết quả và gửi lượt tiếp theo. Nếu có chuyển giao, runner dùng agent đích. Lượt chạy hoàn tất khi agent tạo đầu ra cuối phù hợp. Ứng dụng vẫn chịu trách nhiệm xử lý lỗi, hiển thị kết quả và áp dụng quy tắc cho các thao tác ghi dữ liệu.

**Thực hành.** Tạo agent hướng dẫn học tập, đặt chỉ dẫn trả lời bằng hai gạch đầu dòng và chạy với một chủ đề quen thuộc. Kiểm tra đầu ra cuối và trace của lần gọi mô hình.

[Lab Agents SDK đầu tiên](https://github.com/oracle-university-labs/ou-generativeai-pro/blob/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/OpenAI/04_first_agent.py)
