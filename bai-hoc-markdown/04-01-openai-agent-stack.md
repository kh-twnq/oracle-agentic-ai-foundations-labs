# Responses API và Agents SDK trong ứng dụng

Mô-đun 04 · Bài 01 · Oracle Student Guide, trang 125–129 · [Mục lục](README.md)

Ứng dụng giữ giao diện, quy tắc nghiệp vụ và tích hợp dữ liệu. Responses API là lớp gọi mô hình và cấu hình công cụ. Agents SDK dùng lớp API bên dưới để điều phối lượt chạy, tool, handoff, guardrail và trace.

| Tình huống | Điểm bắt đầu |
| --- | --- |
| Một câu hỏi và một phản hồi, có thể dùng công cụ do nền tảng vận hành | Gọi trực tiếp Responses API. |
| Cần tự quy định các trạng thái, lưu đối số và duyệt từng bước gọi hàm | Quản lý vòng lặp với Responses API. |
| Có nhiều agent chuyên trách, nhiều lời gọi và cần trace tập trung | Định nghĩa các agent và chạy bằng Agents SDK. |

## Ranh giới giữa application, SDK và API

Application giữ user interface, xác thực và business rules. Responses API nhận input, mô hình và cấu hình tool, rồi trả output theo cấu trúc để caller xử lý. Agents SDK thêm các khái niệm như Agent, Runner, handoff và guardrail trên lớp API này.

Trong ví dụ đặt chuyến bay, khi gọi API trực tiếp, application chịu trách nhiệm kiểm tra tool call, chạy tool được yêu cầu, gửi kết quả về model và xử lý retry. Nếu dùng Agents SDK, Runner thực hiện vòng lặp và liên kết tool result với request. Điều kiện nghiệp vụ như xác nhận trước khi đặt vé vẫn cần nằm trong app hoặc tool implementation.

**Tự kiểm tra.** Hệ thống đặt lịch cần tra các khung giờ và yêu cầu xác nhận trước khi ghi lịch. Xác định bước nào do mô hình đề xuất và bước nào cần do ứng dụng kiểm soát.
