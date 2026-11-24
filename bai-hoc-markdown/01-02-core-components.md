# Ba thành phần của AI agent

Mô-đun 01 · Bài 02 · Oracle Student Guide, trang 17–21 · [Mục lục](README.md)

| Thành phần | Vai trò |
| --- | --- |
| LLM | Hiểu yêu cầu, chọn công cụ và đối số, diễn giải kết quả, soạn câu trả lời. |
| Công cụ | Thực thi các tác vụ như tính toán, gọi API, truy vấn dữ liệu hoặc truy xuất tài liệu cho RAG. |
| Điều phối | Cập nhật trạng thái, thực thi và kiểm tra lời gọi, xử lý lỗi, quyết định lặp, dừng hoặc chuyển cho người xử lý. |

Độ tin cậy khi sinh đối số đúng schema là một tiêu chí chọn mô hình. Số lần gọi mô hình trong vòng lặp ảnh hưởng trực tiếp đến độ trễ và chi phí. Với hệ thống có bước phân loại và bước giải quyết phức tạp, hai bước có thể dùng hai mô hình khác nhau.

Bộ điều phối có thể giữ lịch sử của lượt làm việc hiện tại và truy xuất dữ liệu lưu dài hạn khi cần. Cấu hình quyền và điều kiện dừng thuộc về ứng dụng. Chẳng hạn, nếu công cụ hết thời gian chờ, runtime có thể thử lại một thao tác đọc hoặc trả trạng thái lỗi để người dùng quyết định.

**Tự kiểm tra.** Trong log có yêu cầu gọi tool nhưng lời gọi gặp lỗi xác thực. Thành phần nào đưa ra yêu cầu và thành phần nào cần xử lý lỗi?
