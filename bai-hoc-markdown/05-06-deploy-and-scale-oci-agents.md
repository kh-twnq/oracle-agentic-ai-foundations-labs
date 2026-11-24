# Triển khai và mở rộng agent trên OCI

Mô-đun 05 · Bài 06 · Oracle Student Guide, trang 192–194 · [Mục lục](README.md)

Bài học mở rộng từ agent chạy cục bộ sang một dịch vụ HTTP do OCI lưu trữ. Nếu ứng dụng chỉ cần gọi OCI Responses API, triển khai ứng dụng theo hạ tầng hiện có và cấu hình quyền gọi API. Với agent đóng gói riêng, quy trình thực hành như sau.

1. Chạy thử logic agent trong môi trường phát triển.
2. Đóng gói mã và phụ thuộc thành container image, rồi đẩy image lên OCI Container Registry (OCIR).
3. Tạo Generative AI Application và cấu hình xác thực, mạng, tài nguyên, lưu trữ và scaling.
4. Tạo deployment từ image đã chọn và gọi HTTP endpoint bằng danh tính được phép.

**Tự kiểm tra.** Với agent cần giữ lịch sử qua các lần thay container, giải thích trạng thái đặt ở đâu. Với tool thay đổi dữ liệu, xác định cách xử lý khi client thử lại một yêu cầu vì hết thời gian chờ.
