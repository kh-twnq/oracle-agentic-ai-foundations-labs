# Gọi OCI Responses API lần đầu

Mô-đun 05 · Bài 05 · Oracle Student Guide, trang 187–191 · [Mục lục](README.md)

Bài lab cần tài khoản OCI, compartment, project Generative AI, region, model ID và phương thức xác thực được cấp quyền. Project tổ chức tài nguyên ứng dụng như phản hồi, cuộc hội thoại và file. Bài học trình bày API key của OCI Generative AI và xác thực OCI IAM bằng ký yêu cầu.

Với ví dụ dùng OpenAI Python SDK, đặt `base_url` trỏ tới endpoint OCI theo region. Cấu hình khóa cho client và gửi OCID của project qua header `OpenAI-Project`. Gọi `client.responses.create` với model ID trên OCI và đọc `output_text`. Kiểm tra endpoint, model, project và phương thức xác thực lấy từ cùng môi trường dự kiến.

## Chuẩn bị và kiểm tra request đầu tiên

1. Chọn compartment và Generative AI project. Ghi lại region, project OCID và model ID của lab.
2. Chọn xác thực bằng **OCI Generative AI API key** hoặc **OCI IAM request signing**. Với IAM, ví dụ workshop cấu hình HTTP client và profile để ký request. Đọc script tương ứng với phương thức mình đang dùng.
3. Với OpenAI-compatible API key flow, tạo client có `base_url` OCI, API key lấy từ environment và header `OpenAI-Project`. Sau đó gửi `model` và `input`, đọc `output_text`.
4. Dùng cùng kiểu request với một ví dụ OpenAI gốc để đối chiếu. Thay đổi chính nằm ở endpoint, authentication, model ID và project scope.

Guide minh họa cả API key và ký yêu cầu qua IAM. Hãy kiểm tra các biến môi trường theo đúng script được chạy, vì tên biến có thể khác giữa các ví dụ.

**Thực hành.** Gửi một yêu cầu tóm tắt ngắn. Nếu gặp lỗi xác thực, kiểm tra nguồn khóa hoặc profile và chính sách. Nếu phản hồi báo tài nguyên không tồn tại, đối chiếu cấu hình region, project, model.

[Ví dụ OCI Python SDK](https://github.com/oracle-university-labs/ou-generativeai-pro/blob/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/OCI/oci_first_agent_sdk.py) · [Ví dụ OCI đơn giản](https://github.com/oracle-university-labs/ou-generativeai-pro/blob/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/OCI/oci_first_agent_simple.py)
