# Quy trình tạo embedding và truy vấn vector

Mô-đun 06 · Bài 03 · Oracle Student Guide, trang 206–211 · [Mục lục](README.md)

1. Trích văn bản và chia tài liệu dài thành các đoạn. Các tiện ích Oracle được giới thiệu gồm `UTL_TO_TEXT`, `UTL_TO_CHUNKS` và `UTL_TO_EMBEDDINGS`.
2. Tạo embedding bằng mô hình ONNX trong cơ sở dữ liệu hoặc dùng mô hình bên ngoài. Dùng cùng mô hình hoặc cấu hình cặp tài liệu và truy vấn phù hợp với mô hình đó.
3. Lưu vector cùng mã tài liệu, nội dung đoạn và siêu dữ liệu. Cột `VECTOR` có thể chỉ định số chiều, định dạng và cách lưu dense hoặc sparse.
4. Tính khoảng cách để tìm top-k. Với dữ liệu lớn, cân nhắc chỉ mục HNSW hoặc IVF cho truy vấn xấp xỉ. Workshop cũng đề cập chỉ mục hybrid khi kết hợp nhiều kiểu tìm kiếm.
5. Dùng các đoạn tìm được làm ngữ cảnh cho câu trả lời hoặc trả trực tiếp làm kết quả tìm kiếm.

Cosine đo độ khác hướng, Euclidean đo khoảng cách đường thẳng, Manhattan cộng chênh lệch tuyệt đối theo chiều, và dot product phụ thuộc cả độ lớn lẫn hướng. Chọn thước đo theo hướng dẫn của mô hình và giữ nhất quán giữa truy vấn và chỉ mục.

**Tự kiểm tra.** Khi đổi sang mô hình embedding có số chiều khác, xác định phần nào của pipeline cần tạo lại.
