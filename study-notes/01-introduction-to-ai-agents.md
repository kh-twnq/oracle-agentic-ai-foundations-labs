# Introduction to AI Agents

Module 1 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), trang 9–54 · [Mục lục](README.md)

AI agent dùng LLM để chọn bước tiếp theo dựa trên mục tiêu, tools được cấp và kết quả của các bước trước. Module này giải thích agent loop, so sánh các reasoning patterns, xây một math agent và xem các lớp guardrail cần có khi agent được phép hành động. (trang 9–11)

## AI agent và Agent Execution Loop

| Kiểu hệ thống | Cách xử lý yêu cầu |
| --- | --- |
| Chatbot | Nhận message và tạo câu trả lời. |
| Workflow | Chạy các bước đã được định nghĩa trong application. |
| AI agent | Chọn hành động theo mục tiêu, dùng tools và cập nhật quyết định khi có kết quả mới. |

LLM riêng lẻ xử lý input và context được gửi vào. Trong agent, LLM đề xuất bước tiếp theo, application thực thi tool call và đưa kết quả trở lại context. Runtime giữ state để các bước nối được với nhau. (trang 12–14)

**Agent Execution Loop** đi qua `Perceive → Reason → Act → Observe`. Agent tiếp nhận input hoặc feedback, chọn bước, thực thi hành động và đọc tool result. Ví dụ tìm chuyến bay dùng tool tra cứu, sau đó dựa vào các lựa chọn trả về để trình bày kết quả. Điều kiện dừng có thể là đã đạt mục tiêu, đạt giới hạn số lượt, gặp lỗi hoặc cần chuyển cho người xử lý. (trang 15–16)

## Agent Core Components

- **LLM** hiểu intent, chọn tools và arguments, diễn giải kết quả và soạn final answer. Chọn model dựa trên capability, cost và latency. Một workflow có thể dùng model nhỏ cho routing và model mạnh hơn cho bước reasoning phức tạp. (trang 17–19)
- **Tools** cho phép agent truy cập dữ liệu hoặc thực hiện hành động. Application cung cấp JSON schemas, tiếp nhận structured tool call, kiểm tra arguments rồi chạy implementation. Tool result được gửi lại model để tiếp tục lượt chạy. (trang 20)
- **Orchestration** quản lý loop, tool routing, state, memory và guardrails. Short-term memory giữ context của phiên. Long-term memory có thể truy xuất từ history, tài liệu hoặc knowledge base khi cần. Runtime dùng state để quyết định tiếp tục, retry, dừng hay escalate. (trang 21, 53–54)

![Orchestration kết nối LLM để reasoning và Tools để thực hiện hành động trong agent loop.](images/01-agent-components.png)

## Reasoning Patterns

| Pattern | Cách xử lý |
| --- | --- |
| **Chain-of-Thought (CoT)** | Chia bài toán thành một chuỗi bước trung gian. Hữu ích khi dữ kiện đã có trong input và bài toán cần lập luận nhiều bước. |
| **ReAct (Reasoning + Acting)** | Xen kẽ quyết định, tool call và observation. Dữ liệu từ tool có thể thay đổi bước kế tiếp. |
| **Tree-of-Thoughts (ToT)** | Khám phá và đánh giá nhiều nhánh trước khi chọn hướng giải. Cần thêm lượt đánh giá khi số nhánh tăng. |

CoT dựa trên dữ kiện trong context và kiến thức của model. ReAct bổ sung observation từ môi trường, chẳng hạn gọi search tool để kiểm tra đạo diễn và năm phát hành của một bộ phim rồi dùng dữ liệu trả về để trả lời. Trace quan sát được có thể ghi tool call, arguments và kết quả để kiểm tra cách agent đi tới câu trả lời. (trang 22–27)

## Build the first AI agent

Guide giới thiệu **LangChain/LangGraph** cho workflows có state, **OpenAI Agents SDK** cho orchestration, tracing và guardrails, **CrewAI** cho nhóm agents theo vai trò, và **Smolagents** cho ví dụ nhỏ gọn. Bài thực hành chọn LangChain và triển khai quy trình sau. (trang 28–30)

1. Khởi tạo model bằng `init_chat_model()`. (trang 31)
2. Đăng ký `add`, `multiply`, `divide` và `square_root` bằng `@tool`. Tên và docstring giúp model biết lúc nào nên gọi tool. Type hints mô tả arguments để framework dựng schema, còn return annotation mô tả kiểu kết quả dự kiến. Kiểm tra mẫu số bằng 0 và đầu vào âm của căn bậc hai trong function body. (trang 32–38)
3. Truyền model và tools vào `create_agent()`. Dùng `agent.invoke()` để gửi user message, sau đó kiểm tra tool calls, tool results và final answer. (trang 39–42)

| Bài toán của guide | Tool calls và kết quả |
| --- | --- |
| 42 + 58 | Một lần gọi `add`, kết quả 100. |
| 15 × 8 rồi chia 3 | `multiply` trả 120, sau đó `divide` dùng 120 để trả 40. |
| Hình chữ nhật 12 × 7, tìm diện tích và căn bậc hai của diện tích | Tính diện tích 84, rồi đưa 84 vào `square_root` để được khoảng 9,17. |

Hai bài cuối minh họa việc dùng output của một tool làm arguments cho tool tiếp theo và để agent tự chọn thứ tự thao tác. (trang 43–45)

## Safety and Guardrails

Threat model của guide gồm **prompt injection**, **tool misuse**, **memory poisoning**, **data exfiltration** và **runaway execution**. Hai case study về Slack AI và ChatGPT memory minh họa rủi ro khi agent xử lý nội dung truy xuất hoặc lưu thông tin qua nhiều phiên. Việc kiểm soát provenance, quyền đọc hoặc ghi và dữ liệu được trả ra cần được thực hiện ở nhiều lớp. (trang 46–50)

| Lớp Defense in Depth | Trách nhiệm |
| --- | --- |
| **Input Validation** | Kiểm tra input và coi nội dung truy xuất từ bên ngoài là dữ liệu chưa tin cậy. |
| **LLM Guardrails** | Dùng instructions, giới hạn tool access và chuyển trường hợp cần xem xét cho người xử lý. |
| **Tool Boundaries** | Áp dụng least privilege, kiểm tra arguments, sandbox execution khi cần và dùng human-in-the-loop cho hành động có hệ quả lớn. Idempotency giúp retry thao tác ghi an toàn. |
| **Output Filtering** | Kiểm tra PII, dữ liệu nhạy cảm, sự phù hợp và căn cứ của câu trả lời. |
| **Observability** | Theo dõi traces, errors, thời gian và chi phí, đồng thời che dữ liệu nhạy cảm trong log. |

Agent frameworks giúp quản lý loop và tool calling khi workflow phức tạp hơn. Các giới hạn như iteration budget và tool permissions vẫn cần được đặt tại runtime và application. (trang 51–54)
