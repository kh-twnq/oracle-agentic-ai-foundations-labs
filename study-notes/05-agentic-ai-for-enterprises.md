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

Nội dung theo chương trình học ở tr. 164 của Student Guide. Xem [Ôn tập Module 5](#module-review) để luyện các câu hỏi biến thể.

<a name="1-need-for-agent-lifecycle-and-runtime"></a>

## 1. Vì sao cần quản lý vòng đời và runtime của agent?

**Logic của agent** quyết định agent nên làm gì. **Runtime của agent** cung cấp môi trường để chạy logic đó. **Ứng dụng** gửi đầu vào và sử dụng kết quả. Vòng đời gồm phát triển, kiểm thử, triển khai, vận hành và chỉnh sửa. (tr. 165–168)

| Khả năng của runtime | Trách nhiệm |
| --- | --- |
| Xử lý yêu cầu | Tiếp nhận, xác thực, giới hạn tần suất và định tuyến yêu cầu. |
| Môi trường thực thi | Chạy agent trên máy chủ, trong container hoặc trong môi trường serverless. |
| Điều phối và trạng thái | Điều phối các bước, phiên, bộ nhớ và các lần thử lại. |
| Sandbox cho tool | **Cô lập quá trình chạy tool khỏi môi trường host** và giới hạn tài nguyên tool có thể sử dụng. |
| Tích hợp | Quản lý kết nối đến API và cơ sở dữ liệu, cùng thông tin xác thực. |
| Mở rộng và độ tin cậy | Đáp ứng nhu cầu tải, cân bằng tải và chuyển đổi dự phòng khi có lỗi. |
| Khả năng quan sát | Thu thập log, số liệu đo lường và trace. |

Sandbox có thể tách không gian tiến trình, hệ thống file và cấu hình mạng của tác vụ khỏi host. Ví dụ, agent có thể phân tích một file CSV trong sandbox và lấy báo cáo đầu ra. Quyền truy cập API hoặc dữ liệu bên ngoài vẫn được kiểm soát theo cấu hình và chính sách của ứng dụng. [Tài liệu OCI Enterprise AI Agents](https://docs.oracle.com/en-us/iaas/Content/generative-ai/agents.htm#run-code-in-sandboxes)

Nhóm có thể tự vận hành các thành phần này hoặc dùng runtime được quản lý. Nhóm phụ trách ứng dụng xác định chỉ dẫn, quyền và quy tắc nghiệp vụ. (tr. 169–171, 178–181)

<a name="2-introduction-to-oci-enterprise-ai-platform"></a>

## 2. Giới thiệu về nền tảng OCI Enterprise AI

OCI Enterprise AI kết hợp **mô hình (Models)** để xử lý thông tin, **agent (Agents)** để điều phối và thực thi, cùng **quản trị (Governance)** để kiểm soát quyền truy cập và hành vi. (tr. 172–177)

![OCI Enterprise AI kết hợp mô hình, agent và quản trị.](images/05-oci-enterprise-ai.png)

| Loại mô hình | Chức năng chính |
| --- | --- |
| **Chat** | Tạo phản hồi hoặc đề xuất một lời gọi tool. |
| **Embed** | Chuyển đầu vào thành vector dùng để truy xuất. |
| **Rerank** | **Chấm lại mức độ liên quan của các tài liệu đã truy xuất và sắp xếp lại kết quả.** |

### On-Demand và Dedicated AI Cluster

| Chế độ | Năng lực xử lý | Khi nào phù hợp? |
| --- | --- | --- |
| **On-Demand** | OCI phục vụ mô hình bằng tài nguyên dùng chung. | Thử nghiệm hoặc phục vụ tải thay đổi mà nhóm chưa cần dành riêng năng lực xử lý. |
| **Dedicated AI Cluster** | **Dành riêng năng lực GPU, giúp hiệu năng và độ trễ dễ dự đoán hơn.** | Tải production cần năng lực riêng hoặc cần triển khai mô hình tùy chỉnh đủ điều kiện. |

Ở chế độ Dedicated, ứng dụng gọi endpoint của mô hình được triển khai trên cluster. Khi chọn chế độ, cân nhắc cam kết sử dụng, chi phí và mức hỗ trợ của mô hình theo vùng. Cả hai chế độ đều áp dụng cơ chế xác thực và kiểm soát quyền của OCI. (tr. 174–176) [Các chế độ phục vụ mô hình trên OCI](https://docs.oracle.com/en-us/iaas/Content/generative-ai/modes.htm)

Ở giai đoạn phát triển và kiểm thử, OCI Generative AI cung cấp mô hình chat, embedding, rerank và API để thử agent. Khi triển khai, nhóm có thể dùng Hosted Applications và lưu image trong OCI Container Registry (OCIR). Khi vận hành, IAM, cấu hình mạng và guardrail kiểm soát quyền và hành vi.

Các biện pháp kiểm soát mạng gồm Private Endpoints và Zero Trust Packet Routing (ZPR). Chính sách Identity and Access Management (IAM) quản lý quyền truy cập tài nguyên. Guardrail hỗ trợ kiểm duyệt nội dung và xử lý prompt injection cũng như thông tin nhận dạng cá nhân (PII). (tr. 177)

### Reranking trong RAG

Luồng truy xuất thường gồm `Tạo embedding cho truy vấn → Tìm ứng viên bằng vector search → Rerank → Đưa các đoạn phù hợp nhất vào ngữ cảnh`.

Vector search tìm một nhóm ứng viên dựa trên độ tương đồng giữa các vector. **Reranker chấm mức độ liên quan giữa truy vấn và từng ứng viên đã tìm được**, rồi đưa các kết quả phù hợp hơn lên đầu. Ví dụ, với câu hỏi về thời hạn trả hàng cho đơn quốc tế, vector search có thể tìm nhiều chính sách trả hàng. Reranker ưu tiên đoạn nói cụ thể về đơn quốc tế.

Reranking chỉ xử lý tập ứng viên được đưa vào. Nếu tài liệu đúng bị bỏ sót ở bước tìm kiếm ban đầu, hãy kiểm tra chất lượng truy xuất, bộ lọc hoặc số lượng ứng viên trước khi điều chỉnh reranker. [Rerank trong OCI Generative AI](https://docs.oracle.com/en-us/iaas/Content/generative-ai/rerank.htm)

<a name="3-introduction-to-oci-enterprise-ai-agents"></a>

## 3. Giới thiệu về OCI Enterprise AI Agents

OCI Enterprise AI Agents cung cấp hai cách chạy tải công việc của agent trên dịch vụ được quản lý. (tr. 178–181)

| Lựa chọn | Logic ứng dụng chạy ở đâu? | OCI cung cấp gì? |
| --- | --- | --- |
| **OCI Responses API** | Trong môi trường riêng của nhóm phụ trách ứng dụng. | API được quản lý cho mô hình, các tool được hỗ trợ và trạng thái hội thoại. |
| **Hosted Agentic Apps** | Trong container chạy trên hạ tầng do OCI quản lý. | Một endpoint cho ứng dụng và hạ tầng được quản lý theo cấu hình triển khai. |

Hai cách có thể kết hợp. Một Hosted Agentic App có thể gọi OCI Responses API để tương tác với mô hình, dùng Conversations API để giữ ngữ cảnh và dùng sandbox để xử lý file. [Kiến trúc kết hợp trên OCI](https://docs.oracle.com/en-us/iaas/Content/generative-ai/agents.htm)

<a name="4-oci-enterprise-ai-agents-building-blocks"></a>

## 4. Các thành phần của OCI Enterprise AI Agents

OCI Responses API cung cấp giao diện tương thích OpenAI để định tuyến đến mô hình, suy luận về cách dùng tool và quản lý trạng thái. (tr. 182–184)

| Tool | Vai trò khi thực thi |
| --- | --- |
| **File Search** | OCI truy xuất nội dung từ vector store được chỉ định. |
| **Code Interpreter** | OCI chạy Python trong môi trường cô lập. |
| **Function Calling** | Mô hình yêu cầu gọi hàm. Ứng dụng kiểm tra đối số, thực thi hàm và gửi kết quả về OCI. |
| **MCP Calling** | OCI kết nối MCP server từ xa và gọi các tool được phép. |

Chọn mô hình và vùng có hỗ trợ tool cần dùng. [Tool trong OCI Responses API](https://docs.oracle.com/en-us/iaas/Content/generative-ai/responses-api.htm#use-tools-with-the-responses-api)

### Trạng thái hội thoại và bộ nhớ

| Tính năng trạng thái hoặc bộ nhớ | Phạm vi |
| --- | --- |
| **Bộ nhớ ngắn hạn** | Ngữ cảnh qua nhiều lượt trong cùng một cuộc hội thoại. |
| **Bộ nhớ dài hạn** | Ngữ cảnh qua nhiều phiên, gắn với một `subject_id` trong dự án. |
| **Nén ngữ cảnh** | Biểu diễn lịch sử dài dưới dạng ngắn hơn để giảm lượng ngữ cảnh mà mô hình phải xử lý. |

**Conversations API quản lý lịch sử của cuộc hội thoại nhiều lượt.** Khi tiếp tục dùng cùng một conversation, ứng dụng có thể gửi câu hỏi nối tiếp với ngữ cảnh của những lượt trước. Ví dụ, người dùng hỏi “Đơn `ORD-42` đã giao chưa?” rồi hỏi “Tôi có thể trả đơn đó không?”. Lịch sử giúp agent biết “đơn đó” đang chỉ `ORD-42`. Bộ nhớ dài hạn trong dự án phục vụ nhu cầu giữ thông tin qua nhiều phiên liên quan. [Conversations và memory trên OCI](https://docs.oracle.com/en-us/iaas/Content/generative-ai/agents.htm)

### Files, Vector Stores và Containers

| API | Trách nhiệm |
| --- | --- |
| **Files API** | Quản lý các đối tượng file. |
| **Vector Stores API** | Hỗ trợ chia đoạn, tạo embedding, truy xuất và lọc theo siêu dữ liệu. |
| **Containers API** | **Cung cấp môi trường thực thi cô lập để chạy tác vụ tùy chỉnh**, chẳng hạn xử lý file hoặc chạy mã phân tích dữ liệu. |

Sandbox là môi trường chạy tác vụ. Containers API cung cấp cách làm việc với môi trường đó. Hosted Agentic Apps triển khai **ứng dụng agent** để phục vụ yêu cầu qua endpoint của ứng dụng. Ví dụ, một ứng dụng agent đang chạy có thể dùng một sandbox cho từng tác vụ phân tích file mà nó điều phối. (tr. 185–186) [OCI Containers API](https://docs.oracle.com/en-us/iaas/Content/generative-ai/containers-api.htm)

<a name="5-getting-started-with-oci-enterprise-ai-agents"></a>

## 5. Bắt đầu với OCI Enterprise AI Agents

Có thể xác thực với OCI bằng **Generative AI API Key** hoặc **xác thực dựa trên OCI IAM**. Trong giao diện tương thích OpenAI, `base_url` xác định endpoint theo vùng. Định danh mô hình dùng để chọn mô hình. Header `OpenAI-Project` xác định dự án Generative AI bằng định danh tài nguyên OCI (OCID) của dự án. `client.responses.create()` dùng cấu hình này để gửi yêu cầu tới mô hình. (tr. 187–191)

### Chạy agent toán học qua OCI Responses API

1. Tạo hoặc chọn dự án Generative AI, cấp quyền IAM và chuẩn bị Generative AI API Key. Chọn một vùng và model ID hỗ trợ OCI Responses API và Function Calling. [Thiết lập OCI Responses API](https://docs.oracle.com/en-us/iaas/Content/generative-ai/get-started-agents.htm)
2. Sau khi cài [dependencies của repo](../labs/README.md#reproduce-the-local-runs), đặt `OCI_GENAI_API_KEY`, `REGION`, `MODEL_ID` và `PROJECT_ID` trong môi trường local. Chạy từ thư mục gốc.

   ```sh
   .venv/bin/python labs/oracle-university/agentic-ai-foundations/OCI/oci_first_agent.py
   ```

3. Kiểm tra lời gọi chat đơn giản trước, sau đó xem agent thực hiện các phép tính. Với câu hỏi 42 + 58, tool `add` nhận hai đối số, ứng dụng chạy hàm và gửi `function_call_output` khớp `call_id`. Câu trả lời cuối dùng kết quả 100. Lab dùng `previous_response_id` để tiếp tục lượt gọi. [Mã lab OCI](https://github.com/oracle-university-labs/ou-generativeai-pro/blob/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/OCI/oci_first_agent.py)

Có thể chạy cùng luồng qua [fixture cục bộ](../labs/README.md#results) để kiểm tra vòng gọi tool và chuyển kết quả. Tài khoản OCI có quyền phù hợp cần thiết để xác nhận IAM và inference trên endpoint thật.

<a name="6-oci-enterprise-ai-agents--deploy-and-scale"></a>

## 6. Triển khai và mở rộng OCI Enterprise AI Agents

Khi dùng **OCI Responses API** trực tiếp, OCI vận hành lớp suy luận và các tool được quản lý. Nhóm phụ trách ứng dụng chọn cách chạy và mở rộng mã client, các hàm cục bộ và dịch vụ mà chúng gọi.

Khi dùng **Hosted Applications**, hãy đóng gói logic và các gói phụ thuộc thành container image, đưa image lên OCI Container Registry, rồi tạo ứng dụng và deployment. Ứng dụng quy định xác thực, mạng và lưu trữ. Endpoint phục vụ deployment đang hoạt động. [Triển khai agent trên OCI](https://docs.oracle.com/en-us/iaas/Content/generative-ai/deploying-agents.htm)

Để mở rộng runtime được host, đặt số replica tối thiểu và tối đa, rồi chọn chỉ số autoscaling như số yêu cầu đồng thời, yêu cầu mỗi giây, CPU hoặc bộ nhớ. Ví dụ, số yêu cầu đồng thời có thể phù hợp với agent thường chờ tool truy xuất. Hosted Applications dùng Persistent File Storage hỗ trợ một replica theo tài liệu OCI. Cấu hình replica của ứng dụng và năng lực phục vụ của mô hình là hai quyết định riêng. (tr. 192–195) [Cấu hình Hosted Applications](https://docs.oracle.com/en-us/iaas/Content/generative-ai/applications.htm#scaling)

<a name="module-review"></a>

## Ôn tập Module 5

### Câu 1. Dedicated AI Cluster và On-Demand

Xem [On-Demand và Dedicated AI Cluster](#on-demand-và-dedicated-ai-cluster).

- **Vì sao chọn Dedicated AI Cluster khi cần độ trễ ổn định hơn?** Cluster dành riêng năng lực GPU cho workload, giúp hiệu năng dễ dự đoán hơn.
- **Khi nào On-Demand phù hợp?** Khi nhóm đang thử nghiệm hoặc có tải biến động và muốn gọi mô hình mà chưa cần cấp riêng năng lực GPU.
- **Ứng dụng gọi mô hình chạy ở chế độ Dedicated bằng cách nào?** Gọi endpoint của mô hình đã được triển khai trên cluster.
- **Nhóm còn phải kiểm tra điều gì trước khi chọn Dedicated?** Mức hỗ trợ của mô hình theo vùng, cam kết sử dụng, chi phí và quyền IAM cần thiết.

### Câu 2. Conversations API và bộ nhớ

Xem [Trạng thái hội thoại và bộ nhớ](#trạng-thái-hội-thoại-và-bộ-nhớ).

- **Conversations API quản lý gì?** Lịch sử của cuộc hội thoại nhiều lượt để lượt sau có thể dùng ngữ cảnh của lượt trước.
- **Người dùng hỏi “Còn đơn đó thì sao?” ở lượt sau. Tính năng nào giúp agent hiểu?** Ngữ cảnh ngắn hạn của cùng conversation giúp agent xác định đơn hàng đã được nhắc tới.
- **Khi cần giữ thông tin qua nhiều phiên thì dùng khái niệm nào?** Bộ nhớ dài hạn ở cấp dự án, gắn với định danh chủ thể `subject_id`.
- **Nén ngữ cảnh giải quyết vấn đề gì?** Giảm lượng lịch sử mà mô hình phải xử lý bằng cách biểu diễn nội dung dài dưới dạng ngắn hơn.

### Câu 3. Sandbox cho tool

Xem [Vì sao cần quản lý vòng đời và runtime của agent?](#1-need-for-agent-lifecycle-and-runtime).

- **Lợi ích chính của sandboxed tool execution là gì?** Cô lập quá trình chạy tool khỏi môi trường host và giới hạn tài nguyên tool có thể sử dụng.
- **Sandbox có thể cô lập những gì?** Ví dụ, không gian tiến trình, hệ thống file và không gian mạng của tác vụ.
- **Nếu tool phân tích một file CSV, file và kết quả được xử lý ở đâu?** Ứng dụng đưa file vào sandbox để xử lý rồi lấy báo cáo hoặc dữ liệu đầu ra từ môi trường đó.
- **Nếu tool cần đọc dữ liệu đơn hàng qua API, thành phần nào quyết định quyền đọc?** API hoặc dịch vụ dữ liệu kiểm tra quyền của bên gọi. Sandbox giới hạn môi trường nơi tool chạy.

### Câu 4. Containers API và Hosted Agentic Apps

Xem [Các thành phần của OCI Enterprise AI Agents](#4-oci-enterprise-ai-agents-building-blocks).

- **Containers API dùng để làm gì?** Cung cấp môi trường cô lập để chạy tác vụ tùy chỉnh, chẳng hạn xử lý file hoặc chạy mã phân tích.
- **Khi nào dùng Hosted Agentic Apps?** Khi nhóm muốn đóng gói, triển khai và phục vụ toàn bộ ứng dụng agent qua một endpoint trên hạ tầng OCI.
- **Thành phần nào quản lý quyền truy cập tài nguyên OCI?** IAM. Containers API phục vụ phần thực thi tác vụ.
- **Nếu cần lưu file và tìm đoạn văn liên quan thì dùng API nào?** Files API quản lý file. Vector Stores API hỗ trợ lập chỉ mục và truy xuất nội dung.

### Câu 5. Reranking trong RAG

Xem [Reranking trong RAG](#reranking-trong-rag).

- **Vì sao rerank sau vector similarity search?** Vector search lấy một tập ứng viên. Reranker chấm lại mức độ liên quan trong tập đó để ưu tiên tài liệu phù hợp với câu hỏi.
- **Embedding model và reranker làm gì?** Embedding model biểu diễn văn bản dưới dạng vector. Reranker chấm mức độ phù hợp của từng ứng viên với truy vấn.
- **Reranker có thể đưa lên đầu một tài liệu bị bỏ sót ở bước truy xuất không?** Nó chỉ xếp hạng tập ứng viên đã nhận. Muốn tài liệu đó được xét, cần đưa nó vào tập ứng viên ở bước truy xuất.
- **Nếu đoạn đúng đã có trong tập ứng viên nhưng nằm quá thấp thì xem bước nào?** Kiểm tra kết quả rerank và số đoạn được giữ lại để đưa vào ngữ cảnh cho mô hình.
