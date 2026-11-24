# Khởi tạo và chạy agent bằng Agents SDK

Mô-đun 04 · Bài 03 · Oracle Student Guide, trang 136–141 · [Mục lục](README.md)

Định nghĩa `Agent` bằng tên, chỉ dẫn, mô hình và danh sách công cụ tùy nhu cầu. Chạy bằng `Runner.run_sync` trong ví dụ đồng bộ hoặc `await Runner.run` trong luồng bất đồng bộ. Đọc `result.final_output` để lấy kết quả cuối.

Trong mỗi vòng, runner gửi đầu vào và chỉ dẫn đến mô hình. Nếu có yêu cầu gọi tool, runner thực thi, tích lũy kết quả và gửi lượt tiếp theo. Nếu có handoff, runner dùng agent đích. Lượt chạy hoàn tất khi agent tạo đầu ra cuối phù hợp. Ứng dụng vẫn chịu trách nhiệm xử lý lỗi, hiển thị kết quả và áp dụng quy tắc cho các thao tác ghi dữ liệu.

## Runner xử lý một lượt chạy như thế nào?

`Agent` là cấu hình tái sử dụng. `Runner` thực hiện một phiên chạy với input cụ thể. Chỉ dẫn cho biết phạm vi và format mong muốn, còn tool list quy định những hành động model có thể yêu cầu. Lấy `result.final_output` sau khi lượt chạy kết thúc. Nếu dùng structured output, giá trị có thể là đối tượng theo type đã khai báo.

Sau khi cài `openai-agents` và cấu hình `OPENAI_API_KEY`, ví dụ độc lập dưới đây dùng default model của cấu hình SDK. Bài lab liên kết cuối trang có thiết lập và câu hỏi của workshop.

```python
from agents import Agent, Runner

guide = Agent(
    name="Study guide",
    instructions="Give two short bullet points and one review question.",
)
result = Runner.run_sync(guide, "How do tool calls use schemas?")
print(result.final_output)
```

Đọc trace từ input đến final output. Nếu có tool hoặc handoff, callback và tool result được Runner đưa vào vòng tiếp theo. Với một câu hỏi đơn giản, trace có thể chỉ có một lần gọi model.

**Thực hành.** Tạo agent hướng dẫn học tập, đặt chỉ dẫn trả lời bằng hai gạch đầu dòng và chạy với một chủ đề quen thuộc. Kiểm tra đầu ra cuối và trace của lần gọi mô hình.

[Lab Agents SDK đầu tiên](https://github.com/oracle-university-labs/ou-generativeai-pro/blob/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/OpenAI/04_first_agent.py)
