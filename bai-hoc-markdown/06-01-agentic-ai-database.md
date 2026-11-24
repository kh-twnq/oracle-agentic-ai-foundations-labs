# Tổng quan agentic AI trên Oracle AI Database

Mô-đun 06 · Bài 01 · Oracle Student Guide, trang 199–200 · [Mục lục](README.md)

Tài liệu mô tả nhiều cách đưa semantic search, workflow và công cụ cho agent đến gần dữ liệu nghiệp vụ.

| Năng lực | Vai trò |
| --- | --- |
| Oracle AI Vector Search | Lưu và truy vấn vector cùng dữ liệu quan hệ bằng SQL. |
| Private Agent Factory | Xây và thử agent qua giao diện trực quan, kết nối nguồn dữ liệu đã chọn. |
| Select AI Agent | Định nghĩa và chạy workflow agent qua SQL và PL/SQL. |
| Autonomous AI Database MCP Server | Cung cấp các tool được cấp phép qua endpoint MCP. |

Workshop còn giới thiệu Autonomous AI Vector Database như hướng dùng dịch vụ vector được vận hành sẵn. Một ứng dụng có thể dùng Vector Search để tìm các đoạn liên quan, rồi cung cấp kết quả cho agent chạy trong ứng dụng hoặc trong cơ sở dữ liệu.

## Chọn capability theo đường đi của dữ liệu

Một ứng dụng hỏi đáp có thể dùng **Oracle AI Vector Search** cho semantic retrieval rồi gửi kết quả sang LLM dưới dạng RAG context. **Private Agent Factory** phù hợp khi cần ghép data source và workflow qua UI. **Select AI Agent** phù hợp khi orchestration và tool implementation cần đặt gần dữ liệu, dùng SQL hoặc PL/SQL. **Autonomous AI Database MCP Server** cung cấp điểm truy cập theo protocol cho MCP clients bên ngoài.

Sơ đồ tổng quan của guide còn nhắc đến **Oracle Deep Data Security**, **Oracle Trusted Answer Search**, **Oracle Vectors on Ice** và **Oracle Private AI Services Container** ở mức hệ sinh thái. Các bài thực hành kế tiếp tập trung vào Vector Search, Agent Factory, Select AI Agent và MCP Server.

**Tự kiểm tra.** Nếu một agent chạy bên ngoài cần gọi một truy vấn nghiệp vụ đã giới hạn quyền, phân biệt vai trò của truy vấn, cơ sở dữ liệu và giao diện MCP.
