# Deploy và scale OCI agent

Mô-đun 05 · Bài 06 · Oracle Student Guide, trang 192–194 · [Mục lục](README.md)

Bài học mở rộng từ agent chạy cục bộ sang một dịch vụ HTTP do OCI lưu trữ. Nếu ứng dụng chỉ cần gọi OCI Responses API, triển khai ứng dụng theo hạ tầng hiện có và cấu hình quyền gọi API. Với agent đóng gói riêng, quy trình thực hành như sau.

1. Chạy thử logic agent trong môi trường phát triển.
2. Đóng gói mã và phụ thuộc thành container image, rồi đẩy image lên OCI Container Registry (OCIR).
3. Tạo Generative AI Application và cấu hình xác thực, mạng, tài nguyên, lưu trữ và scaling.
4. Tạo deployment từ image đã chọn và gọi HTTP endpoint bằng danh tính được phép.

## Các mốc từ local development đến endpoint

Guide trình bày chuỗi **build → package → upload → configure → deploy → invoke**. Ở ba bước đầu, image cần gom đúng agent code và runtime dependencies rồi được lưu tại OCIR. Ở ba bước sau, tạo cấu hình ứng dụng, chọn image để deploy và xác nhận endpoint thực thi được agent theo đúng identity.

Sau khi invoke, kiểm tra log để biết phiên bản image nào đang chạy, request nào đến endpoint, thời gian tool call và cách một lỗi được báo về caller. Phân biệt lỗi tại identity/network với lỗi trong agent logic. Nếu app dùng OCI Responses API trực tiếp, điểm triển khai cần kiểm tra là ứng dụng gọi API và service endpoint của OCI.

**Tự kiểm tra.** Với agent cần giữ lịch sử qua các lần thay container, giải thích trạng thái đặt ở đâu. Với tool thay đổi dữ liệu, xác định cách xử lý khi client thử lại một yêu cầu vì hết thời gian chờ.
