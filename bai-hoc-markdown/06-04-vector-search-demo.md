# Lab xếp hạng sản phẩm bằng vector và SQL

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
