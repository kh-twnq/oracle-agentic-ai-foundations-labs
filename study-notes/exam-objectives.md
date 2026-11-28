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
