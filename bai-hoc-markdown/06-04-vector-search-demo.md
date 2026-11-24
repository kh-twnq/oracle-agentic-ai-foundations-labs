# Oracle AI Vector Search Demo với Python và SQL

Mô-đun 06 · Bài 04 · Oracle Student Guide, trang 212–222 · [Mục lục](README.md)

Lab dùng `python-oracledb` và mô hình `all-MiniLM-L6-v2` để tạo embedding 384 chiều cho mô tả của mười sản phẩm. Mỗi hàng lưu tên, mô tả, giá, danh mục và vector. Khi người dùng nhập câu hỏi, tạo vector truy vấn bằng cùng mô hình và bind vào SQL.

Bài đầu xếp hạng ba sản phẩm gần nhất với ý định tìm dụng cụ tập tại nhà. Bài hai ưu tiên đồ bảo hộ cho thể thao dưới nước và giới hạn giá dưới 100 USD. Đây là ví dụ truy vấn áp dụng điều kiện giá rồi xếp hạng theo cosine.

```sql
SELECT name, price
FROM products
WHERE price < :price_limit
ORDER BY VECTOR_DISTANCE(embedding, :query_vector, COSINE), id
FETCH FIRST 5 ROWS ONLY;
```

Workspace có kết quả chạy SQLite với vector thật và đối chiếu bằng `VECTOR_DISTANCE` trên Oracle FreeSQL. Tài liệu minh họa và lần chạy cục bộ có thể cho thứ hạng khác nhau khi thay mô tả sản phẩm. README của lab ghi các khác biệt và cách kiểm tra truy vấn từ khóa.

Trong workspace cục bộ, script chạy thử là `vector_search_local.py` và kết quả đối chiếu nằm ở `results/vector-search-oracle.json`.

## Setup, data ingestion và hai truy vấn trong guide

1. Cài `oracledb` và `sentence-transformers`, rồi kết nối schema lab trên Oracle AI Database có hỗ trợ `VECTOR`. Tạo bảng sản phẩm với cột `VECTOR(384, FLOAT32)` cho model demo.
2. Dùng `SentenceTransformer` để encode từng mô tả. Chuyển dữ liệu thành `array.array("f", ...)` cho bind kiểu float32 bằng Python driver. Insert các hàng và commit trước khi kiểm tra kết quả.
3. Tạo query embedding cho ý định tìm thiết bị tập ở nhà. Chạy exact similarity search bằng `VECTOR_DISTANCE` theo `COSINE`, trả top 3 và hiển thị điểm để đối chiếu.
4. Tạo query embedding cho ý định tìm đồ bảo hộ thể thao dưới nước. Thêm `WHERE price < 100` rồi lấy top 5. Kiểm tra cả thứ hạng và điều kiện giá.

Guide minh họa Yoga Mat, Fitness Tracker và Basketball cho truy vấn đầu, còn Swimming Goggles là kết quả nổi bật của truy vấn thứ hai. Đọc phần mô tả sản phẩm và phép so trùng trước khi kết luận về baseline. Ví dụ, mô tả Climbing Harness trên trang 215 có chữ `gear`, nên truy vấn literal dùng từ đó có thể trả kết quả. Cùng model và metric vẫn có thể đổi thứ hạng nếu mô tả hoặc query text thay đổi.
