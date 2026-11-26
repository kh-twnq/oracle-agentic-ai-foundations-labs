# LangChain for AI Agents

*LangChain cho AI agent*

Module 2 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), tr. 55–89 · [Mục lục](README.md)

## Agenda

*Nội dung học*

1. [Giới thiệu về LangChain](#1-introduction-to-langchain)
2. [Xây dựng agent đầu tiên bằng LangChain](#2-build-your-first-agent-using-langchain)
3. [Cách agent LangChain hoạt động bên trong](#3-langchain-agent-under-the-hood)

Nội dung theo chương trình học ở tr. 56 của Student Guide. Xem [Ôn tập module](#module-review) để luyện các biến thể của năm câu hỏi kiểm tra kỹ năng.

<a name="1-introduction-to-langchain"></a>

## 1. Giới thiệu về LangChain

LangChain cung cấp các thành phần để xây dựng ứng dụng LLM. Một **chain** nối các bước theo trình tự đã định. Một **agent** cho phép mô hình chọn hành động tiếp theo trong lúc chạy. **Retrieval-Augmented Generation (RAG)** đưa nội dung truy xuất được vào ngữ cảnh của mô hình. (tr. 57–59)

| Thành phần | Mục đích |
| --- | --- |
| **LangChain** | Kết hợp mô hình, prompt, chain, tool và bộ nhớ. |
| **LangGraph** | Biểu diễn trạng thái, nhánh và vòng lặp dưới dạng đồ thị. |
| **LangSmith** | Hỗ trợ tracing, kiểm tra chi tiết, kiểm thử và gỡ lỗi. |
| **Tích hợp** | Kết nối với nhà cung cấp mô hình, cơ sở dữ liệu, API tìm kiếm và các dịch vụ khác. |

<a name="unified-model-interface"></a>

### Giao diện mô hình thống nhất

**Giao diện mô hình thống nhất giúp lập trình viên chuyển nhà cung cấp với ít thay đổi trong mã ứng dụng.** `init_chat_model()` nhận định danh mô hình có tiền tố chỉ nhà cung cấp. Mã ứng dụng vẫn có thể gọi `model.invoke(...)`. Thành phần tích hợp được chọn sẽ chuyển đổi yêu cầu sang định dạng của nhà cung cấp tương ứng. (tr. 60, 71, 89)

Khi đổi nhà cung cấp, có thể vẫn phải thay gói tích hợp, thông tin xác thực và cấu hình mô hình. Hãy kiểm tra mô hình mới có hỗ trợ các tính năng ứng dụng đang dùng hay không, chẳng hạn gọi tool hoặc trả đầu ra có cấu trúc. Chất lượng phản hồi, giới hạn ngữ cảnh, chi phí và độ trễ có thể khác nhau. Nếu cần tinh chỉnh mô hình, đó là một thao tác riêng. [Mô hình trong LangChain](https://docs.langchain.com/oss/python/langchain/models)

<a name="prompt-templates-and-lcel"></a>

### Mẫu prompt và LCEL

`PromptTemplate` điền giá trị cho các biến trong văn bản. `ChatPromptTemplate` tạo tin nhắn theo vai trò cho chỉ dẫn hệ thống, đầu vào của người dùng và các phản hồi AI trước đó. **Prompt few-shot** dùng các cặp đầu vào và đầu ra để minh họa hành vi mong muốn. (tr. 61)

**LangChain Expression Language (LCEL) dùng toán tử pipe `|` để nối các thành phần. Đầu ra của mỗi bước trở thành đầu vào của bước tiếp theo.** Trong một chuỗi điển hình, mẫu prompt tạo tin nhắn, mô hình sinh phản hồi, rồi `StrOutputParser()` trích xuất văn bản từ phản hồi đó. (tr. 62, 89)

```python
chain = prompt | model | StrOutputParser()
answer = chain.invoke({"question": "What is the return policy?"})
```

Thành phần đầu tiên nhận đầu vào truyền vào `invoke()`. Thành phần cuối cùng quyết định đầu ra của chain. Nếu thành phần tiếp theo cần dữ liệu có cấu trúc khác, hãy thêm một bước chuyển đổi. Chain truy xuất cũng có thể chứa một retriever để lấy tài liệu từ kho vector. LCEL nối các bước với nhau. Kho vector đảm nhiệm việc lưu trữ và tìm kiếm. [RunnableSequence](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableSequence)

![LCEL chuyển prompt đã chuẩn bị cho mô hình rồi chuyển phản hồi cho StrOutputParser.](images/02-langchain-chain.png)

<a name="2-build-your-first-agent-using-langchain"></a>

## 2. Xây dựng agent đầu tiên bằng LangChain

Một lời gọi mô hình cơ bản trả về đầu ra dựa trên đầu vào. Agent có thể hành động, quan sát kết quả rồi dùng thông tin đó để chọn bước tiếp theo. Đây là **ReAct**. Cách này phù hợp với những tác vụ phụ thuộc vào dữ liệu hiện tại hoặc kết quả trung gian. (tr. 63–65, 70)

| Siêu dữ liệu hoặc phần triển khai của tool | Mục đích |
| --- | --- |
| `@tool` | Đăng ký một hàm Python làm tool có thể gọi. |
| Tên hàm và khai báo kiểu | Xác định tool, các trường đầu vào và kiểu dữ liệu của chúng. |
| Docstring | Mô tả tool làm gì và khi nào nên chọn nó. |
| Khai báo kiểu trả về | Mô tả kiểu của kết quả dự kiến. |
| Thân hàm | Thực hiện thao tác khi ứng dụng gọi hàm. |

Định nghĩa tool gửi cho mô hình mô tả tên, mục đích và các đối số được chấp nhận. Trong định dạng API dùng ở khóa học, chúng xuất hiện dưới dạng `name`, `description` và `parameters`. Schema tham số cho biết những đầu vào nào bắt buộc. `create_agent()` cấu hình mô hình và tool cho agent. `agent.invoke()` bắt đầu một lượt chạy với các tin nhắn được cung cấp. (tr. 66–74)

<a name="3-langchain-agent-under-the-hood"></a>

## 3. Cách agent LangChain hoạt động bên trong

<a name="first-model-request"></a>

### Yêu cầu đầu tiên gửi tới mô hình

**Trong lần gọi mô hình đầu tiên, LangChain gửi tin nhắn của người dùng và định nghĩa các tool hiện có.** Mô hình cũng có thể nhận chỉ dẫn hệ thống và các tin nhắn trước đó nếu ứng dụng cung cấp. Trong định dạng API minh họa ở khóa học, tin nhắn nằm trong `messages` và định nghĩa tool nằm trong `tools`. (tr. 74–77)

Với yêu cầu tra cứu trạng thái đơn hàng, mô hình có thể nhận câu hỏi “Đơn hàng ORD-42 đang ở đâu?” cùng định nghĩa cho biết `get_order` nhận một chuỗi `order_id`. Định nghĩa mô tả cách yêu cầu thao tác. Phần triển khai Python và cơ sở dữ liệu đơn hàng nằm ở phía ứng dụng.

<a name="tool-call-and-execution"></a>

### Gọi và thực thi tool

**Mô hình có thể đề xuất một lời gọi tool. LangChain chạy hàm Python đã đăng ký trong ứng dụng.** Mô hình trả về tên tool, đối số và ID lời gọi. Trong phản hồi API minh họa ở khóa học, các đối số được mã hóa dưới dạng chuỗi JSON. `AIMessage.tool_calls` của LangChain chuẩn hóa lời gọi và biểu diễn các đối số đã phân tích dưới dạng dictionary. (tr. 78–85, 87–89) [Mô hình trong LangChain](https://docs.langchain.com/oss/python/langchain/models)

1. Mô hình yêu cầu gọi `get_order` với `order_id="ORD-42"`.
2. Runtime tìm tool đã đăng ký theo tên và chạy tool với các đối số được cung cấp. Ứng dụng có thể thực thi quy tắc phân quyền hoặc yêu cầu phê duyệt cho một số hành động.
3. Runtime ghi kết quả dưới dạng `ToolMessage`. `tool_call_id` liên kết kết quả với yêu cầu ban đầu.
4. Lần gọi mô hình tiếp theo nhận danh sách tin nhắn đã cập nhật. Mô hình có thể trả lời dựa trên kết quả hoặc yêu cầu gọi tool khác.

Nếu mô hình đưa ra câu trả lời cuối cùng ngay lần gọi đầu tiên, runtime có thể kết thúc mà không thực thi tool nào. [Agent trong LangChain](https://docs.langchain.com/oss/python/langchain/agents)

<a name="debugging-and-production-optimization"></a>

### Gỡ lỗi và tối ưu khi vận hành thực tế

**Hiểu các bước bên trong `agent.invoke()` giúp lập trình viên khoanh vùng lỗi và đo thời gian, chi phí phát sinh ở từng bước.** Hãy kiểm tra định nghĩa tool, đối số do mô hình đề xuất, hàm đã chạy và kết quả được thêm vào lịch sử tin nhắn. Trình tự này cũng hữu ích khi cần tùy chỉnh vòng lặp. (tr. 85–89)

| Dấu hiệu | Nên kiểm tra gì trước? |
| --- | --- |
| Mô hình chọn sai tool. | Kiểm tra mô tả và danh sách tool được cung cấp trong lần gọi đó. |
| Mô hình truyền đối số không hợp lệ. | Đối chiếu các đối số được yêu cầu với schema đầu vào và lỗi xác thực. |
| Tool đã chạy nhưng câu trả lời bỏ qua kết quả. | Kiểm tra kết quả đã được thêm vào yêu cầu tiếp theo gửi tới mô hình với đúng ID lời gọi hay chưa. |
| Lượt chạy chậm hoặc tốn kém. | Đo riêng các lần gọi mô hình và các lần gọi tool. Kiểm tra số vòng lặp và kích thước ngữ cảnh gửi đi trong mỗi lần gọi. |

<a name="module-review"></a>

## Ôn tập module

### Q1. Unified model interface

*Câu 1. Giao diện mô hình thống nhất*

Xem [Giao diện mô hình thống nhất](#unified-model-interface).

- **Vì sao LangChain cung cấp một giao diện thống nhất?** Giao diện này giữ cách dùng các thao tác phổ biến như `invoke()` nhất quán, nên khi đổi nhà cung cấp có thể sửa ít mã gọi hơn.
- **Khi đổi nhà cung cấp, vẫn có thể phải thay đổi những gì?** Cấu hình mô hình, gói tích hợp và thông tin xác thực. Cũng cần kiểm tra các tính năng mà ứng dụng phụ thuộc vào có được hỗ trợ hay không.
- **Hai nhà cung cấp có thể trả kết quả khác nhau cho cùng một đầu vào không?** Có. Giao diện chung chuẩn hóa cách ứng dụng gọi mô hình. Mỗi mô hình vẫn có thể phản hồi theo cách khác nhau.
- **Đổi nhà cung cấp có huấn luyện mô hình trên dữ liệu của ứng dụng không?** Việc chuyển đổi chỉ chọn một tích hợp mô hình khác. Tinh chỉnh mô hình là một quy trình riêng.

### Q2. LCEL and chains

*Câu 2. LCEL và chain*

Xem [Mẫu prompt và LCEL](#prompt-templates-and-lcel).

- **Toán tử `|` làm gì trong LCEL?** Nó nối các thành phần để đầu ra của một bước trở thành đầu vào của bước tiếp theo.
- **Dữ liệu đi qua `prompt | model | StrOutputParser()` như thế nào?** Các biến của prompt được dùng để tạo tin nhắn cho mô hình. Mô hình trả về phản hồi. Bộ phân tích trích xuất phần văn bản.
- **Nếu thành phần tiếp theo cần đầu vào có cấu trúc khác thì sao?** Thêm một bước chuyển đổi để tạo đúng cấu trúc mà thành phần đó yêu cầu.
- **LCEL có vai trò gì trong chain truy xuất?** LCEL nối các bước truy xuất và sinh nội dung. Retriever lấy tài liệu liên quan từ nguồn dữ liệu, chẳng hạn kho vector.

### Q3. Debugging and optimizing agent runs

*Câu 3. Gỡ lỗi và tối ưu lượt chạy của agent*

Xem [Gỡ lỗi và tối ưu khi vận hành thực tế](#debugging-and-production-optimization).

- **Vì sao cần hiểu điều gì xảy ra bên trong `agent.invoke()`?** Để khoanh vùng lỗi và xác định lần gọi mô hình, lần gọi tool hoặc bước lặp nào làm tăng độ trễ và chi phí.
- **Nên xem ở đâu nếu mô hình chọn sai tool?** Kiểm tra các tool được cung cấp trong lần gọi đó, mô tả của chúng và các tin nhắn mô hình nhận được.
- **Nên xem ở đâu nếu tool chạy thành công nhưng câu trả lời bỏ qua kết quả?** Kiểm tra kết quả của tool đã được đưa vào lần gọi mô hình tiếp theo và liên kết với đúng ID lời gọi hay chưa.
- **Nên đo gì trước khi tìm cách tăng tốc lượt chạy?** Đo số lượng và thời gian của các lần gọi mô hình và tool, cùng kích thước ngữ cảnh. Phần chậm nhất có thể nằm ở dịch vụ phía sau hoặc do agent chạy nhiều vòng lặp.

### Q4. What the first model request contains

*Câu 4. Nội dung của yêu cầu đầu tiên gửi tới mô hình*

Xem [Yêu cầu đầu tiên gửi tới mô hình](#first-model-request).

- **Trong ví dụ của khóa học, yêu cầu đầu tiên gửi tới mô hình gồm gì?** Tin nhắn của người dùng và các định nghĩa tool hiện có. Nếu được cung cấp, chỉ dẫn hệ thống hoặc tin nhắn trước đó cũng có thể được đưa vào.
- **Mô hình biết gì về `get_order` từ yêu cầu đó?** Tên, mô tả và các đối số mà tool chấp nhận. Dựa vào đó, mô hình quyết định có nên yêu cầu gọi tool hay không và điền `order_id` như thế nào.
- **Khi nào trạng thái đơn hàng được thêm vào cuộc hội thoại?** Sau khi ứng dụng chạy `get_order` và thêm kết quả dưới dạng tin nhắn tool cho lần gọi mô hình tiếp theo.
- **Agent có thể kết thúc sau lần gọi mô hình đầu tiên không?** Có. Mô hình có thể đưa ra câu trả lời cuối cùng khi ngữ cảnh hiện có đã đủ.

### Q5. Tool request versus tool execution

*Câu 5. Yêu cầu gọi tool và thực thi tool*

Xem [Gọi và thực thi tool](#tool-call-and-execution).

- **Vì sao mô hình trả về một lời gọi tool?** Để đề xuất hành động bằng cách chỉ rõ tên tool và cung cấp các đối số. Ứng dụng quản lý và thực thi hàm đã đăng ký.
- **Mô hình có thể yêu cầu gọi một hàm Python tùy chỉnh không?** Có, nếu ứng dụng đăng ký hàm đó làm tool và cung cấp định nghĩa của nó cho mô hình.
- **Runtime ghép nhiều kết quả tool với các yêu cầu tương ứng như thế nào?** Mỗi `ToolMessage` sử dụng `tool_call_id` của yêu cầu mà tin nhắn đó phản hồi.
- **Khi nào cần người phê duyệt?** Khi ứng dụng đặt quy tắc phê duyệt cho hành động đó. Ví dụ, ứng dụng có thể cho phép tra cứu đơn hàng ngay nhưng yêu cầu phê duyệt trước khi hoàn tiền.
