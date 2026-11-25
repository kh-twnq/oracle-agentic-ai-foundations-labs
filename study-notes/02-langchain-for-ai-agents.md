# LangChain for AI Agents

Module 2 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), trang 55–89 · [Mục lục](README.md)

LangChain kết nối LLM với tools, APIs và nguồn dữ liệu để xây chatbot, agent và ứng dụng Retrieval-Augmented Generation (RAG). Module này bắt đầu từ một chain gồm prompt, model và output parser, sau đó xây agent có thể gọi Python tools. Ví dụ cuối theo dõi câu hỏi tính toán qua ba lần gọi Model API để thấy phần việc của model, framework và application. (trang 55–56)

## LangChain Ecosystem, Models và Prompts

LangChain cung cấp các building blocks như models, prompts, chains, tools và memory. **LangGraph** biểu diễn workflow dạng graph khi cần quản lý state, nhánh và vòng lặp. **LangSmith** cung cấp observability, tracing, testing và debugging. **Integrations** nối framework với model providers, vector databases, search APIs và các hệ thống khác. (trang 57–59)

`init_chat_model()` dùng model identifier có provider prefix. Guide minh họa đổi giữa OpenAI và Anthropic trong cùng cách khởi tạo. Unified model interface giúp giảm số chỗ phải sửa khi chuyển provider. Khả năng tool calling, context window và reasoning vẫn phụ thuộc model đã chọn, còn package và credentials được cấu hình theo integration tương ứng. (trang 60, 71, 89)

Prompt template giữ cấu trúc cố định và điền giá trị vào placeholders tại runtime. Ba dạng trong guide phục vụ các nhu cầu sau. (trang 61)

| Thành phần | Cách dùng |
| --- | --- |
| `PromptTemplate` | Tạo prompt text từ biến như `topic`. |
| `ChatPromptTemplate` | Tạo messages theo role. System định hướng hành vi và giọng điệu, human chứa input của người dùng, AI biểu diễn phản hồi trước đó. |
| Few-shot prompt | Đưa cặp input và output mẫu để định hướng cách model trả lời. |

## LCEL và Chain Composition

LangChain Expression Language (LCEL) dùng toán tử pipe `|` để chuyển output của mỗi bước sang bước kế tiếp. Với `chain = prompt | model | StrOutputParser()`, lời gọi `chain.invoke({"topic": "AI agents"})` điền `topic` vào template, gửi prompt đã tạo đến model, rồi lấy phần text từ chat response. Kết quả là một chuỗi Python để application sử dụng. (trang 62, 89)

![LCEL chuyển dữ liệu từ prompt qua model rồi đến StrOutputParser.](images/02-langchain-chain.png)

## Build agent với Tools và ReAct

Trong ví dụ của Guide, một basic LLM call đi từ input qua model đến output trong một lượt. Agent giữ context của các bước trước và dùng model để chọn bước tiếp theo, chẳng hạn gọi tool, quan sát kết quả hoặc trả lời người dùng. Tools có thể là web search, database query, code execution hoặc lời gọi custom API. Guide giới thiệu built-in tools và custom Python functions đăng ký bằng `@tool`. (trang 63–65)

| Thành phần của Python tool | Vai trò |
| --- | --- |
| `@tool` | Đăng ký function với framework để agent có thể yêu cầu gọi. |
| Tên hàm và type hints | Giúp tạo tool definition và JSON schema cho arguments, ví dụ hai tham số số của `add`. |
| Docstring | Mô tả tác dụng và thời điểm dùng tool để model chọn đúng chức năng. |
| Return annotation, ví dụ `-> float` | Mô tả kiểu kết quả dự kiến để hiểu cách dùng output ở bước sau. |
| Function body | Chứa phép tính, truy vấn hoặc hành động do application thực thi. |

Tool definition mà model nhận có `name`, `description` và `parameters`. Trong payload minh họa, `parameters` xác định kiểu dữ liệu và danh sách trường bắt buộc. (trang 66–69, 75)

**ReAct** tổ chức quá trình này thành vòng lặp. Ở **Reason**, model xác định cần dữ liệu hay hành động gì. Ở **Act**, agent gọi tool hoặc trả lời. Ở **Observe**, model nhận kết quả để ra quyết định tiếp theo. Vòng lặp kết thúc khi agent có đủ thông tin hoặc đạt giới hạn số lượt. Trong ví dụ thời tiết Seattle, agent chọn tool tìm thời tiết, đọc kết quả, rồi trả lời dựa trên dữ liệu vừa nhận. (trang 70)

Bài thực hành thiết lập Python virtual environment và cài `langchain`, `langchain-openai`, `langgraph`, `python-dotenv`. Ví dụ OpenAI đọc `OPENAI_API_KEY` từ cấu hình môi trường. Quy trình của bài lab là khởi tạo model bằng `init_chat_model()`, đăng ký `multiply` và `divide`, truyền model và tools vào `create_agent()`, rồi gọi `agent.invoke()` với user message. Logic kiểm tra chia cho 0 nằm trong hàm `divide`. (trang 71–72) [Hướng dẫn chạy lab](../labs/README.md)

## Agent Loop và Tool Execution

Guide lần theo câu hỏi tính **15 × 8 ÷ 3**. Python code khởi động agent bằng `agent.invoke()`. LangChain chuẩn bị request và xử lý kết quả. Model quyết định tool và arguments. Trong walkthrough, bộ tools gồm `add`, `multiply`, `divide` và `square_root`. (trang 73–78)

| Lần gọi Model API | Dữ liệu gửi đi | Response và bước tiếp theo | Trang |
| --- | --- | --- | --- |
| 1 | `messages` chứa user message. `tools` chứa các tool definitions model được phép dùng. | Model yêu cầu `multiply(15, 8)` với ID `call_001`. LangChain tra registry, thực thi hàm và nhận 120. | 74–79 |
| 2 | History gồm user message, assistant tool call và tool result 120, cùng tool definitions. | Model dùng 120 làm đầu vào của `divide(120, 3)`, với ID `call_002`. LangChain thực thi hàm và nhận 40.0. | 80–82 |
| 3 | History gồm năm messages, tức user message và hai cặp tool call–tool result. Tool definitions vẫn được gửi cùng request. | Model trả câu trả lời bằng text với kết quả 40. LangChain kết thúc vòng lặp và trả result về Python code. | 83–85 |

Một tool call trong payload minh họa có tên, arguments ở dạng JSON string và call ID. LangChain parse arguments, tìm function tương ứng trong **tool registry** rồi thực thi ở application. Tool result là message role `tool`. Trường `tool_call_id` nối nó với đúng lời gọi. Việc gửi lại history trong các request của bài giúp model biết phép nhân đã hoàn thành và dùng kết quả của phép nhân cho phép chia. (trang 76–88)

## Tracing và Debugging

`agent.invoke()` điều phối việc dựng schemas, định dạng request, parse responses, tìm và chạy tools, nối results vào history, rồi quyết định có gọi model tiếp hay đã đến final answer. Khi đọc trace, bắt đầu từ tool definition model đã nhận. Sau đó đối chiếu tên và arguments trong tool call, hàm thật trong registry, kết quả thực thi và message được gửi lại. Guide dùng khả năng theo dõi các bước này để giải thích vì sao hiểu internals giúp debug, xây custom agent loop, tối ưu performance và triển khai production. (trang 85–89)
