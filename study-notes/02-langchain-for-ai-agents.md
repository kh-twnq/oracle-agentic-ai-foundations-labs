# LangChain for AI Agents

Student Guide · What You’ve Learned · trang 89 · [Mục lục](README.md)

1. **LangChain** cung cấp giao diện thống nhất cho nhiều LLM providers.
2. `chain = prompt | model | StrOutputParser()`. Toán tử `|` nối các bước trong chain.
3. **LLM = Reasoning.** Model quyết định gọi tool nào và truyền arguments gì. Việc thực thi thuộc lớp application.
4. **Application = Execution.** LangChain phân tích tool request, chạy hàm Python rồi gửi kết quả về model.
5. **ReAct Loop** chạy theo vòng `Reason → Act → Observe → Repeat` đến khi model không cần gọi thêm tool.
6. **Conversation = State.** Mỗi message được thêm vào history. Trong flow của bài, toàn bộ history được gửi lại trong mỗi LLM API call.
7. **`agent.invoke()`** gói việc chuẩn bị schemas, gọi API, parsing và execution vào một lời gọi.

![Pipeline LangChain truyền output từ prompt đến model rồi qua StrOutputParser.](images/02-langchain-chain.png)

## Ôn Skill Check mô-đun 2

Số trang dưới đây trỏ tới các phần giải thích và ví dụ trong [Oracle Student Guide](https://mylearn.oracle.com/ou/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course).

### 1. LangChain gửi gì trong first agent request?

**Phương án 1. LangChain gửi user message và các tool definitions có sẵn.** Trong ví dụ, `agent.invoke()` nhận câu hỏi từ Python code. Request đầu gửi đến Model API có hai trường chính. `messages` chứa câu hỏi với role `user`, còn `tools` chứa danh sách tool model được phép yêu cầu gọi. (trang 74–75)

Mỗi tool definition có tên, description và JSON schema cho parameters, gồm tên, kiểu dữ liệu và các tham số bắt buộc. LangChain dựng schema từ hàm đăng ký bằng `@tool`. Model dùng docstring để chọn tool và dùng type hints để tạo arguments đúng kiểu. (trang 66–67, 75)

### 2. Vì sao cần hiểu LangChain internals?

**Phương án 2. Hiểu internals giúp debug lỗi và tối ưu agent khi đưa vào production.** Guide nêu bốn ứng dụng cụ thể gồm debug agent failures, xây custom agent loops, tối ưu performance và triển khai production. (trang 86)

Guide lần theo những bước ẩn sau `agent.invoke()`, gồm dựng tool schema, gửi request, parse tool call, tra tool registry, chạy hàm Python và thêm tool result vào history. Khi debug, trace cho thấy tool nào được gọi, arguments gì đã được dùng và tool trả về kết quả gì. Docstring và schema vẫn là dữ liệu đầu vào để model chọn tool. (trang 66–67, 85–88)

Các thành phần liên quan trong guide gồm LangGraph để điều phối agent bằng graph và LangSmith để tracing, testing và debugging. (trang 59)

### 3. Unified model interface giúp gì khi đổi provider?

**Phương án 2. Developer có thể đổi model provider với ít thay đổi code.** Guide dùng `init_chat_model()` để minh họa cùng một cách khởi tạo cho model của OpenAI và Anthropic. Phần gọi model trong application có thể tiếp tục dùng interface chung. (trang 60, 89)

Khả năng tool calling, context window và reasoning vẫn khác nhau giữa các model. Setup trong guide cài provider integration tương ứng, ví dụ `langchain-openai` hoặc `langchain-anthropic`. Ví dụ OpenAI cấu hình `OPENAI_API_KEY` cho phần xác thực. (trang 60, 71)

### 4. LCEL dùng để làm gì?

**Phương án 1. LangChain Expression Language (LCEL) dùng toán tử pipe `|` để nối các thành phần của chain.** Trong `chain = prompt | model | StrOutputParser()`, output của mỗi bước trở thành input cho bước tiếp theo. (trang 62, 89)

Khi gọi `chain.invoke()` trong ví dụ của guide, `ChatPromptTemplate` điền giá trị vào placeholder, chat model xử lý prompt, và `StrOutputParser()` lấy phần text thành chuỗi Python. `PromptTemplate` dùng cho text có biến, còn `ChatPromptTemplate` hỗ trợ các role như system, human và AI. (trang 61–62)

### 5. Vì sao model trả tool call khi cần chạy hàm Python?

**Phương án 1. Model đảm nhận reasoning và yêu cầu gọi tool. LangChain thực thi hàm ở phía application.** Model trả structured `tool_calls` gồm tên tool, arguments và call ID. Trong response minh họa, arguments là một JSON string. LangChain parse response, tra tên tool trong registry rồi gọi hàm Python với arguments đã parse. (trang 76–79, 89)

Guide dùng phép tính 15 × 8 ÷ 3 để theo dõi ReAct loop.

| Bước | Điều xảy ra trong ví dụ | Trang |
| --- | --- | --- |
| Tool call đầu | Model yêu cầu gọi `multiply` với 15 và 8. LangChain chạy hàm và nhận 120. | 76–79 |
| Tool result | LangChain thêm message role `tool` với `tool_call_id` khớp lời gọi gốc, rồi gửi lại conversation history. | 80 |
| Tool call tiếp theo | Model dùng 120 từ tool result làm argument để gọi `divide`. LangChain chạy phép chia cho 3 và gửi lại kết quả 40.0. | 81–83 |
| Final answer | Response của model có nội dung text và kết thúc chuỗi tool calls. LangChain trả result về cho Python code. | 84–85 |
