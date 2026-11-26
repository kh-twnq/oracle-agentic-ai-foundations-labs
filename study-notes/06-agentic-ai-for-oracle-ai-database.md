# Agentic AI for Oracle AI Database

*Agentic AI cho Oracle AI Database*

Module 6 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), tr. 197–241 · [Mục lục](README.md)

## Agenda

*Nội dung học*

1. [Agentic AI cho Oracle AI Database](#1-agentic-ai-for-oracle-ai-database)
2. [Giới thiệu về Oracle AI Vector Search](#2-introduction-to-oracle-ai-vector-search)
3. [Quy trình Oracle AI Vector Search](#3-oracle-ai-vector-search-workflow)
4. [Minh họa Oracle AI Vector Search](#4-oracle-ai-vector-search-demo)
5. [Giới thiệu về Oracle AI Database Private Agent Factory](#5-introduction-to-oracle-ai-database-private-agent-factory)
6. [Giới thiệu về Select AI Agent](#6-introduction-to-select-ai-agent)
7. [Oracle Autonomous AI Database MCP Server](#7-oracle-autonomous-ai-database-mcp-server)

Nội dung theo chương trình học ở tr. 198 của Student Guide.

<a name="1-agentic-ai-for-oracle-ai-database"></a>

## 1. Agentic AI cho Oracle AI Database

Agent trong doanh nghiệp có thể cần truy xuất thông tin liên quan, thực hiện thao tác cơ sở dữ liệu đã được cấp quyền và cung cấp các tool của mình cho ứng dụng khác. Oracle AI Database có các tính năng phục vụ từng nhiệm vụ đó. (tr. 199–200)

| Tính năng | Trách nhiệm |
| --- | --- |
| **Oracle AI Vector Search** | Xếp hạng dữ liệu theo độ tương đồng ngữ nghĩa, kết hợp với bộ lọc dữ liệu quan hệ. |
| **Private Agent Factory** | Cung cấp môi trường trực quan để xây dựng workflow cho agent. |
| **Select AI Agent** | Điều phối workflow của agent gần nơi lưu trữ dữ liệu. |
| **Autonomous AI Database MCP Server** | Công bố các tool cơ sở dữ liệu cho MCP client bên ngoài. |

Autonomous AI Vector Database là một tính năng liên quan dành cho các tác vụ xử lý vector. (tr. 200)

![Các tính năng của Oracle AI Database gồm AI Vector Search, Agent Factory, Select AI Agent và Autonomous MCP Server.](images/06-oracle-ai-database.png)

<a name="2-introduction-to-oracle-ai-vector-search"></a>

## 2. Giới thiệu về Oracle AI Vector Search

**Tìm kiếm theo từ khóa** tìm nội dung có từ khóa trùng khớp. **Tìm kiếm theo ngữ nghĩa** truy xuất nội dung có ý nghĩa gần với truy vấn. Tokenizer tách văn bản thành các token, có thể là những đơn vị nhỏ hơn một từ. Mô hình embedding ánh xạ các token thành một vector có số chiều cố định. Vector của truy vấn và tài liệu phải nằm trong không gian embedding tương thích thì khoảng cách giữa chúng mới có ý nghĩa. (tr. 201–204)

Oracle AI Vector Search lưu embedding cùng với dữ liệu quan hệ. Truy vấn SQL có thể áp dụng bộ lọc theo quy tắc nghiệp vụ rồi xếp hạng các hàng còn lại theo độ tương đồng vector. (tr. 205)

<a name="3-oracle-ai-vector-search-workflow"></a>

## 3. Quy trình Oracle AI Vector Search

1. **Chuẩn bị.** Trích xuất văn bản và chia tài liệu dài thành các đoạn vừa với giới hạn đầu vào của mô hình embedding. Các đoạn nhỏ giúp bước truy xuất trả về đúng phần liên quan trong tài liệu.
2. **Tạo embedding.** Để tạo embedding trong cơ sở dữ liệu, có thể nạp mô hình ONNX bằng `DBMS_VECTOR.LOAD_ONNX_MODEL` rồi gọi mô hình qua `VECTOR_EMBEDDING`. Nhà cung cấp bên ngoài cũng có thể tạo embedding. Chuỗi xử lý tài liệu có thể dùng `UTL_TO_TEXT`, `UTL_TO_CHUNKS` và `UTL_TO_EMBEDDINGS`.
3. **Lưu trữ và lập chỉ mục.** Lưu vector cùng định danh nguồn và siêu dữ liệu. HNSW và IVF là các loại chỉ mục vector. Chỉ mục vector lai hỗ trợ kết hợp nhiều phương thức tìm kiếm.
4. **Truy xuất.** Tạo embedding cho truy vấn, xếp hạng các kết quả ứng viên rồi trả về top-k kết quả. RAG có thể đưa nội dung truy xuất được vào ngữ cảnh của mô hình. (tr. 206–211)

Cột `VECTOR` có thể khai báo số chiều và định dạng như `FLOAT32`, `FLOAT64`, `INT8` hoặc `BINARY`. Vector dày lưu mọi vị trí. Vector thưa lưu vị trí và giá trị của các phần tử khác 0. (tr. 210)

| Thước đo | Đại lượng được đo |
| --- | --- |
| **Cosine** | Độ khác biệt về hướng giữa các vector. |
| **Euclid (L2)** | Khoảng cách theo đường thẳng. |
| **Manhattan (L1)** | Tổng chênh lệch tuyệt đối theo từng chiều. |
| **Tích vô hướng** | Điểm số dựa trên hướng và độ lớn của vector. |

Khoảng cách càng nhỏ thì kết quả càng gần với truy vấn. Thứ tự xếp hạng theo tích vô hướng phụ thuộc vào cách diễn giải điểm số. (tr. 211)

<a name="4-oracle-ai-vector-search-demo"></a>

## 4. Minh họa Oracle AI Vector Search

**Tìm kiếm tương đồng chính xác** tính khoảng cách giữa vector truy vấn và từng vector đủ điều kiện. Truy vấn và nội dung đã lưu dùng mô hình embedding tương thích. `VECTOR_DISTANCE` cung cấp giá trị để xếp hạng. Một điều kiện lọc trên dữ liệu quan hệ giới hạn các hàng được xét trước khi xếp hạng và lấy top-k kết quả. (tr. 212–222)

<a name="5-introduction-to-oracle-ai-database-private-agent-factory"></a>

## 5. Giới thiệu về Oracle AI Database Private Agent Factory

Private Agent Factory cung cấp các agent dựng sẵn, công cụ tạo workflow trực quan và các tích hợp dữ liệu. Đăng nhập một lần (SSO), quyền truy cập theo vai trò và guardrail cho prompt hỗ trợ công tác quản trị. Có thể triển khai dưới dạng container bằng Podman tại chỗ hoặc trên đám mây, với kết nối tới Oracle AI Database và nhà cung cấp mô hình. (tr. 223–225)

| Thành phần | Thành phần này làm việc với gì? |
| --- | --- |
| **Knowledge Agent** | Tài liệu được phê duyệt từ file, SharePoint, website hoặc OCI Object Storage. Embedding hỗ trợ truy xuất và câu trả lời có thể dẫn nguồn. |
| **Data Analysis Agent** | Các bảng và view mà agent có quyền truy cập. Agent sinh SQL rồi trình bày kết quả hoặc trực quan hóa dữ liệu. |
| **Agent Builder** | Các nút workflow trực quan. Tool, tích hợp MCP, thành phần Python tùy chỉnh và nhiều agent có thể cùng tham gia. |

Các nguồn đã kết nối và quyền được cấp quyết định agent có thể truy cập những gì. (tr. 226–228)

<a name="6-introduction-to-select-ai-agent"></a>

## 6. Giới thiệu về Select AI Agent

**Select AI Agent** điều phối workflow của agent gần nơi lưu trữ dữ liệu. **Hồ sơ AI (AI profile)** cung cấp cấu hình mô hình và ngữ cảnh dữ liệu. `DBMS_CLOUD_AI_AGENT` định nghĩa agent, tool, tác vụ và nhóm. Vai trò trong cơ sở dữ liệu và chính sách Virtual Private Database (VPD) kiểm soát quyền truy cập. Cơ chế kiểm toán ghi lại hoạt động trong cơ sở dữ liệu. (tr. 229–231)

Lập kế hoạch (Planning) chọn các bước. Sử dụng tool (Tool Use) thực hiện hành động. Đánh giá lại (Reflection) kiểm tra kết quả. Quản lý bộ nhớ (Memory Management) giữ ngữ cảnh liên quan qua các lượt. Một lượt chạy có thể dùng RAG để truy xuất nội dung, **NL2SQL** để sinh SQL, PL/SQL để thực hiện thao tác nghiệp vụ hoặc REST để kết nối với hệ thống bên ngoài. (tr. 232–234)

## 7. Oracle Autonomous AI Database MCP Server

**Oracle Autonomous AI Database MCP Server** là tính năng đa tenant được quản lý của Autonomous AI Database Serverless. MCP client dùng Streamable HTTP qua HTTPS để kết nối tới endpoint ứng với vùng và OCID của cơ sở dữ liệu. Server công bố các tool của Select AI Agent như NL2SQL, RAG và PL/SQL tùy chỉnh. (tr. 235–240)

Thông tin xác thực của cơ sở dữ liệu xác định người gọi. Vai trò và chính sách trong cơ sở dữ liệu quyết định tool và dữ liệu nào có thể truy cập. Hồ sơ AI có thể cung cấp siêu dữ liệu schema cho NL2SQL và giảm việc khám phá schema trong lúc xử lý yêu cầu. MCP quy định cách client bên ngoài khám phá và gọi các tool. (tr. 237–241) [Các thành phần cốt lõi của MCP](03-introduction-to-mcp.md#2-mcp-core-components)
