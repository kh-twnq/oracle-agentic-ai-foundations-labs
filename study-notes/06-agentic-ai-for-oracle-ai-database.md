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
6. [Select AI và Select AI Agent](#6-introduction-to-select-ai-agent)
7. [Oracle Autonomous AI Database MCP Server](#7-oracle-autonomous-ai-database-mcp-server)

Nội dung theo chương trình học ở tr. 198 của Student Guide.

<a name="1-agentic-ai-for-oracle-ai-database"></a>

## 1. Agentic AI cho Oracle AI Database

Agent trong doanh nghiệp có thể cần truy xuất thông tin liên quan, thực hiện thao tác cơ sở dữ liệu đã được cấp quyền và cung cấp các tool của mình cho ứng dụng khác. Oracle AI Database có các tính năng phục vụ từng nhiệm vụ đó. (tr. 199–200)

| Tính năng | Trách nhiệm |
| --- | --- |
| **Oracle AI Vector Search** | Xếp hạng dữ liệu theo độ tương đồng ngữ nghĩa, kết hợp với bộ lọc dữ liệu quan hệ. |
| **Private Agent Factory** | Cung cấp môi trường trực quan để xây dựng workflow cho agent. |
| **Select AI** | Dùng câu hỏi ngôn ngữ tự nhiên để tạo SQL, chạy truy vấn hoặc diễn giải kết quả. |
| **Select AI Agent** | Điều phối tác vụ nhiều bước và các tool gần nơi lưu trữ dữ liệu. |
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

Với `VECTOR_DISTANCE(..., COSINE)`, khoảng cách càng nhỏ thì vector càng gần. Trong Oracle, `VECTOR_DISTANCE(..., DOT)` trả **tích vô hướng đổi dấu**, nên sắp xếp tăng dần theo khoảng cách DOT tương đương xếp tích vô hướng gốc từ cao xuống thấp. Khi dùng chỉ mục vector cho tìm kiếm xấp xỉ, dùng metric phù hợp với chỉ mục. (tr. 211) [Hàm VECTOR_DISTANCE](https://docs.oracle.com/en/database/oracle/oracle-database/26/vecse/vector_distance.html)

<a name="4-oracle-ai-vector-search-demo"></a>

## 4. Minh họa Oracle AI Vector Search

**Tìm kiếm tương đồng chính xác** tính khoảng cách giữa vector truy vấn và từng vector đủ điều kiện. Truy vấn và nội dung đã lưu dùng mô hình embedding tương thích. `VECTOR_DISTANCE` cung cấp giá trị để xếp hạng. Một điều kiện lọc trên dữ liệu quan hệ giới hạn các hàng được xét trước khi xếp hạng và lấy top-k kết quả. (tr. 212–222)

### Dùng kết quả truy xuất để tạo câu trả lời

Ví dụ dùng một catalog `products` có các cột `product_id`, `product_name`, `description`, `price_usd` và `embedding` kiểu `VECTOR(384, FLOAT32)`. Tạo embedding cho “protection for water sports” bằng cùng mô hình đã tạo embedding cho mô tả sản phẩm. Truyền chuỗi vector 384 chiều vào biến bind `:query_embedding`.

```sql
SELECT product_id, product_name, description, price_usd,
       VECTOR_DISTANCE(embedding, TO_VECTOR(:query_embedding), COSINE) AS distance
FROM products
WHERE price_usd < 100
ORDER BY distance, product_id
FETCH FIRST 5 ROWS ONLY;
```

Đưa tên, mô tả, giá và mã sản phẩm của các hàng truy xuất vào ngữ cảnh của agent. Yêu cầu agent đề xuất sản phẩm dựa trên các hàng đó và dẫn mã sản phẩm làm căn cứ. Nếu kết quả trống hoặc thiếu dữ kiện, agent báo thiếu căn cứ hoặc hỏi lại. Bước truy xuất tạo bằng chứng cho câu trả lời mà không cần tinh chỉnh mô hình.

Trong lab, điều kiện dưới 100 USD và phép xếp hạng cosine đưa **Swimming Goggles** lên đầu cho truy vấn này. File SQL tạo sẵn chứa vector mẫu và có thể chạy trên Oracle AI Database 26ai mà không cần tạo bảng `products`. [SQL lab được tạo sẵn](../labs/sample-results/vector-search-oracle.sql) · [Kết quả Oracle FreeSQL](../labs/sample-results/vector-search-oracle.json) · [Cách chạy lab](../labs/README.md#vector-search-comparison-with-the-guide)

<a name="5-introduction-to-oracle-ai-database-private-agent-factory"></a>

## 5. Giới thiệu về Oracle AI Database Private Agent Factory

Private Agent Factory cung cấp các agent dựng sẵn, công cụ tạo workflow trực quan và các tích hợp dữ liệu. Đăng nhập một lần (SSO), quyền truy cập theo vai trò và guardrail cho prompt hỗ trợ công tác quản trị. Có thể triển khai dưới dạng container bằng Podman tại chỗ hoặc trên đám mây, với kết nối tới Oracle AI Database và nhà cung cấp mô hình. (tr. 223–225)

| Thành phần | Thành phần này làm việc với gì? |
| --- | --- |
| **Knowledge Agent** | Tài liệu được phê duyệt từ file, SharePoint, website hoặc OCI Object Storage. Embedding hỗ trợ truy xuất và câu trả lời có thể dẫn nguồn. |
| **Data Analysis Agent** | Các bảng và view mà agent có quyền truy cập. Agent sinh SQL rồi trình bày kết quả hoặc trực quan hóa dữ liệu. |
| **Agent Builder** | Các nút workflow trực quan. Tool, tích hợp MCP, thành phần Python tùy chỉnh và nhiều agent có thể cùng tham gia. |

Để tạo agent không cần viết code, chọn mẫu hoặc kéo thả các nút vào Agent Builder, kết nối nguồn dữ liệu đã được cấp quyền, chọn mô hình và thêm chỉ dẫn. Chẳng hạn, dùng Knowledge Agent đã kết nối tài liệu chính sách làm một nút trong workflow hỏi đáp. Chạy thử để xem câu trả lời và dẫn nguồn trước khi triển khai. Các nguồn đã kết nối và quyền được cấp quyết định phạm vi truy cập. (tr. 226–228) [Giới thiệu Private Agent Factory](https://docs.oracle.com/en/database/oracle/agent-factory/25.3/paias/introduction.html) · [Các nút trong Agent Builder](https://docs.oracle.com/en/database/oracle/agent-factory/26.7/paias/agent-builder-components.html)

<a name="6-introduction-to-select-ai-agent"></a>

## 6. Select AI và Select AI Agent

### Hỏi dữ liệu bằng Select AI

**Select AI** dùng mô hình đã cấu hình trong AI profile để xử lý câu hỏi bằng ngôn ngữ tự nhiên. Profile chọn provider, model, thông tin xác thực và phạm vi bảng hoặc view dùng làm ngữ cảnh. Với truy vấn NL2SQL, mô hình dựa vào metadata để sinh SQL. Cơ sở dữ liệu thi hành truy vấn theo quyền của người gọi khi hành động yêu cầu thực thi.

| Hành động | Kết quả |
| --- | --- |
| `SHOWSQL` | Hiển thị SQL được tạo để người dùng xem trước. |
| `RUNSQL` | Chạy truy vấn SQL được tạo và trả các hàng kết quả. |
| `NARRATE` | Chạy truy vấn, rồi dùng kết quả để tạo câu trả lời bằng ngôn ngữ tự nhiên. |

Ví dụ dưới đây dùng một AI profile đã cấu hình sẵn cho catalog. Lệnh đầu chọn profile cho phiên. Lệnh sau hiển thị SQL Oracle sinh ra cho câu hỏi. Chạy trong SQL client hỗ trợ cú pháp `SELECT AI`.

```sql
EXEC DBMS_CLOUD_AI.SET_PROFILE('PRODUCTS_PROFILE');
SELECT AI SHOWSQL Which products cost less than 100 dollars;
```

Ứng dụng không giữ trạng thái phiên có thể gọi `DBMS_CLOUD_AI.GENERATE` với `profile_name`, `prompt` và `action` tường minh. [Ví dụ Select AI](https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/select-ai-examples.html) · [Sinh SQL từ câu hỏi](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/adbaa/generate-sql-from-natural-language-prompts-using-select-ai.html)

### Điều phối tác vụ bằng Select AI Agent

**Select AI Agent** điều phối workflow của agent gần nơi lưu trữ dữ liệu. **Hồ sơ AI (AI profile)** cung cấp cấu hình mô hình và ngữ cảnh dữ liệu. `DBMS_CLOUD_AI_AGENT` định nghĩa agent, tool, tác vụ và nhóm. Vai trò trong cơ sở dữ liệu và chính sách Virtual Private Database (VPD) kiểm soát quyền truy cập. Cơ chế kiểm toán ghi lại hoạt động trong cơ sở dữ liệu. (tr. 229–231)

Lập kế hoạch (Planning) chọn các bước. Sử dụng tool (Tool Use) thực hiện hành động. Đánh giá lại (Reflection) kiểm tra kết quả. Quản lý bộ nhớ (Memory Management) giữ ngữ cảnh liên quan qua các lượt. Một lượt chạy có thể dùng RAG để truy xuất nội dung, **NL2SQL** để sinh SQL, PL/SQL để thực hiện thao tác nghiệp vụ hoặc REST để kết nối với hệ thống bên ngoài. (tr. 232–234)

## 7. Oracle Autonomous AI Database MCP Server

**Oracle Autonomous AI Database MCP Server** là tính năng đa tenant được quản lý của Autonomous AI Database Serverless. MCP client dùng Streamable HTTP qua HTTPS để kết nối tới endpoint ứng với vùng và OCID của cơ sở dữ liệu. Server công bố các tool của Select AI Agent như NL2SQL, RAG và PL/SQL tùy chỉnh. (tr. 235–240)

Thông tin xác thực của cơ sở dữ liệu xác định người gọi. Vai trò và chính sách trong cơ sở dữ liệu quyết định tool và dữ liệu nào có thể truy cập. Hồ sơ AI có thể cung cấp siêu dữ liệu schema cho NL2SQL và giảm việc khám phá schema trong lúc xử lý yêu cầu. (tr. 237–241)

Luồng tích hợp bắt đầu bằng việc bật MCP Server cho database và chuẩn bị tool trong Select AI Agent, chẳng hạn tool tra cứu chính sách bằng RAG. Ứng dụng cấu hình endpoint và xác thực theo thiết lập của database, rồi dùng `tools/list` để khám phá tool mà danh tính hiện tại được phép thấy. Khi agent chọn tool, MCP client gửi `tools/call` với các đối số. Database áp dụng quyền, chạy tool và trả dữ liệu để agent sử dụng trong câu trả lời. [Tài liệu MCP Server của Oracle](https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/mcp-server.html) · [Thiết lập và gọi MCP Server](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/use-mcp-server.html) · [Các thành phần cốt lõi của MCP](03-introduction-to-mcp.md#2-mcp-core-components)
