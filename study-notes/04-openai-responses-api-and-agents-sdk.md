# OpenAI Responses API and Agents SDK

Module 4 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), trang 123–162 · [Mục lục](README.md)

Module này đi từ một Responses API call đến hệ thống Customer Support có function tools, handoffs, guardrails và tracing. Mỗi lớp trong OpenAI agent stack đảm nhận một phần của flow. (trang 123–129)

## OpenAI agent stack

Application giữ UI, business rules và tích hợp dữ liệu. **Responses API** nhận input, cấu hình tools và trả structured output. **Agents SDK** xây trên Responses API và cung cấp Agent, Runner, handoffs, guardrails và tracing. Guide dùng Responses API trực tiếp cho flow ngắn hoặc khi application muốn điều khiển từng bước. Với multi-agent orchestration, SDK thay application quản lý phần lặp và chuyển giao. Quy tắc nghiệp vụ, như xác nhận trước khi đặt chuyến bay, vẫn do application hoặc tool thực thi. (trang 125–129)

![OpenAI agent stack gồm Responses API, Agents SDK, guardrails và tracing.](images/04-openai-agent-stack.png)

## Responses API và Conversation Chaining

Ví dụ Python cài package `openai`, cấu hình `OPENAI_API_KEY`, rồi gọi `client.responses.create()` với `model` và `input`. API có thể nhận text hoặc structured input. `response.output_text` lấy nội dung text để hiển thị. Khi cần theo dõi tool calls, application có thể xem các output items của response. (trang 130–132)

Để nối hai lượt, gửi `previous_response_id` bằng ID của response trước. Ví dụ của Guide cung cấp thông tin một người ở lượt đầu, rồi hỏi lại thông tin đó ở lượt sau. Application xác định conversation nào cần nối thông qua response ID. (trang 133)

Các built-in tools được Guide giới thiệu gồm **Web Search**, **File Search**, **Code Interpreter**, **Computer Use** và **Image Generation**. Application khai báo tools được cấp trong request. Model chọn có dùng tool nào theo yêu cầu. Ví dụ Web Search so sánh câu hỏi cần thông tin mới với câu hỏi kiến thức phổ thông để quan sát thời điểm model quyết định tìm kiếm. (trang 134–135)

## Agents SDK và Function Calling

Trong bài đầu tiên, `Agent` khai báo tên, instructions, model và tools. `Runner.run_sync()` thực hiện lượt chạy đồng bộ, còn `await Runner.run()` phục vụ flow bất đồng bộ. `result.final_output` trả kết quả cuối. Runner gửi input cho model, thực thi tool khi được yêu cầu, gắn tool result vào lượt tiếp theo và dừng khi có final output. (trang 136–141)

| Tool type | Cách dùng trong Guide |
| --- | --- |
| **Hosted Tools** | Dùng khả năng do nền tảng cung cấp như Web Search, File Search hoặc Code Interpreter. |
| **Function Tools** | Dùng `@function_tool` để đăng ký Python function. Type hints và docstring giúp tạo schema và description gửi cho model. |
| **Agents as Tools** | Dùng `as_tool()` để gọi specialist agent và lấy kết quả về agent chính. |

Math agent đăng ký `add`, `multiply`, `divide` và `square_root`. Với phép tính nhiều bước, Runner chạy phép nhân, trả kết quả cho model, rồi thực hiện phép chia do model yêu cầu. Application xử lý phép tính và kiểm tra đầu vào trong Python function. Guide đối chiếu `@function_tool`, `Agent`, `Runner.run_sync()` và `final_output` với `@tool`, `create_agent()` và `agent.invoke()` ở LangChain. (trang 142–148)

## Multi-Agent Systems

- **Handoff pattern** dùng Triage Agent để chọn specialist và chuyển quyền xử lý lượt chạy. `handoff_description` mô tả khi nào nên chuyển đến một agent. `handoffs` khai báo các đích được phép. Bài lab định tuyến câu hỏi đến các tutor theo chủ đề.
- **Manager pattern** giữ lượt chạy ở agent trung tâm. Manager gọi specialists thông qua `as_tool()`, nhận các kết quả rồi tạo câu trả lời chung. (trang 149–152)

## Guardrails, Tracing và Customer Support

**Input guardrail** kiểm tra phạm vi và định dạng request. Guide minh họa hai cách chạy, gồm chặn trước và chạy song song với agent. **Output guardrail** kiểm tra kết quả về chất lượng, chính sách hoặc dữ liệu nhạy cảm. Ví dụ dùng một checker agent trả Boolean có cấu trúc bằng Pydantic. Hàm `@input_guardrail` trả `GuardrailFunctionOutput` và có thể kích hoạt `tripwire_triggered`. Trace ghi agent calls, tool arguments, handoffs, guardrail results và token usage để phân tích lượt chạy. (trang 153–156)

System Customer Support dùng **Triage Agent** để handoff sang **Order Status**, **Refunds** hoặc **FAQ**. Order Status tra đơn qua function tool. Refunds dùng tool nghiệp vụ, và FAQ có thể dùng Web Search. Input guardrail kiểm tra câu hỏi thuộc phạm vi support. (trang 157–159)

Với đơn `ORD-001`, trace minh họa guardrail và triage chạy song song. Triage chuyển sang Order Status Agent, agent gọi `lookup_order`, nhận trạng thái giao hàng và tạo final answer. Nhìn từng span giúp xác định thời gian nằm ở các model calls hay Python tool. Guide dùng ví dụ này để nối các khái niệm từ conversation state đến orchestration và observability. (trang 160–162) [Hướng dẫn chạy lab](../labs/README.md)
