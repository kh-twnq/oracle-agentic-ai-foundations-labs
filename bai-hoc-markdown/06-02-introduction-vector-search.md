# Cơ bản về Oracle AI Vector Search

Mô-đun 06 · Bài 02 · Oracle Student Guide, trang 201–205 · [Mục lục](README.md)

Tìm kiếm từ khóa phụ thuộc từ xuất hiện trong văn bản. Tìm kiếm ngữ nghĩa biểu diễn văn bản và truy vấn thành các mảng số gọi là **embedding**, rồi dùng khoảng cách để xếp hạng. Hai câu diễn đạt khác nhau có thể có vector gần nhau nếu mô hình học được quan hệ về nghĩa.

Tokenizer tách văn bản thành token. Mô hình embedding xử lý chuỗi token và tạo vector với số chiều xác định. Số chiều và cách tạo vector phụ thuộc mô hình. Tài liệu và truy vấn cần được đưa vào cùng một không gian embedding để khoảng cách có ý nghĩa.

Oracle AI Database lưu vector cùng các cột thông thường. `VECTOR_DISTANCE` dùng trong SQL để xếp hạng theo độ gần, còn `WHERE` giới hạn theo giá, danh mục hoặc siêu dữ liệu khác. Kết quả tìm kiếm ngữ nghĩa có thể trở thành đoạn ngữ cảnh trong RAG.

**Tự kiểm tra.** Với yêu cầu tìm áo khoác đi mưa dưới một mức giá, xác định phần nào biểu diễn thành embedding và phần nào dùng điều kiện số.
