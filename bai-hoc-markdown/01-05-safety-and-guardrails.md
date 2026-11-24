# An toàn và guardrails cho agent

Mô-đun 01 · Bài 05 · Oracle Student Guide, trang 46–52 · [Mục lục](README.md)

Agent có thể gặp chỉ dẫn chèn trong dữ liệu lấy về, yêu cầu dùng công cụ ngoài phạm vi, nội dung độc hại được lưu vào bộ nhớ, rò rỉ dữ liệu hoặc vòng lặp tốn tài nguyên. Mức độ ảnh hưởng phụ thuộc vào quyền mà từng công cụ có và dữ liệu mà agent được phép trao đổi.

| Lớp kiểm soát | Việc cần làm |
| --- | --- |
| Đầu vào | Coi tài liệu và nội dung từ nguồn ngoài là dữ liệu chưa tin cậy. Kiểm tra định dạng, kích thước và tần suất. |
| Điều phối | Chỉ cấp bộ công cụ cần dùng. Đặt giới hạn số vòng, thời gian và ngân sách. |
| Thực thi | Kiểm tra đối số và quyền trên đối tượng cụ thể. Cách ly mã chạy. Yêu cầu phê duyệt trước thao tác có hệ quả lớn. |
| Đầu ra | Kiểm tra thông tin cá nhân, bí mật cần che và căn cứ của kết luận. |
| Giám sát | Ghi tên tool, kết quả, lỗi và chi phí. Che dữ liệu nhạy cảm trong trace. |

**Tự kiểm tra.** Thiết kế hai quyền riêng cho một tool đọc đơn hàng và một tool sửa đơn hàng. Với thao tác ghi có thể được thử lại sau timeout, dùng mã yêu cầu để tránh áp dụng cùng một thay đổi hai lần.
