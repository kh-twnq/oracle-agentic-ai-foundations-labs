# Responses API và Agents SDK trong ứng dụng

Mô-đun 04 · Bài 01 · Oracle Student Guide, trang 125–129 · [Mục lục](README.md)

Ứng dụng giữ giao diện, quy tắc nghiệp vụ và tích hợp dữ liệu. Responses API là lớp gọi mô hình và cấu hình công cụ. Agents SDK dùng lớp API bên dưới để điều phối lượt chạy, tool, handoff, guardrail và trace.

| Tình huống | Điểm bắt đầu |
| --- | --- |
| Một câu hỏi và một phản hồi, có thể dùng công cụ do nền tảng vận hành | Gọi trực tiếp Responses API. |
| Cần tự quy định các trạng thái, lưu đối số và duyệt từng bước gọi hàm | Quản lý vòng lặp với Responses API. |
| Có nhiều agent chuyên trách, nhiều lời gọi và cần trace tập trung | Định nghĩa các agent và chạy bằng Agents SDK. |

**Tự kiểm tra.** Hệ thống đặt lịch cần tra các khung giờ và yêu cầu xác nhận trước khi ghi lịch. Xác định bước nào do mô hình đề xuất và bước nào cần do ứng dụng kiểm soát.
