# Các khối xây dựng của LangChain

Mô-đun 02 · Bài 01 · Oracle Student Guide, trang 57–62 · [Mục lục](README.md)

LangChain cung cấp giao diện chung cho nhiều chat model và các thành phần như prompt template, parser và tool. LangGraph mô tả luồng chạy bằng các nút, điều kiện rẽ nhánh và trạng thái. LangSmith hỗ trợ trace, đánh giá và gỡ lỗi. Các gói tích hợp kết nối đến từng nhà cung cấp hoặc nguồn dữ liệu.

- **Model.** `init_chat_model` chọn mô hình thông qua giao diện chung. Khả năng gọi công cụ, đầu vào đa phương thức và cấu hình vẫn phụ thuộc mô hình.
- **Prompt.** `PromptTemplate` điền biến vào chuỗi văn bản. `ChatPromptTemplate` giữ vai trò của tin nhắn, ví dụ system và user. Có thể thêm vài ví dụ để định hướng định dạng cần trả về.
- **Chain.** LCEL nối các bước như `prompt | model | StrOutputParser()`. `invoke` nhận các biến đầu vào, còn parser lấy phần văn bản từ kết quả mô hình.

**Thực hành.** Tạo template nhận tên chủ đề, sau đó gọi cùng chain với hai chủ đề khác nhau. Quan sát vai trò của template, mô hình và parser trong mỗi lần chạy.

[Lab các khối xây dựng](https://github.com/oracle-university-labs/ou-generativeai-pro/blob/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/LangChain/core_building_blocks.py)
