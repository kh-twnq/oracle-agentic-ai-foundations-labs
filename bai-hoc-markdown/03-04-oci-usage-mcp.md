# Thực hành MCP với dữ liệu sử dụng OCI

Mô-đun 03 · Bài 04 · Oracle Student Guide, trang 116–120 · [Mục lục](README.md)

Oracle cung cấp gói `oracle.oci-usage-mcp-server`. Trong bài lab, `uvx` khởi chạy server trên máy cục bộ. Client trao đổi với server qua stdio. Chính tiến trình server gọi OCI Usage API qua HTTPS bằng hồ sơ OCI đã cấu hình.

Tool `get_summarized_usage` nhận tenancy, thời gian bắt đầu và kết thúc, độ chi tiết theo thời gian và chiều nhóm như dịch vụ. Loại truy vấn xác định dữ liệu chi phí hay mức sử dụng. Để tái tạo báo cáo, client cần áp dụng cùng bộ lọc và khoảng thời gian khi so sánh với Cost Analysis.

Có thể gọi server từ client trực tiếp để kiểm tra schema và dữ liệu trước khi thêm mô hình. Bài lab agent diễn giải yêu cầu ngôn ngữ tự nhiên thành tham số rồi tổng hợp kết quả. Workspace có hai báo cáo trên dữ liệu giả lập để đối chiếu. Truy vấn thật cần hồ sơ OCI có quyền đọc dữ liệu chi phí của tenancy.

[Client OCI Usage](https://github.com/oracle-university-labs/ou-generativeai-pro/blob/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/Real%20World%20MCP/01_oci_usage_mcp_client.py) · [Agent OCI Usage](https://github.com/oracle-university-labs/ou-generativeai-pro/blob/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/Real%20World%20MCP/02_oci_usage_mcp_agent.py)

Trong workspace cục bộ, báo cáo mẫu nằm ở `results/oci-usage-agent-synthetic.csv`.
