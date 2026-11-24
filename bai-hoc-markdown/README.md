# Oracle Agentic AI Foundations

Bộ ghi chú gồm 32 bài thuộc 6 mô-đun của workshop. Nội dung giải thích bằng tiếng Việt và giữ thuật ngữ như Agent Execution Loop, tool calling, handoff, guardrail và Vector Search, cùng tên API, method và product. Dùng số trang để đối chiếu slide và speaker notes trong Student Guide. Các bài lab có liên kết tới mã công khai tương ứng của Oracle University.

Các bài có 27 sơ đồ minh họa được vẽ lại từ phần kiến trúc và workflow của guide. Nhãn trong hình giữ thuật ngữ tiếng Anh. Mỗi hình có chú thích và số trang để đối chiếu.

[Oracle Agentic AI Foundations: Hands-on Workshop (Student Guide), D1114464GC10](https://mylearn.oracle.com/ou/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course)

[Mã lab công khai của Oracle University](https://github.com/oracle-university-labs/ou-generativeai-pro/tree/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations)

## 01. Nhập môn AI agent

Oracle Student Guide, trang 9–54.

- [01. AI agent và Agent Execution Loop](01-01-what-is-an-ai-agent.md) · trang 11–16
- [02. Agent Core Components](01-02-core-components.md) · trang 17–21
- [03. Reasoning Patterns với CoT, ReAct và ToT](01-03-reasoning-patterns.md) · trang 22–27
- [04. Xây dựng AI agent đầu tiên](01-04-first-agent.md) · trang 28–45
- [05. Threat Model và Guardrails cho AI agent](01-05-safety-and-guardrails.md) · trang 46–52

**Ôn tập**, trang 53–54. Phân biệt vai trò LLM, tools và orchestration. Dùng ReAct trace để giải thích vì sao agent gọi tool, quan sát rồi quyết định tiếp tục hay dừng. Xác định lớp guardrail cần thiết cho mỗi rủi ro.

## 02. LangChain cho AI agent

Oracle Student Guide, trang 55–89.

- [01. Các khối xây dựng của LangChain](02-01-langchain-building-blocks.md) · trang 57–62
- [02. Xây LangChain agent với tool calling](02-02-build-langchain-agent.md) · trang 63–72
- [03. LangChain agent loop từ request đến final output](02-03-langchain-agent-under-the-hood.md) · trang 73–88

**Ôn tập**, trang 89. Theo dõi input đi qua prompt, model và parser trong chain. Với agent, kiểm tra tool schema, tool call, tool result và conversation state trước khi đọc final answer.

## 03. Model Context Protocol (MCP)

Oracle Student Guide, trang 91–121.

- [01. Model Context Protocol là gì?](03-01-what-is-mcp.md) · trang 93–96
- [02. MCP Primitives, Connection Lifecycle và JSON-RPC](03-02-mcp-core-components.md) · trang 97–103
- [03. Kết nối agent đầu tiên với MCP server](03-03-add-mcp-to-agent.md) · trang 104–115
- [04. Thực hành MCP với dữ liệu sử dụng OCI](03-04-oci-usage-mcp.md) · trang 116–120

**Ôn tập**, trang 121. Giải thích từng vai trò host, client và server. Phân biệt discovery qua `tools/list` với execution qua `tools/call`. Xác định tool chạy tại local server hay truy cập downstream service.

## 04. OpenAI Responses API và Agents SDK

Oracle Student Guide, trang 123–162.

- [01. Responses API và Agents SDK trong ứng dụng](04-01-openai-agent-stack.md) · trang 125–129
- [02. Responses API, Conversation Chaining và Hosted Tools](04-02-responses-api.md) · trang 130–135
- [03. Khởi tạo và chạy agent bằng Agents SDK](04-03-agents-sdk.md) · trang 136–141
- [04. Hosted Tools, Function Tools và Agents as Tools](04-04-tools-and-function-calling.md) · trang 142–148
- [05. Multi-agent orchestration với Handoffs](04-05-multi-agent-handoffs.md) · trang 149–152
- [06. Guardrails và tracing trong Agents SDK](04-06-guardrails-and-tracing.md) · trang 153–156
- [07. Bài tổng hợp về agent hỗ trợ khách hàng](04-07-customer-support-agent.md) · trang 157–161

**Ôn tập**, trang 162. Chọn Responses API hoặc Agents SDK theo phần orchestration application muốn nắm. Dùng function tools, handoffs, guardrails và tracing để kiểm tra cả hành vi của agent lẫn business rules.

## 05. Agentic AI trên Oracle Cloud Infrastructure

Oracle Student Guide, trang 163–195.

- [01. Agent Lifecycle và Runtime Architecture](05-01-agent-runtime.md) · trang 165–171
- [02. Nền tảng OCI Enterprise AI](05-02-oci-enterprise-ai-platform.md) · trang 172–177
- [03. OCI Responses API và Hosted Agentic Apps](05-03-oci-enterprise-ai-agents.md) · trang 178–181
- [04. OCI Agent Building Blocks](05-04-oci-agent-building-blocks.md) · trang 182–186
- [05. Gọi OCI Responses API lần đầu](05-05-first-oci-agent.md) · trang 187–191
- [06. Deploy và scale OCI agent](05-06-deploy-and-scale-oci-agents.md) · trang 192–194

**Ôn tập**, trang 195. Xác định trách nhiệm thuộc agent logic, runtime và governance. Phân biệt managed OCI Responses API với hosted application đóng gói thành container.

## 06. Agentic AI trên Oracle AI Database

Oracle Student Guide, trang 197–241.

- [01. Tổng quan agentic AI trên Oracle AI Database](06-01-agentic-ai-database.md) · trang 199–200
- [02. Cơ bản về Oracle AI Vector Search](06-02-introduction-vector-search.md) · trang 201–205
- [03. Vector Search Workflow, Embeddings và Distance Metrics](06-03-vector-search-workflow.md) · trang 206–211
- [04. Oracle AI Vector Search Demo với Python và SQL](06-04-vector-search-demo.md) · trang 212–222
- [05. Xây agent bằng Private Agent Factory](06-05-private-agent-factory.md) · trang 223–228
- [06. Select AI Agent và Customer Return Workflow](06-06-select-ai-agent.md) · trang 229–234
- [07. MCP server tích hợp trong Autonomous AI Database](06-07-autonomous-db-mcp-server.md) · trang 235–240

**Ôn tập**, trang 241. Ghép đúng nhu cầu với Vector Search, Private Agent Factory, Select AI Agent hoặc Autonomous AI Database MCP Server. Theo dõi quyền dữ liệu từ user đến query hoặc tool thực thi.

Trong mô-đun MCP, slide ở trang 116 lặp số 03. Mục lục này đánh số 04 cho bài thực hành OCI Usage MCP theo thứ tự xuất hiện.
