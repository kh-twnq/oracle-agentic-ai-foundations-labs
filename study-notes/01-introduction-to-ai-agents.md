# Introduction to AI Agents

*Giới thiệu về AI agent*

Module 1 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), tr. 9–54 · [Mục lục](README.md)

## Agenda

*Nội dung học*

1. [AI agent là gì?](#1-what-is-an-ai-agent)
2. [Các thành phần cốt lõi của AI agent](#2-ai-agent-core-components)
3. [Các mẫu suy luận](#3-reasoning-patterns)
4. [Xây dựng AI agent đầu tiên](#4-building-your-first-ai-agent)
5. [An toàn và guardrail](#5-safety--guardrails)

Nội dung theo chương trình học ở tr. 10 của Student Guide. Xem [Ôn tập module](#module-review) để luyện các câu hỏi kiểm tra kỹ năng liên quan.

<a name="1-what-is-an-ai-agent"></a>

## 1. AI agent là gì?

**AI agent chọn hành động tiếp theo dựa trên mục tiêu và thông tin có được tại thời điểm đó.** **Agent dựa trên LLM kết hợp mô hình, tool và cơ chế điều phối vòng lặp.** Kết quả từ tool có thể làm đổi hướng xử lý của agent. (tr. 11–16)

| Hệ thống | Mức tự chủ và cách xử lý | Vai trò của tool |
| --- | --- | --- |
| Chatbot truyền thống | **Phản hồi từng lượt** theo kịch bản, FAQ hoặc ngữ cảnh chat. | Có thể tra một nguồn cấu hình sẵn để trả lời. |
| Workflow theo quy tắc | **Quy tắc của ứng dụng xác định trước các bước và điều kiện rẽ nhánh.** | Ứng dụng gọi dịch vụ tại các bước đã định. |
| AI agent | **Mô hình chọn bước tiếp theo dựa trên mục tiêu, ngữ cảnh và kết quả vừa quan sát.** Runtime giữ quyền thực thi trong các giới hạn của ứng dụng. | Mô hình có thể chọn tool và đối số ở mỗi vòng lặp, rồi điều chỉnh bước sau theo kết quả. |

Với cùng câu hỏi về trả hàng, chatbot có thể trả lời từ FAQ, workflow kiểm tra ngày giao theo một cây quyết định, còn agent có thể tra đơn, nhận ra đó là đơn quốc tế và tìm chính sách tương ứng. Khi phân loại, hãy xem ai quyết định bước tiếp theo và kết quả của tool có thể đổi hướng xử lý như thế nào.

<a name="2-ai-agent-core-components"></a>

## 2. Các thành phần cốt lõi của AI agent

| Thành phần | Trách nhiệm |
| --- | --- |
| **Mô hình** | Diễn giải mục tiêu, chọn tool và đối số, hoặc tạo câu trả lời. |
| **Tool** | Thực hiện các thao tác như truy xuất dữ liệu hoặc gọi API. Schema cho mô hình biết tool chấp nhận những đối số nào. |
| **Runtime của agent** | Chạy agent và duy trì trạng thái của nó. Cơ chế điều phối quản lý các lần gọi mô hình, việc thực thi tool và điều kiện dừng. |

![Mô hình đề xuất hành động, tool thực thi và cơ chế điều phối quản lý vòng lặp.](images/01-agent-components.png)

**Vòng lặp thực thi của agent** là `Perceive → Reason → Act → Observe`.

- **Perceive.** Tiếp nhận yêu cầu và ngữ cảnh liên quan.
- **Reason.** Chọn bước tiếp theo dựa trên thông tin hiện có.
- **Act.** Kiểm tra tính hợp lệ của lời gọi tool được đề xuất và thực thi nếu được phép.
- **Observe.** **Tiếp nhận kết quả của hành động trước và đưa kết quả đó vào lần ra quyết định tiếp theo.** Kết quả quan sát được có thể là dữ liệu trả về, kết quả rỗng hoặc lỗi của tool.

**Định tuyến tool (tool routing)** gồm chọn tool, chuẩn bị lời gọi, chuyển cho đúng hàm xử lý và đưa kết quả về vòng lặp. Ví dụ, sau khi gọi `get_order`, agent có thể tra chính sách trả hàng nếu đơn đã giao hoặc hỏi lại mã đơn khi kết quả rỗng.

Runtime có thể dừng khi có câu trả lời cuối cùng, chạm giới hạn số vòng lặp, gặp lỗi hoặc handoff cho người xử lý. (tr. 15–21)

**Trạng thái** ghi lại lượt chạy hiện tại, gồm các tin nhắn và kết quả từ tool. **Bộ nhớ ngắn hạn** giữ ngữ cảnh trong phiên. **Bộ nhớ dài hạn** có thể cung cấp thông tin từ những phiên trước hoặc từ kho tri thức. Khi chọn mô hình, cần cân bằng năng lực, chi phí và độ trễ. Chi phí và độ trễ có thể cộng dồn qua nhiều lần gọi trong một lượt chạy. (tr. 19–21, 53–54)

<a name="3-reasoning-patterns"></a>

## 3. Các mẫu suy luận

| Mẫu | Cách hoạt động | Hạn chế chính |
| --- | --- | --- |
| **Chain-of-Thought (CoT)** | Chia bài toán thành các bước suy luận trung gian. | Kết luận phụ thuộc vào thông tin mô hình có được. |
| **ReAct** | Luân phiên giữa suy luận, gọi tool và quan sát kết quả. | Mỗi lượt bổ sung làm tăng khối lượng xử lý, đồng thời cho phép đưa thêm dữ kiện mới vào. |
| **Tree-of-Thoughts (ToT)** | **Khám phá nhiều hướng giải khả dĩ rồi đánh giá chúng trước khi tiếp tục.** | Càng nhiều nhánh thì càng cần nhiều lần đánh giá. |

Khi hướng hiện tại bế tắc, Tree-of-Thoughts có thể quay lại một nhánh khác. Khám phá nhiều nhánh là một chiến lược tìm kiếm. Các lần đánh giá có thể chạy tuần tự. **Prompt tuần tự** chuyển đầu ra của một prompt sang prompt kế tiếp theo thứ tự đã định.

ReAct hữu ích khi quyết định tiếp theo phụ thuộc vào thông tin từ bên ngoài. Một kết quả quan sát được có thể làm thay đổi kế hoạch. Kết quả từ một tool cũng có thể trở thành đầu vào cho lần gọi tool sau. (tr. 22–27, 43–45)

<a name="4-building-your-first-ai-agent"></a>

## 4. Xây dựng AI agent đầu tiên

Trong LangChain, `init_chat_model()` chọn mô hình và `@tool` đăng ký các hàm. Định nghĩa tool cung cấp tên hàm, mô tả và schema tham số. `create_agent()` gắn mô hình với các tool. `agent.invoke()` chuyển tin nhắn của người dùng cho runtime. Kết quả từ một tool sau đó có thể cung cấp đối số cho lần gọi tiếp theo. (tr. 31–45)

<a name="defining-a-tools-input-schema"></a>

### Định nghĩa schema đầu vào của tool

**Khai báo kiểu (type hint) trong Python giúp LangChain tạo schema đầu vào cho tool.** Trong `get_order(order_id: str, include_items: bool = False)`, schema có thể mô tả `order_id` là chuỗi bắt buộc và `include_items` là giá trị boolean không bắt buộc, có giá trị mặc định. Docstring giải thích tool làm gì và khi nào nên dùng. Schema mô tả cấu trúc của một yêu cầu hợp lệ. Tool vẫn kiểm tra quyền và quy tắc nghiệp vụ trước khi truy cập đơn hàng. [Định nghĩa tool trong LangChain](https://docs.langchain.com/oss/python/langchain/tools)

LangChain và LangGraph hỗ trợ điều phối có trạng thái. OpenAI Agents SDK cung cấp runner, tracing và guardrail. CrewAI tổ chức agent theo vai trò. Smolagents cung cấp một framework gọn nhẹ. Lựa chọn phụ thuộc vào mức độ điều phối mà ứng dụng cần. (tr. 28–30) [Thực thi tool trong LangChain](02-langchain-for-ai-agents.md#3-langchain-agent-under-the-hood)

<a name="5-safety--guardrails"></a>

## 5. An toàn và guardrail

Tool có thể đọc dữ liệu hoặc tạo ra tác động bên ngoài. **Prompt injection** đưa chỉ dẫn vào thông qua dữ liệu. **Lạm dụng tool** là dùng tool ngoài mục đích đã định. **Đầu độc bộ nhớ** là lưu lại đầu vào có hại hoặc gây hiểu lầm. **Rò rỉ dữ liệu** làm lộ thông tin được bảo vệ. **Thực thi mất kiểm soát** tiêu tốn quá nhiều thời gian hoặc ngân sách. (tr. 46–50)

**Phòng thủ chiều sâu giảm rủi ro bằng nhiều lớp kiểm soát.** Ví dụ, kiểm tra quyền tại tool vẫn có thể chặn truy cập trái phép khi yêu cầu đã qua bước kiểm tra đầu vào.

| Lớp phòng thủ chiều sâu | Biện pháp kiểm soát |
| --- | --- |
| **Kiểm tra đầu vào** | Kiểm tra định dạng và tần suất yêu cầu. Xem nội dung truy xuất được là dữ liệu chưa đáng tin cậy. |
| **Guardrail cho LLM** | Đặt giới hạn hành vi và giới hạn các tool mà mô hình có thể dùng. |
| **Ranh giới của tool** | **Giới hạn thao tác tool được làm và dữ liệu tool được truy cập.** Áp dụng nguyên tắc đặc quyền tối thiểu, kiểm tra đối số, cô lập việc thực thi và yêu cầu người phê duyệt khi phù hợp. Dùng tính lũy đẳng để hạn chế tác động bị lặp khi thử lại. |
| **Lọc đầu ra** | Kiểm tra thông tin nhận dạng cá nhân (PII), nội dung nhạy cảm và mức độ liên quan. |
| **Khả năng quan sát** | Ghi lại trace, lỗi, độ trễ và chi phí. Che các giá trị nhạy cảm và giám sát giới hạn của lượt chạy. |

Ví dụ, hãy kiểm tra định dạng mã đơn hàng ngay khi yêu cầu đi vào ứng dụng. Khi tool tra cứu chạy, hãy kiểm tra người gọi có quyền truy cập chính đơn hàng đó hay không. Tool hoàn tiền cũng có thể yêu cầu phê duyệt trước khi hoàn tiền. Việc kiểm tra quyền cần diễn ra tại nơi thao tác tạo ra tác động. Giới hạn số vòng lặp của runtime kiểm soát agent được thử trong bao lâu. (tr. 51–54)

<a name="module-review"></a>

## Ôn tập module

### Q1. Defense in depth and tool boundaries

*Câu 1. Phòng thủ chiều sâu và ranh giới của tool*

Xem [An toàn và guardrail](#5-safety--guardrails).

- **Lớp nào giới hạn hành vi nguy hiểm của tool?** Ranh giới của tool thực thi các giới hạn ngay khi tool chạy, gồm hành động được phép, quyền truy cập dữ liệu và yêu cầu phê duyệt.
- **Nên kiểm tra quyền sở hữu đơn hàng ở đâu?** Tại ranh giới của tool hoặc dịch vụ. Mã đơn hàng hợp lệ vẫn có thể trỏ tới đơn mà người gọi không có quyền đọc.
- **Lớp nào xử lý yêu cầu đầu vào, câu trả lời cuối cùng hoặc trace của lượt chạy?** Kiểm tra đầu vào xử lý yêu cầu. Lọc đầu ra kiểm tra dữ liệu nhạy cảm trong câu trả lời. Khả năng quan sát ghi lại diễn biến để người vận hành xem xét.
- **Điều gì giúp hạn chế việc hoàn tiền trùng nếu lời gọi được thử lại?** Khóa lũy đẳng giúp dịch vụ nhận ra yêu cầu lặp và tránh hoàn tiền hai lần.

### Q2. Python type hints and tool schemas

*Câu 2. Khai báo kiểu trong Python và schema của tool*

Xem [Định nghĩa schema đầu vào của tool](#defining-a-tools-input-schema).

- **Khai báo kiểu có ích gì khi định nghĩa tool cho agent?** Framework như LangChain có thể dùng khai báo kiểu để tạo schema đầu vào cho tool. Nhờ đó mô hình biết tên và kiểu dữ liệu dự kiến của từng đối số.
- **Làm sao biết tham số nào bắt buộc trong ví dụ?** `order_id: str` không có giá trị mặc định nên người gọi phải cung cấp. `include_items: bool = False` có giá trị mặc định nên có thể bỏ qua.
- **Khai báo kiểu và docstring khác nhau thế nào?** Khai báo kiểu mô tả kiểu dữ liệu của đối số. Docstring mô tả tool làm gì và giúp mô hình quyết định khi nào nên gọi.
- **Một schema tool hợp lệ có xác lập quyền thực thi hành động không?** Việc xác thực schema kiểm tra cấu trúc đầu vào. Ứng dụng phải kiểm tra quyền và quy tắc nghiệp vụ trước khi thực thi hành động.

### Q3. Reasoning patterns

*Câu 3. Các mẫu suy luận*

Xem [Các mẫu suy luận](#3-reasoning-patterns).

- **Cách nào khám phá nhiều hướng giải khả dĩ?** Tree-of-Thoughts tạo nhánh, đánh giá các phương án và có thể quay lại nhánh khác nếu nhánh hiện tại bế tắc. [Bài báo Tree of Thoughts](https://proceedings.nips.cc/paper_files/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract-Conference.html)
- **Cách nào chia bài toán thành các bước suy luận trung gian?** Chain-of-Thought. Ví dụ điển hình sẽ lần lượt đi qua một chuỗi bước.
- **Cách nào cho phép kết quả từ tool thay đổi bước tiếp theo?** ReAct luân phiên giữa suy luận và hành động. Kết quả quan sát từ lời gọi tool cung cấp thông tin cho quyết định kế tiếp.
- **Khi nào prompt tuần tự phù hợp?** Khi có thể xác định trước các giai đoạn, chẳng hạn trích xuất các trường, kiểm tra chúng rồi định dạng kết quả.

### Q4. AI agent versus fixed workflow

*Câu 4. AI agent và workflow cố định*

Xem [AI agent là gì?](#1-what-is-an-ai-agent).

- **Điểm nào phân biệt agent với workflow cố định?** Agent chọn hành động tiếp theo trong lúc chạy, dựa trên mục tiêu, ngữ cảnh và kết quả quan sát. Workflow cố định áp dụng các quy tắc và nhánh đã định trước.
- **Workflow cố định có thể rẽ nhánh theo điều kiện không?** Có. Quy tắc “nếu đã giao hàng thì kiểm tra điều kiện trả hàng” vẫn là một nhánh đã định trước.
- **Thêm LLM vào một bước có biến workflow thành workflow do agent điều phối không?** Luồng điều khiển vẫn có thể cố định. Ví dụ, bước cuối đã định trước có thể dùng LLM để tóm tắt đơn hàng. Ứng dụng vẫn quyết định bước nào chạy tiếp.
- **Agent có thể tuân theo các quy tắc cố định không?** Có. Ví dụ, agent có thể tự chọn có tra cứu đơn hàng hay không, còn ứng dụng luôn yêu cầu phê duyệt trước khi hoàn tiền.

### Q5. Observe in the agent loop

*Câu 5. Bước Observe trong vòng lặp của agent*

Xem [Các thành phần cốt lõi của AI agent](#2-ai-agent-core-components).

- **Bước Observe dùng để làm gì?** Tiếp nhận và sử dụng kết quả của hành động trước, chẳng hạn phản hồi hoặc lỗi của tool, để có thêm thông tin cho quyết định tiếp theo.
- **Perceive và Observe khác nhau thế nào trong vòng lặp này?** Perceive tiếp nhận yêu cầu và ngữ cảnh liên quan. Observe nhận phản hồi từ hành động mà agent đã thực hiện.
- **Sau khi quan sát kết quả, agent có thể làm gì?** Agent có thể trả lời, chọn tool khác, hỏi thêm thông tin còn thiếu hoặc dừng theo quy tắc của runtime.
- **Quan sát kết quả từ tool có huấn luyện mô hình không?** Kết quả trở thành ngữ cảnh của lượt chạy hiện tại. Việc huấn luyện thay đổi tham số mô hình thông qua một quy trình riêng.
