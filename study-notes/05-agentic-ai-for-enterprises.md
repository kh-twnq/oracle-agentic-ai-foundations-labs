# Agentic AI for Enterprises

*Agentic AI cho doanh nghiệp*

Module 5 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), tr. 163–195 · [Mục lục](README.md)

## Agenda

*Nội dung học*

1. [Vì sao cần quản lý vòng đời và runtime của agent?](#1-need-for-agent-lifecycle-and-runtime)
2. [Giới thiệu về nền tảng OCI Enterprise AI](#2-introduction-to-oci-enterprise-ai-platform)
3. [Giới thiệu về OCI Enterprise AI Agents](#3-introduction-to-oci-enterprise-ai-agents)
4. [Các thành phần của OCI Enterprise AI Agents](#4-oci-enterprise-ai-agents-building-blocks)
5. [Bắt đầu với OCI Enterprise AI Agents](#5-getting-started-with-oci-enterprise-ai-agents)
6. [Triển khai và mở rộng OCI Enterprise AI Agents](#6-oci-enterprise-ai-agents--deploy-and-scale)

Nội dung theo chương trình học ở tr. 164 của Student Guide.

<a name="1-need-for-agent-lifecycle-and-runtime"></a>

## 1. Vì sao cần quản lý vòng đời và runtime của agent?

**Logic của agent** quyết định agent nên làm gì. **Runtime của agent** cung cấp môi trường để chạy logic đó. **Ứng dụng** gửi đầu vào và sử dụng kết quả. Vòng đời gồm phát triển, kiểm thử, triển khai, vận hành và chỉnh sửa. (tr. 165–168)

| Khả năng của runtime | Trách nhiệm |
| --- | --- |
| Xử lý yêu cầu | Tiếp nhận, xác thực, giới hạn tần suất và định tuyến yêu cầu. |
| Môi trường thực thi | Chạy agent trên máy chủ, trong container hoặc trong môi trường serverless. |
| Điều phối và trạng thái | Điều phối các bước, phiên, bộ nhớ và các lần thử lại. |
| Sandbox cho tool | Cô lập quá trình thực thi và giới hạn tài nguyên. |
| Tích hợp | Quản lý kết nối đến API và cơ sở dữ liệu, cùng thông tin xác thực. |
| Mở rộng và độ tin cậy | Đáp ứng nhu cầu tải, cân bằng tải và chuyển đổi dự phòng khi có lỗi. |
| Khả năng quan sát | Thu thập log, số liệu đo lường và trace. |

Nhóm có thể tự vận hành các thành phần này hoặc dùng runtime được quản lý. Nhóm phụ trách ứng dụng xác định chỉ dẫn, quyền và quy tắc nghiệp vụ. (tr. 169–171, 178–181)

<a name="2-introduction-to-oci-enterprise-ai-platform"></a>

## 2. Giới thiệu về nền tảng OCI Enterprise AI

OCI Enterprise AI kết hợp **mô hình (Models)** để xử lý thông tin, **agent (Agents)** để điều phối và thực thi, cùng **quản trị (Governance)** để kiểm soát quyền truy cập và hành vi. (tr. 172–177)

![OCI Enterprise AI kết hợp mô hình, agent và quản trị.](images/05-oci-enterprise-ai.png)

| Loại mô hình | Chức năng chính |
| --- | --- |
| **Chat** | Tạo phản hồi hoặc đề xuất một lời gọi tool. |
| **Embed** | Chuyển đầu vào thành vector dùng để truy xuất. |
| **Rerank** | Chấm điểm các kết quả đã truy xuất và sắp xếp lại theo mức độ liên quan. |

**On-Demand** sử dụng tài nguyên xử lý dùng chung và phù hợp khi mức sử dụng thay đổi. **Dedicated AI Cluster** dành riêng năng lực xử lý cho một tenancy. Lựa chọn này phù hợp với tải công việc cần môi trường cô lập, độ trễ có thể dự đoán hoặc mô hình tùy chỉnh đủ điều kiện. Hai lựa chọn có cam kết khác nhau về năng lực xử lý và chi phí. (tr. 174–176)

Các biện pháp kiểm soát mạng gồm Private Endpoints và Zero Trust Packet Routing (ZPR). Chính sách Identity and Access Management (IAM) quản lý quyền truy cập tài nguyên. Guardrail hỗ trợ kiểm duyệt nội dung và xử lý prompt injection cũng như thông tin nhận dạng cá nhân (PII). (tr. 177)

<a name="3-introduction-to-oci-enterprise-ai-agents"></a>

## 3. Giới thiệu về OCI Enterprise AI Agents

OCI Enterprise AI Agents cung cấp hai cách chạy tải công việc của agent trên dịch vụ được quản lý. (tr. 178–181)

| Lựa chọn | Logic ứng dụng chạy ở đâu? | OCI cung cấp gì? |
| --- | --- | --- |
| **OCI Responses API** | Trong môi trường riêng của nhóm phụ trách ứng dụng. | API được quản lý cho mô hình, các tool được hỗ trợ và trạng thái hội thoại. |
| **Hosted Agentic Apps** | Trong container chạy trên hạ tầng do OCI quản lý. | Một endpoint cho ứng dụng và hạ tầng được quản lý theo cấu hình triển khai. |

<a name="4-oci-enterprise-ai-agents-building-blocks"></a>

## 4. Các thành phần của OCI Enterprise AI Agents

OCI Responses API cung cấp giao diện tương thích OpenAI để định tuyến đến mô hình, suy luận về cách dùng tool và quản lý trạng thái. File Search truy xuất nội dung tài liệu. Code Interpreter chạy Python trong sandbox. Function Calling yêu cầu gọi hàm do ứng dụng cung cấp. MCP Calling kết nối với MCP server. (tr. 182–184)

| Tính năng trạng thái hoặc bộ nhớ | Phạm vi |
| --- | --- |
| **Bộ nhớ ngắn hạn** | Ngữ cảnh qua nhiều lượt trong cùng một cuộc hội thoại, được quản lý qua Conversations API. |
| **Bộ nhớ dài hạn** | Ngữ cảnh qua nhiều phiên, gắn với một `subject_id` trong dự án. |
| **Nén ngữ cảnh** | Biểu diễn lịch sử dài dưới dạng ngắn hơn để giảm lượng ngữ cảnh mà mô hình phải xử lý. |

Files API quản lý các đối tượng file. Vector Stores API hỗ trợ chia đoạn, tạo embedding, truy xuất và lọc theo siêu dữ liệu. Containers API cung cấp môi trường thực thi cô lập. (tr. 185–186)

<a name="5-getting-started-with-oci-enterprise-ai-agents"></a>

## 5. Bắt đầu với OCI Enterprise AI Agents

Có thể xác thực với OCI bằng **Generative AI API Key** hoặc **ký yêu cầu bằng OCI IAM**. Trong giao diện tương thích OpenAI, `base_url` xác định endpoint theo vùng. Định danh mô hình dùng để chọn mô hình. Header `OpenAI-Project` xác định dự án Generative AI bằng định danh tài nguyên OCI (OCID) của dự án. `client.responses.create()` dùng cấu hình này để gửi yêu cầu tới mô hình. (tr. 187–191)

<a name="6-oci-enterprise-ai-agents--deploy-and-scale"></a>

## 6. Triển khai và mở rộng OCI Enterprise AI Agents

Khi triển khai trên OCI, logic của agent và các gói phụ thuộc được đóng gói thành container image. OCI Container Registry lưu image này. Cấu hình triển khai quy định định danh, mạng, lưu trữ và cách mở rộng. Endpoint được quản lý chuyển yêu cầu đến phiên bản ứng dụng đã triển khai. (tr. 192–195)
