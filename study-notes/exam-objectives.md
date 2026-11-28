# Đối chiếu mục tiêu thi 1Z0-1157-26

Bảng này dẫn tới nội dung ôn tập cho 28 mục tiêu ở trang 2–3 của đề cương Agentic AI Foundations Associate. Mỗi hàng mô tả điều cần nắm và dẫn tới phần giải thích hoặc bài thực hành tương ứng.

Nguồn đối chiếu gồm đề cương thi của Oracle, đề cương khóa học công khai và mã lab Oracle University. Các module giữ tham chiếu tới Student Guide trên MyLearn. [Đề cương thi](https://education.oracle.com/agentic-ai-foundations-associate/pexam_1Z0-1157-26) · [Tổng quan sáu module của Oracle University](https://blogs.oracle.com/oracleuniversity/oracle-agentic-ai-foundations-training-certification-now-available) · [Student Guide trên MyLearn](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course)

## Introduction to AI Agents

| Mục tiêu ôn tập | Nội dung trong repo |
| --- | --- |
| Phân biệt chatbot, workflow theo quy tắc và agent dựa trên mức tự chủ, cách xử lý và cách dùng tool. | [AI agent là gì?](01-introduction-to-ai-agents.md#1-what-is-an-ai-agent) |
| Giải thích vai trò của LLM, tool và runtime trong vòng lặp agent. | [Thành phần và vòng lặp](01-introduction-to-ai-agents.md#2-ai-agent-core-components) |
| Giải thích Chain-of-Thought và ReAct, bao gồm vai trò của kết quả quan sát. | [Các mẫu suy luận](01-introduction-to-ai-agents.md#3-reasoning-patterns) |
| Nhận diện rủi ro và đặt guardrail tại các bước phù hợp. | [An toàn và guardrail](01-introduction-to-ai-agents.md#5-safety--guardrails) |

## LangChain for AI Agents

| Mục tiêu ôn tập | Nội dung trong repo |
| --- | --- |
| Giải thích vai trò của chat model, prompt, tool và agent. | [Các thành phần LangChain](02-langchain-for-ai-agents.md#1-introduction-to-langchain) · [Định nghĩa tool và agent](02-langchain-for-ai-agents.md#2-build-your-first-agent-using-langchain) |
| Dùng prompt, chain và tool để xây dựng agent. | [Ví dụ Python](02-langchain-for-ai-agents.md#thực-hành-với-prompt-chain-và-tool) |
| Theo dõi lượt gọi mô hình, thực thi hàm và kết quả tool quay lại mô hình. | [Luồng thực thi LangChain](02-langchain-for-ai-agents.md#3-langchain-agent-under-the-hood) |

## Model Context Protocol (MCP) Fundamentals

| Mục tiêu ôn tập | Nội dung trong repo |
| --- | --- |
| Giải thích cách MCP chuẩn hóa kết nối với hệ thống và tool bên ngoài. | [Vai trò của MCP](03-introduction-to-mcp.md#1-what-is-model-context-protocol) |
| Mô tả vai trò của host, client, server, tools, resources và prompts. | [Các thành phần MCP](03-introduction-to-mcp.md#2-mcp-core-components) |
| Đọc thông điệp JSON-RPC 2.0 và phân biệt stdio với Streamable HTTP. | [Thông điệp và transport](03-introduction-to-mcp.md#messages-and-transports) |
| Tích hợp MCP server vào luồng agent và kiểm tra khám phá, gọi tool. | [Lab MCP và LangChain](03-introduction-to-mcp.md#tích-hợp-server-toán-học-vào-langchain) |

## OpenAI Responses API and Agents SDK

| Mục tiêu ôn tập | Nội dung trong repo |
| --- | --- |
| Giải thích cách Responses API hỗ trợ trạng thái hội thoại và gọi tool. | [Responses API](04-openai-responses-api-and-agents-sdk.md#2-openai-responses-api) |
| Giải thích vai trò của Agent, Runner, Tool, Handoffs và Guardrails. | [Agent và Runner](04-openai-responses-api-and-agents-sdk.md#3-openai-agents-sdk) · [Tool](04-openai-responses-api-and-agents-sdk.md#4-tools-and-function-calling) · [Handoff](04-openai-responses-api-and-agents-sdk.md#5-multi-agent-systems-with-handoffs) · [Guardrail](04-openai-responses-api-and-agents-sdk.md#6-guardrails-and-safety) |
| Đăng ký hàm và dùng Runner thực thi tool do mô hình chọn. | [Ví dụ gọi hàm qua SDK](04-openai-responses-api-and-agents-sdk.md#thực-hành-gọi-hàm-qua-runner) |
| Phân biệt manager pattern với handoff và giải thích cách phân luồng đến agent chuyên trách. | [Mẫu nhiều agent](04-openai-responses-api-and-agents-sdk.md#5-multi-agent-systems-with-handoffs) |
| Chọn guardrail cho yêu cầu, câu trả lời và từng lời gọi function tool. | [Các điểm kiểm tra](04-openai-responses-api-and-agents-sdk.md#6-guardrails-and-safety) |

## OCI Enterprise AI Agents

| Mục tiêu ôn tập | Nội dung trong repo |
| --- | --- |
| Xác định dịch vụ OCI hỗ trợ phát triển, triển khai và quản trị agent. | [Nền tảng OCI Enterprise AI](05-agentic-ai-for-enterprises.md#2-introduction-to-oci-enterprise-ai-platform) |
| Giải thích cách OCI hỗ trợ xây dựng, điều phối và thực thi agent. | [Responses API, Hosted Applications và mô hình kết hợp](05-agentic-ai-for-enterprises.md#3-introduction-to-oci-enterprise-ai-agents) |
| Mô tả Responses API, các tool, bộ nhớ và vector store. | [Các thành phần Enterprise AI Agents](05-agentic-ai-for-enterprises.md#4-oci-enterprise-ai-agents-building-blocks) |
| Cấu hình dự án và chạy agent cơ bản qua OCI Responses API. | [Agent toán học trên OCI](05-agentic-ai-for-enterprises.md#chạy-agent-toán-học-qua-oci-responses-api) |
| Giải thích lựa chọn triển khai và cấu hình mở rộng runtime. | [Triển khai và autoscaling](05-agentic-ai-for-enterprises.md#6-oci-enterprise-ai-agents--deploy-and-scale) |

## Agentic AI for Oracle AI Database

| Mục tiêu ôn tập | Nội dung trong repo |
| --- | --- |
| Giải thích vai trò của Vector Search, Select AI và MCP đối với agent dùng dữ liệu Oracle. | [Các tính năng agentic AI trong Oracle AI Database](06-agentic-ai-for-oracle-ai-database.md#1-agentic-ai-for-oracle-ai-database) |
| Mô tả kiểu VECTOR, embedding và tìm kiếm tương đồng. | [Khái niệm Vector Search](06-agentic-ai-for-oracle-ai-database.md#2-introduction-to-oracle-ai-vector-search) · [Kiểu VECTOR và các metric](06-agentic-ai-for-oracle-ai-database.md#3-oracle-ai-vector-search-workflow) |
| Theo dõi quy trình từ chia tài liệu, tạo embedding đến xếp hạng và truy xuất. | [Quy trình Vector Search](06-agentic-ai-for-oracle-ai-database.md#3-oracle-ai-vector-search-workflow) |
| Truy xuất hàng liên quan bằng SQL và dùng kết quả làm căn cứ cho câu trả lời. | [SQL và luồng grounding](06-agentic-ai-for-oracle-ai-database.md#dùng-kết-quả-truy-xuất-để-tạo-câu-trả-lời) |
| Giải thích cách tạo và chạy thử agent không cần viết code bằng Private Agent Factory. | [Private Agent Factory và Agent Builder](06-agentic-ai-for-oracle-ai-database.md#5-introduction-to-oracle-ai-database-private-agent-factory) |
| Giải thích cách Select AI chuyển câu hỏi ngôn ngữ tự nhiên thành SQL hoặc câu trả lời. | [AI profile, SHOWSQL, RUNSQL và NARRATE](06-agentic-ai-for-oracle-ai-database.md#hỏi-dữ-liệu-bằng-select-ai) |
| Giải thích cách MCP client khám phá và gọi tool do Autonomous AI Database cung cấp. | [Autonomous AI Database MCP Server](06-agentic-ai-for-oracle-ai-database.md#7-oracle-autonomous-ai-database-mcp-server) |

[Kết quả và cách chạy lab](../labs/README.md) · [Mục lục kho tri thức](README.md)

## Đối chiếu 40 câu thi thử

Số câu theo thứ tự ở màn hình Review của [Practice Exam trên Oracle MyLearn](https://mylearn.oracle.com/ou/course/practice-exam-oracle-agentic-ai-associate-certification/163247/271346). Cột cuối ghi nhận phần ghi chú đã đủ hoặc đã được bổ sung chi tiết sau khi xem bài thi thử. Các ý cần nhớ được in đậm trong module.

| Câu | Kiến thức cần ôn | Vị trí trong kho tri thức | Đối chiếu |
| ---: | --- | --- | --- |
| 1 | Transport của Autonomous AI Database MCP Server | [Module 06 §7](06-agentic-ai-for-oracle-ai-database.md#7-oracle-autonomous-ai-database-mcp-server) | Có sẵn |
| 2 | Type hint và schema tham số tool LangChain | [Module 02 §2](02-langchain-for-ai-agents.md#2-build-your-first-agent-using-langchain) | Có sẵn |
| 3 | Code Interpreter và môi trường Python cô lập | [Module 05 §4](05-agentic-ai-for-enterprises.md#4-oci-enterprise-ai-agents-building-blocks) | Có sẵn |
| 4 | Vì sao phòng thủ chiều sâu giảm rủi ro | [Module 01 §5](01-introduction-to-ai-agents.md#5-safety--guardrails) | **Bổ sung** |
| 5 | Tính tự chủ khi agent chọn hành động kế tiếp | [Module 01 §1](01-introduction-to-ai-agents.md#1-what-is-an-ai-agent) | Có sẵn |
| 6 | Định tuyến tool trùng tên theo MCP server nguồn | [Module 03 §3](03-introduction-to-mcp.md#3-add-mcp-server-to-your-first-agent) | **Bổ sung** |
| 7 | LLM, tool và vòng lặp điều phối | [Module 01 §1–2](01-introduction-to-ai-agents.md#1-what-is-an-ai-agent) | Có sẵn |
| 8 | Xác thực và định tuyến yêu cầu của runtime | [Module 05 §1](05-agentic-ai-for-enterprises.md#1-need-for-agent-lifecycle-and-runtime) | Có sẵn |
| 9 | Các khả năng agentic AI của Oracle AI Database | [Module 06 §1](06-agentic-ai-for-oracle-ai-database.md#1-agentic-ai-for-oracle-ai-database) | Có sẵn |
| 10 | Guardrail dùng hàm kiểm tra hoặc agent phụ | [Module 04 §6](04-openai-responses-api-and-agents-sdk.md#6-guardrails-and-safety) | **Bổ sung** |
| 11 | Dự án Generative AI khi dùng OCI Responses API | [Module 05 §5](05-agentic-ai-for-enterprises.md#5-getting-started-with-oci-enterprise-ai-agents) | Có sẵn |
| 12 | Kết quả cuối từ Runner | [Module 04 §3](04-openai-responses-api-and-agents-sdk.md#3-openai-agents-sdk) | Có sẵn |
| 13 | Suy luận được quản lý của OCI Enterprise AI Models | [Module 05 §2](05-agentic-ai-for-enterprises.md#2-introduction-to-oci-enterprise-ai-platform) | Có sẵn |
| 14 | Ba nhóm tool trong Select AI Agent | [Module 06 §6](06-agentic-ai-for-oracle-ai-database.md#điều-phối-tác-vụ-bằng-select-ai-agent) | Có sẵn |
| 15 | Tài nguyên và vận hành hosted agent do OCI quản lý | [Module 05 §3](05-agentic-ai-for-enterprises.md#3-introduction-to-oci-enterprise-ai-agents) | Có sẵn |
| 16 | Container image và OCI Container Registry | [Module 05 §6](05-agentic-ai-for-enterprises.md#6-oci-enterprise-ai-agents--deploy-and-scale) | Có sẵn |
| 17 | Danh sách handoff và quyền tiếp quản | [Module 04 §5](04-openai-responses-api-and-agents-sdk.md#5-multi-agent-systems-with-handoffs) | Có sẵn |
| 18 | Khởi chạy MCP server qua stdio | [Module 03 §3, lab toán học](03-introduction-to-mcp.md#tích-hợp-server-toán-học-vào-langchain) | **Bổ sung** |
| 19 | Hosted tools, function tools và agents as tools | [Module 04 §4](04-openai-responses-api-and-agents-sdk.md#4-tools-and-function-calling) | Có sẵn |
| 20 | MCP prompts là mẫu tương tác dùng lại | [Module 03 §2](03-introduction-to-mcp.md#2-mcp-core-components) | Có sẵn |
| 21 | Chỉ mục lai dùng vector và từ khóa | [Module 06 §3](06-agentic-ai-for-oracle-ai-database.md#3-oracle-ai-vector-search-workflow) | **Bổ sung** |
| 22 | RAG và NL2SQL trong Select AI Agent | [Module 06 §6](06-agentic-ai-for-oracle-ai-database.md#điều-phối-tác-vụ-bằng-select-ai-agent) | Có sẵn |
| 23 | Chatbot, workflow theo quy tắc và AI agent | [Module 01 §1](01-introduction-to-ai-agents.md#1-what-is-an-ai-agent) | Có sẵn |
| 24 | Tripwire dừng lượt chạy và phát sinh ngoại lệ | [Module 04 §6](04-openai-responses-api-and-agents-sdk.md#6-guardrails-and-safety) | **Bổ sung** |
| 25 | Chọn, gọi và xử lý kết quả tool | [Module 01 §2](01-introduction-to-ai-agents.md#2-ai-agent-core-components) | Có sẵn |
| 26 | Vector Stores API và truy xuất theo ngữ nghĩa | [Module 05 §4, Vector Stores](05-agentic-ai-for-enterprises.md#files-vector-stores-và-containers) | Có sẵn |
| 27 | Framework Select AI Agent trong cơ sở dữ liệu | [Module 06 §6](06-agentic-ai-for-oracle-ai-database.md#điều-phối-tác-vụ-bằng-select-ai-agent) | Có sẵn |
| 28 | Đọc văn bản từ Responses API và Chat Completions | [Module 04 §2](04-openai-responses-api-and-agents-sdk.md#2-openai-responses-api) | **Bổ sung** |
| 29 | Container, Podman và Podman Compose | [Module 06 §5](06-agentic-ai-for-oracle-ai-database.md#5-introduction-to-oracle-ai-database-private-agent-factory) | **Bổ sung** |
| 30 | Knowledge Agent và Data Analysis Agent trong khóa học | [Module 06 §5](06-agentic-ai-for-oracle-ai-database.md#5-introduction-to-oracle-ai-database-private-agent-factory) | Có sẵn |
| 31 | Truy xuất và đưa các đoạn văn bản vào ngữ cảnh LLM | [Module 06 §4, grounding](06-agentic-ai-for-oracle-ai-database.md#dùng-kết-quả-truy-xuất-để-tạo-câu-trả-lời) | Có sẵn |
| 32 | Endpoint, xác thực và project khi dùng OpenAI SDK với OCI | [Module 05 §5](05-agentic-ai-for-enterprises.md#5-getting-started-with-oci-enterprise-ai-agents) | Có sẵn |
| 33 | Vai trò của framework và managed runtime | [Module 05 §1](05-agentic-ai-for-enterprises.md#1-need-for-agent-lifecycle-and-runtime) | Có sẵn |
| 34 | Chuỗi trích văn bản, chia đoạn và tạo embedding | [Module 06 §3](06-agentic-ai-for-oracle-ai-database.md#3-oracle-ai-vector-search-workflow) | **Bổ sung** |
| 35 | MCP chuẩn hóa kết nối với tool và dữ liệu | [Module 03 §1](03-introduction-to-mcp.md#1-what-is-model-context-protocol) | Có sẵn |
| 36 | Bộ nhớ ngắn hạn trong một phiên hội thoại OCI | [Module 05 §4, bộ nhớ](05-agentic-ai-for-enterprises.md#trạng-thái-hội-thoại-và-bộ-nhớ) | Có sẵn |
| 37 | Output parser trong LangChain | [Module 02 §1, LCEL](02-langchain-for-ai-agents.md#prompt-templates-and-lcel) | **Bổ sung** |
| 38 | Điều phối tập trung bằng Manager pattern | [Module 04 §5](04-openai-responses-api-and-agents-sdk.md#5-multi-agent-systems-with-handoffs) | Có sẵn |
| 39 | Trường `instructions` trong định nghĩa Agent | [Module 04 §3](04-openai-responses-api-and-agents-sdk.md#3-openai-agents-sdk) | **Bổ sung** |
| 40 | Định dạng phần tử của kiểu `VECTOR` | [Module 06 §3](06-agentic-ai-for-oracle-ai-database.md#3-oracle-ai-vector-search-workflow) | Có sẵn |
