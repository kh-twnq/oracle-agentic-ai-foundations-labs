# Threat Model và Guardrails cho AI agent

Mô-đun 01 · Bài 05 · Oracle Student Guide, trang 46–52 · [Mục lục](README.md)

Agent có thể gặp prompt injection trong dữ liệu lấy về, yêu cầu dùng công cụ ngoài phạm vi, nội dung độc hại được lưu vào bộ nhớ, rò rỉ dữ liệu hoặc vòng lặp tốn tài nguyên. Mức độ ảnh hưởng phụ thuộc vào quyền mà từng công cụ có và dữ liệu mà agent được phép trao đổi.

| Lớp kiểm soát | Việc cần làm |
| --- | --- |
| Đầu vào | Coi tài liệu và nội dung từ nguồn ngoài là dữ liệu chưa tin cậy. Kiểm tra định dạng, kích thước và tần suất. |
| Điều phối | Chỉ cấp bộ công cụ cần dùng. Đặt giới hạn số vòng, thời gian và ngân sách. |
| Thực thi | Kiểm tra đối số và quyền trên đối tượng cụ thể. Cách ly mã chạy. Yêu cầu phê duyệt trước thao tác có hệ quả lớn. |
| Đầu ra | Kiểm tra thông tin cá nhân, bí mật cần che và căn cứ của kết luận. |
| Giám sát | Ghi tên tool, kết quả, lỗi và chi phí. Che dữ liệu nhạy cảm trong trace. |

## Threat model và các ví dụ trong guide

Guide dẫn hai sự cố để minh họa rủi ro của agent có quyền đọc dữ liệu hoặc ghi memory. Trường hợp Slack AI minh họa **indirect prompt injection** qua nội dung được truy xuất và rủi ro khi thông tin từ vùng dữ liệu hạn chế xuất hiện ở output. Trường hợp `spAIware` minh họa **memory poisoning** kéo dài sang phiên sau. Các điểm kiểm soát tương ứng gồm xác thực phạm vi truy xuất, kiểm tra output, ghi nhận nguồn và kiểm soát dữ liệu được đưa vào long-term memory.

- **Tool misuse** xảy ra khi một lời gọi hợp lệ về kiểu dữ liệu lại sai quyền hoặc sai mục đích. Tool cần tự kiểm tra quyền theo đối tượng và hành động.
- **Data exfiltration** có thể đi qua phản hồi hoặc một tool gửi dữ liệu ra ngoài. Xác định rõ đích được phép và che dữ liệu nhạy cảm trước khi truyền.
- **Runaway execution** cần giới hạn lượt, token, thời gian và chi phí. Log nên cho phép phân biệt vòng lặp logic với retry do timeout.

**Defense in depth** kết hợp input validation, model guardrails, tool boundaries, output filtering và observability. Với các bước ghi dữ liệu, thêm **idempotency** và **human-in-the-loop** theo mức rủi ro.

**Tự kiểm tra.** Thiết kế hai quyền riêng cho một tool đọc đơn hàng và một tool sửa đơn hàng. Với thao tác ghi có thể được thử lại sau timeout, dùng mã yêu cầu để tránh áp dụng cùng một thay đổi hai lần.
