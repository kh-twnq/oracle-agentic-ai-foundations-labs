# Reasoning Patterns với CoT, ReAct và ToT

Mô-đun 01 · Bài 03 · Oracle Student Guide, trang 22–27 · [Mục lục](README.md)

**Chain-of-Thought (CoT)** chia bài toán thành các bước trung gian. Mẫu này phù hợp với bài toán logic có dữ kiện nằm trong đề. Chia nhỏ lập luận vẫn có thể cho kết quả sai khi dữ kiện đầu vào thiếu hoặc đã cũ.

**ReAct** đan xen quyết định, hành động và quan sát. Sau mỗi lần gọi tool, kết quả mới có thể thay đổi kế hoạch. Ví dụ, agent cần tìm giờ mở cửa của một chi nhánh. Nó tra đúng địa chỉ, kiểm tra có lịch nghỉ lễ tại nơi đó rồi tổng hợp kết quả. Trace của lời gọi, đối số và dữ liệu trả về giúp theo dõi tiến trình.

**Tree-of-Thoughts (ToT)** xem xét nhiều hướng giải, đánh giá các phương án trung gian rồi chọn nhánh để tiếp tục. Duyệt thêm nhánh làm tăng số lần đánh giá nên cần cân đối với thời gian và chi phí.

## Đọc một ReAct trace

Hãy theo dõi ba sự kiện có thể kiểm chứng. Agent chọn tool nào, tool trả dữ liệu nào và agent quyết định tiếp tục hay dừng. Nếu tra cứu metadata cho một bộ phim, tool có thể trả tên đạo diễn và năm phát hành trong cùng một lượt. Nếu kết quả có hai phim trùng tên, agent có thể hỏi phiên bản hoặc thu hẹp truy vấn trước khi trả lời.

CoT xử lý một chuỗi bước lập luận, ToT khám phá nhiều nhánh, còn ReAct cập nhật quyết định dựa vào **observation** từ môi trường. Một trace cài đặt trong ứng dụng có thể ghi tool call, observation và quyết định định tuyến. Các sự kiện này đủ để tái hiện nhiều lỗi ngay cả khi model không cung cấp internal reasoning.

**Tự kiểm tra.** Với yêu cầu tìm lịch bảo trì mới nhất và tóm tắt ảnh hưởng, vì sao tra cứu nguồn là một bước cần thiết?
