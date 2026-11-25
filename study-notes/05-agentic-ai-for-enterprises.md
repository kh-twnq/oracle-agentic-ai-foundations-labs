# Agentic AI for Enterprises

Module 5 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), trang 163–195 · [Mục lục](README.md)

Agent code mô tả việc chọn bước, gọi tools và tạo kết quả. Khi đưa lên production, agent cần runtime để nhận requests, thực thi, giữ state, kết nối hệ thống và theo dõi lỗi. Guide dùng OCI Enterprise AI để minh họa cách cung cấp những khả năng này. (trang 163–168)

## Agent Lifecycle và Runtime Architecture

Agent stack gồm **User / Application**, **Runtime Architecture** và **Agent Logic**. Lifecycle bao gồm phát triển, kiểm thử, deploy, vận hành và cập nhật. Runtime xử lý các trách nhiệm trong từng lượt chạy. (trang 165–171)

| Runtime capability | Trách nhiệm |
| --- | --- |
| **Request Handling** | Nhận request, xác thực, giới hạn tần suất và route đến agent. |
| **Execution Environment** | Cấp môi trường như server, container hoặc serverless để chạy agent. |
| **Orchestration & State** | Quản lý sessions, memory, các bước và retry khi phù hợp. |
| **Tool Sandbox** | Giới hạn phạm vi và tài nguyên mà tools có thể dùng. |
| **Integrations** | Kết nối APIs, databases và credentials tương ứng. |
| **Scaling & Reliability** | Xử lý tải tăng, cân bằng tải và failover. |
| **Observability** | Ghi logs, metrics và traces để theo dõi và debug. |

Với self-managed runtime, đội phát triển lắp ghép các thành phần này. Với managed runtime, nền tảng cung cấp các phần phù hợp với cách triển khai đã chọn. (trang 169–171)

## OCI Enterprise AI Platform

OCI Enterprise AI kết hợp **Models** để dùng model, **Agents** để điều phối và thực thi, và **Governance** để kiểm soát mạng, danh tính và hành vi. (trang 172–177)

![OCI Enterprise AI kết hợp Models, Agents và Governance, với lựa chọn OCI Responses API hoặc hosted application.](images/05-oci-enterprise-ai.png)

| Model type | Vai trò trong workflow |
| --- | --- |
| **Chat** | Xử lý hội thoại, reasoning, tạo nội dung hoặc chọn tool. |
| **Embed** | Chuyển dữ liệu thành vectors dùng cho semantic search và retrieval. |
| **Rerank** | Chấm mức liên quan của các candidates theo query và sắp lại kết quả. |

Guide dùng **On-Demand** cho capacity chia sẻ và tải biến động. **Dedicated AI Cluster** dành capacity riêng cho tenancy, phù hợp khi cần isolation, latency ổn định hoặc triển khai model tùy chỉnh theo khả năng dịch vụ. Hai cách tính chi phí trong Guide dựa trên usage hoặc thời gian cấp cluster. (trang 174–176)

Governance gồm **Network Security** với Private Endpoints và Zero Trust Packet Routing (ZPR), **Identity Control** với IAM policies theo tenancy hoặc compartment, và **AI Behavior** với guardrails. Các kiểm tra hành vi gồm content moderation, prompt injection defense và PII detection. (trang 177)

## OCI Enterprise AI Agents

Guide trình bày hai cách dùng managed runtime. Với **OCI Responses API**, application chạy trong môi trường của mình và gọi service để dùng model, state và tools. Với **Hosted Agentic Apps**, OCI chạy container chứa agent logic và framework do đội phát triển lựa chọn. OCI có thể cung cấp endpoint, scaling và các thiết lập vận hành cho deployment. Đội phát triển vẫn định nghĩa instructions, tools, nguồn tri thức và mục tiêu nghiệp vụ. (trang 178–181)

### Agent building blocks

**OCI Responses API** dùng interface tương thích OpenAI và hỗ trợ tool reasoning, multi-model routing cùng conversation state. Nhóm tools trong Guide gồm **File Search** để truy xuất tài liệu, **Code Interpreter** để chạy Python trong sandbox, **Function Calling** để gọi business functions và **MCP Calling** để kết nối server MCP. (trang 182–184)

| Memory capability | Phạm vi |
| --- | --- |
| **Short-term memory** | Conversations API quản lý state giữa các lượt trong một conversation. |
| **Long-term memory** | Duy trì context qua nhiều sessions theo `subject_id` trong một project. |
| **Context compaction** | Rút gọn history khi conversation dài để giảm phần context phải xử lý. |

**Files API** quản lý file, **Vector Stores API** hỗ trợ chunking, embedding, retrieval và metadata filtering, còn **Containers API** cung cấp execution environment cho workload cần cách ly. (trang 185–186)

## Authentication, first request và deployment

Để gọi OCI Responses API, Guide chuẩn bị OCI account, compartment, Generative AI project, region, model identifier và quyền truy cập. Hai hướng xác thực được minh họa là **Generative AI API Key** và **OCI IAM request signing**. Chọn client configuration theo hướng đang dùng. (trang 187–189)

Ví dụ dùng OpenAI Python SDK đặt `base_url` thành endpoint OCI của region, gửi Generative AI project OCID trong header `OpenAI-Project`, rồi gọi `client.responses.create()` với model trên OCI. Kết quả text lấy qua `output_text`. Cú pháp gọi giống ví dụ OpenAI, với endpoint, authentication, model và project của OCI. (trang 190–191)

Với **Hosted Agentic Apps**, flow trong Guide là **Build → Package → Upload → Configure → Deploy → Invoke**. Chạy thử agent, đóng gói dependencies thành image, đưa image lên OCI Container Registry (OCIR), cấu hình Generative AI Application về identity, network, storage và scaling, rồi deploy và gọi HTTP endpoint. Với hướng **OCI Responses API**, application gọi managed API từ hạ tầng hiện có. (trang 192–195) [Hướng dẫn chạy lab](../labs/README.md)
