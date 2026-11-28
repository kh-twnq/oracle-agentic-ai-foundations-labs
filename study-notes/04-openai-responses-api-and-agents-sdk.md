# OpenAI Responses API and Agents SDK

*OpenAI Responses API và Agents SDK*

Module 4 · [Student Guide D1114464GC10](https://mylearn.oracle.com/ekit/163240/163512/66a3c548-2f85-4e05-b3b6-c6327492f4d3/course), tr. 123–162 · [Mục lục](README.md)

## Agenda

*Nội dung học*

1. [Kiến trúc agent của OpenAI](#1-openai-agent-stack)
2. [OpenAI Responses API](#2-openai-responses-api)
3. [OpenAI Agents SDK](#3-openai-agents-sdk)
4. [Tool và gọi hàm](#4-tools-and-function-calling)
5. [Hệ thống nhiều agent dùng handoff](#5-multi-agent-systems-with-handoffs)
6. [Guardrail và an toàn](#6-guardrails-and-safety)
7. [Kết hợp các thành phần](#7-putting-it-all-together)

Nội dung theo chương trình học ở tr. 124 của Student Guide. Xem [Ôn tập module](#module-review) để luyện các biến thể của năm câu hỏi kiểm tra kỹ năng.

<a name="1-openai-agent-stack"></a>

## 1. Kiến trúc agent của OpenAI

**Kiến trúc agent của OpenAI** tách ứng dụng, runtime và API mô hình thành các lớp riêng. Ứng dụng quản lý quy tắc nghiệp vụ và quyền truy cập. **Responses API** gửi đầu vào cho mô hình và trả về đầu ra có cấu trúc. **Agents SDK** dùng API này để điều phối các lượt chạy agent có nhiều bước. (tr. 125–129)

| Giao diện | Ai quyết định bước tiếp theo? | Trường hợp sử dụng điển hình |
| --- | --- | --- |
| **Gọi trực tiếp Responses API** | Mã ứng dụng đọc phản hồi và quyết định các lời gọi tiếp theo. | Trả lời một lần, chạy workflow có các bước định trước hoặc dùng vòng lặp tùy chỉnh mà ứng dụng đã quản lý. |
| **Agents SDK** | Runner đã cấu hình quản lý vòng lặp của agent, gồm các tool dựa trên hàm của ứng dụng và các handoff. | **Workflow cần điều phối agent, guardrail hoặc phối hợp giữa nhiều agent.** |

Responses API cũng hỗ trợ gọi tool và sử dụng ngữ cảnh qua nhiều lượt. Khi gọi API trực tiếp, ứng dụng tự thực thi các tool tùy chỉnh và gửi yêu cầu tiếp theo. Lựa chọn phụ thuộc vào phần điều phối mà ứng dụng muốn giao cho SDK.

![Kiến trúc agent của OpenAI gồm Responses API, Agents SDK, guardrail và tracing.](images/04-openai-agent-stack.png)

## 2. OpenAI Responses API

`client.responses.create()` nhận mô hình cùng đầu vào dạng văn bản hoặc có cấu trúc. Phản hồi chứa các **mục đầu ra** để xử lý theo cấu trúc, chẳng hạn tin nhắn hoặc lời gọi hàm. Thuộc tính `response.output_text` giúp đọc nhanh phần văn bản của phản hồi. (tr. 130–132)

<a name="continuing-a-conversation"></a>

### Tiếp tục cuộc hội thoại

**`previous_response_id` liên kết yêu cầu mới với một phản hồi trước đó để mô hình tiếp tục sử dụng ngữ cảnh hội thoại đã có.** Yêu cầu tiếp theo gửi đầu vào mới và tham chiếu `id` của phản hồi liền trước. Nhờ vậy, ứng dụng không phải gửi lại toàn bộ lịch sử theo cách thủ công ở mỗi yêu cầu. (tr. 133–135)

```python
first = client.responses.create(
    model=model,
    input="Explain how an order return works.",
)

second = client.responses.create(
    model=model,
    previous_response_id=first.id,
    input="What happens if the order contains two items?",
)
```

Mỗi yêu cầu có thể cung cấp `instructions` cấp cao nhất của riêng nó. Nếu vẫn cần áp dụng cùng chỉ dẫn, hãy truyền lại trong yêu cầu tiếp theo. Các token đầu vào trước đó trong chuỗi vẫn được tính phí đầu vào. Ứng dụng cũng có thể tự quản lý lịch sử bằng cách truyền các mục trước đó có liên quan vào `input`. [Trạng thái hội thoại](https://developers.openai.com/api/docs/guides/conversation-state)

### Tools in a response

*Tool trong phản hồi*

Các tool tích hợp sẵn có thể gồm Web Search, File Search, Code Interpreter, Computer Use và Image Generation. Ứng dụng khai báo những tool khả dụng cho yêu cầu. Mô hình có thể yêu cầu gọi tool hoặc trả lời trực tiếp. Với hàm do ứng dụng định nghĩa, ứng dụng đọc mục `function_call`, kiểm tra tên và đối số rồi thực thi hàm. Yêu cầu tiếp theo gửi mục `function_call_output` có cùng `call_id`. Mô hình dùng kết quả này để trả lời hoặc yêu cầu bước khác. (tr. 133–135) [Gọi hàm qua Responses API](https://developers.openai.com/api/docs/guides/function-calling)

## 3. OpenAI Agents SDK

`Agent` chứa chỉ dẫn, mô hình và các tool. **Runner** gửi đầu vào tới mô hình, thực thi các tool dựa trên hàm được yêu cầu rồi gửi kết quả trở lại mô hình. Runner lặp lại quy trình cho đến khi lượt chạy hoàn tất hoặc gặp điều kiện dừng. (tr. 136–141)

`Runner.run_sync()` chạy đồng bộ. `Runner.run()` chạy bất đồng bộ. Khi lượt chạy hoàn tất, kết quả cuối cùng nằm trong `result.final_output`. (tr. 138–141)

<a name="4-tools-and-function-calling"></a>

## 4. Tool và gọi hàm

| Loại tool | Thành phần nào thực hiện công việc? |
| --- | --- |
| **Tool do nền tảng cung cấp (Hosted Tools)** | Nền tảng cung cấp và thực thi tính năng như Web Search hoặc Code Interpreter. |
| **Tool dựa trên hàm (Function Tools)** | Hàm Python của ứng dụng thực hiện thao tác. `@function_tool` cung cấp định nghĩa của hàm cho agent. |
| **Agent dưới dạng tool (Agents as Tools)** | `Agent.as_tool()` cung cấp một agent chuyên trách dưới dạng tool. Kết quả được trả về cho agent đã gọi nó. |

<a name="function-tool-schemas"></a>

### Schema của tool dựa trên hàm

**`@function_tool` dùng khai báo kiểu của các tham số Python để tự động tạo schema đầu vào cho tool.** Ví dụ, `get_order(order_id: str, include_items: bool)` tạo đầu vào gồm một chuỗi và một giá trị boolean. Docstring có thể mô tả tool và các đối số để mô hình biết khi nào nên gọi và gọi như thế nào. Khai báo kiểu mô tả đầu vào cho cả hàm đồng bộ và hàm bất đồng bộ. [Tool trong Agents SDK](https://openai.github.io/openai-agents-python/tools/)

Schema mô tả các đối số hợp lệ. Thân hàm thực hiện thao tác và áp dụng các quy tắc nghiệp vụ. Ví dụ, mã đơn hàng có thể đúng kiểu dữ liệu nhưng trỏ tới đơn mà người gọi không có quyền xem.

Runner chuyển kết quả trung gian từ tool về cho mô hình, để những lần gọi sau có thể sử dụng các kết quả đó. (tr. 142–148) [Thực thi tool trong LangChain](02-langchain-for-ai-agents.md#3-langchain-agent-under-the-hood)

### Thực hành gọi hàm qua Runner

Cài dependencies theo [hướng dẫn lab](../labs/README.md#reproduce-the-local-runs) và đặt `OPENAI_API_KEY` cho lần chạy thật. Runner đăng ký schema, thực thi hàm khi mô hình yêu cầu rồi chuyển kết quả về cho mô hình.

```python
from agents import Agent, Runner, function_tool

@function_tool
def multiply(a: int, b: int) -> int:
    """Nhân hai số nguyên."""
    return a * b

agent = Agent(
    name="MathAgent",
    model="gpt-4o-mini",
    instructions="Dùng tool multiply khi tính phép nhân.",
    tools=[multiply],
)
result = Runner.run_sync(agent, "Tính 15 × 8.", max_turns=4)
print(result.final_output)
```

Kiểm tra tool nhận 15 và 8, trả về 120, và câu trả lời cuối dùng kết quả đó. Lab gốc có thêm trường hợp nhiều lượt gọi hàm và lỗi đầu vào. [Lab function tools](https://github.com/oracle-university-labs/ou-generativeai-pro/blob/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/OpenAI/05_function_tools.py) · [Kết quả chạy fixture](../labs/README.md#results)

<a name="5-multi-agent-systems-with-handoffs"></a>

## 5. Hệ thống nhiều agent dùng handoff

**Phân luồng (triage)** chuyển yêu cầu đến agent chuyên trách phù hợp. Mẫu điều phối quyết định agent nào điều khiển lượt chạy hiện tại sau khi phân luồng. (tr. 149–152)

| Mẫu | Agent nào điều khiển lượt xử lý? | Cách cấu hình |
| --- | --- | --- |
| **Mẫu agent quản lý (Manager pattern)** | **Agent quản lý giữ quyền điều khiển, giao các tác vụ có phạm vi rõ ràng cho agent chuyên trách và có thể tổng hợp kết quả thành câu trả lời cuối cùng.** | Cung cấp các agent chuyên trách cho agent quản lý qua `Agent.as_tool()`. |
| **Handoff** | Agent chuyên trách tiếp quản và có thể trả lời trực tiếp cho người dùng. | Liệt kê các agent đích trong `handoffs`. Dùng `handoff_description` để mô tả khi nào nên chuyển yêu cầu đến từng agent chuyên trách. |

Ví dụ, agent quản lý hỗ trợ khách hàng có thể hỏi agent Đơn hàng về trạng thái giao hàng, hỏi agent Trả hàng về chính sách trả hàng rồi tổng hợp kết quả. Nếu agent Trả hàng cần trực tiếp xử lý phần còn lại của lượt người dùng, agent phân luồng có thể handoff cho agent đó. Trong cả hai mẫu, các agent chuyên trách đều có thể có tool riêng. Trong lab handoff, `result.last_agent.name` cho biết agent nào hoàn tất lượt chạy. [Điều phối agent](https://openai.github.io/openai-agents-python/multi_agent/) · [Lab handoff](https://github.com/oracle-university-labs/ou-generativeai-pro/blob/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/OpenAI/06_multi_agent_handoffs.py)

<a name="6-guardrails-and-safety"></a>

## 6. Guardrail và an toàn

| Guardrail | Thời điểm và phạm vi | Ví dụ |
| --- | --- | --- |
| **Đầu vào của agent** | Kiểm tra yêu cầu tại agent đầu tiên. Dùng `run_in_parallel=False` nếu lượt chạy phải chờ kết quả kiểm tra. | Chặn yêu cầu ngoài phạm vi hỗ trợ. |
| **Đầu ra của agent** | Kiểm tra câu trả lời từ agent tạo đầu ra cuối cùng, kể cả khi lượt chạy đã handoff. | Chặn nội dung chứa dữ liệu nhạy cảm trước khi trả cho người dùng. |
| **Đầu vào của function tool** | Chạy trước mỗi lần gọi tool có gắn guardrail. | Kiểm tra người gọi có quyền xem đơn cụ thể trước khi đọc dữ liệu. |
| **Đầu ra của function tool** | Chạy sau khi tool thực thi, trước khi kết quả được dùng tiếp. | Thay kết quả chứa dữ liệu nhạy cảm bằng thông báo an toàn. |

`@input_guardrail` hoặc `@output_guardrail` có thể trả về `GuardrailFunctionOutput(tripwire_triggered=True, ...)` để Runner dừng lượt chạy. Dùng `@tool_input_guardrail` và `@tool_output_guardrail` để định nghĩa kiểm tra, rồi gắn vào `tool_input_guardrails` và `tool_output_guardrails` của function tool. Guardrail của function tool có thể từ chối lời gọi hoặc kết quả và cho agent tiếp tục với thông báo thay thế, hoặc dừng lượt chạy bằng tripwire. Khi một thao tác có tác động bên ngoài, kiểm tra quyền và điều kiện thực thi trước khi gọi tool. Guardrail đầu ra chạy sau thao tác. Áp dụng quy tắc tại lớp thực thi tương ứng cho hosted tool và handoff. (tr. 153–156) [Phạm vi và chế độ chạy guardrail](https://openai.github.io/openai-agents-python/guardrails/) · [Lab guardrail đầu vào](https://github.com/oracle-university-labs/ou-generativeai-pro/blob/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations/OpenAI/07_guardrails.py)

### Tracing

**Tracing ghi lại diễn biến của lượt chạy agent để lập trình viên theo dõi quá trình thực thi và gỡ lỗi.** Một **trace** nhóm các thao tác liên quan. Một **span** biểu diễn một thao tác riêng lẻ, chẳng hạn lần sinh nội dung của mô hình, lời gọi tool dựa trên hàm, một handoff hoặc một lần kiểm tra guardrail. (tr. 155–156)

Ví dụ, nếu yêu cầu trả hàng xử lý chậm, hãy xem các span để xác định độ trễ đến từ lần gọi mô hình, guardrail hay bước tra cứu đơn hàng. Guardrail có thể dừng lượt chạy. Span tương ứng ghi lại diễn biến. [Tracing trong Agents SDK](https://openai.github.io/openai-agents-python/tracing/)

<a name="7-putting-it-all-together"></a>

## 7. Kết hợp các thành phần

Một hệ thống hỗ trợ khách hàng kết hợp guardrail đầu vào, agent phân luồng và các agent chuyên trách về trạng thái đơn hàng, hoàn tiền hoặc câu hỏi thường gặp. Guardrail kiểm tra yêu cầu có nằm trong phạm vi xử lý hay không. Agent phân luồng chọn agent chuyên trách. Agent chuyên trách gọi hàm hoặc tool tìm kiếm phù hợp rồi dùng kết quả để trả lời. (tr. 157–162)

Trace liên kết quyết định phân luồng với tool được chọn và câu trả lời cuối cùng. Trace cũng cho thấy độ trễ đến từ lần gọi mô hình, guardrail hay chính hàm được gọi. (tr. 159–161)

<a name="module-review"></a>

## Ôn tập module

### Q1. Manager pattern and handoffs

*Câu 1. Mẫu agent quản lý và handoff*

Xem [Hệ thống nhiều agent dùng handoff](#5-multi-agent-systems-with-handoffs).

- **Agent quản lý trung tâm làm gì?** Nó giao việc cho các agent chuyên trách, nhận kết quả và giữ quyền điều khiển lượt xử lý.
- **Khi nào nên dùng handoff?** Khi agent chuyên trách cần tiếp quản và trực tiếp xử lý phần còn lại của lượt hiện tại.
- **Khi dùng `Agent.as_tool()`, quyền điều khiển quay về đâu?** Kết quả của agent chuyên trách được trả về cho agent đã gọi nó. Agent gọi có thể quyết định bước tiếp theo.
- **Mẫu agent quản lý có quyết định cách các agent chuyên trách lên lịch hoặc sử dụng tool không?** Mẫu này xác định ai điều khiển lượt xử lý. Tool, quyền và lịch thực thi phụ thuộc vào cấu hình của agent và ứng dụng.

### Q2. Type hints and function tool definitions

*Câu 2. Khai báo kiểu và định nghĩa tool dựa trên hàm*

Xem [Schema của tool dựa trên hàm](#function-tool-schemas).

- **Vì sao khai báo kiểu quan trọng với `@function_tool`?** SDK đọc khai báo kiểu để suy ra các kiểu dữ liệu dự kiến và tạo schema đầu vào của tool.
- **Docstring có vai trò gì?** Nó giải thích tool làm gì và có thể mô tả từng đối số để giúp mô hình chọn và gọi tool.
- **Có thể dùng một hàm bất đồng bộ làm tool không?** Có. Khai báo kiểu định nghĩa các đối số. Định nghĩa hàm quyết định phần triển khai chạy đồng bộ hay bất đồng bộ.
- **Ai kiểm tra người gọi có quyền truy cập đơn hàng hay không?** Tool hoặc dịch vụ của ứng dụng thực thi quy tắc phân quyền đó. Schema có thể mô tả mã đơn hàng là một chuỗi.

### Q3. Tracing and debugging

*Câu 3. Tracing và gỡ lỗi*

Xem [Tracing](#tracing).

- **Vì sao nên bật tracing?** Tracing cho thấy các bước agent đã thực hiện và giúp tìm ra lỗi, quyết định phân luồng bất ngờ hoặc thao tác chạy chậm.
- **Trace và span khác nhau thế nào?** Trace nhóm các thao tác liên quan. Span ghi lại một thao tác riêng lẻ, chẳng hạn lời gọi tool hoặc một handoff.
- **Nên kiểm tra ở đâu nếu agent chọn đúng agent chuyên trách nhưng dùng dữ liệu cũ để trả lời?** Theo dõi handoff đến agent chuyên trách rồi kiểm tra bước tra cứu và kết quả trả về cho agent, nếu trace có ghi lại các chi tiết đó.
- **Thành phần nào dừng yêu cầu không được phép và thành phần nào ghi lại sự kiện?** Guardrail có thể dừng lượt chạy khi điều kiện chặn được kích hoạt. Tracing ghi lại sự kiện guardrail để xem xét.

### Q4. Conversation chaining

*Câu 4. Nối các lượt hội thoại*

Xem [Tiếp tục cuộc hội thoại](#continuing-a-conversation).

- **`previous_response_id` làm gì?** Nó liên kết yêu cầu mới với phản hồi trước để mô hình tiếp tục sử dụng ngữ cảnh đã có.
- **Cần đưa ID nào vào yêu cầu tiếp theo?** Dùng `id` của phản hồi mà bạn muốn tiếp tục từ đó. ID này xác định một phản hồi trong chuỗi.
- **`instructions` cấp cao nhất của yêu cầu trước có tự được áp dụng tiếp không?** `instructions` cấp cao nhất áp dụng cho yêu cầu cung cấp chúng. Hãy gửi lại nếu yêu cầu tiếp theo cần cùng chỉ dẫn.
- **Chỉ gửi đầu vào mới thì có được dùng miễn phí ngữ cảnh trước đó không?** Các token đầu vào trước đó trong chuỗi vẫn được tính phí đầu vào. ID phản hồi giúp bạn khỏi phải gửi lại toàn bộ lịch sử theo cách thủ công.

### Q5. Responses API versus Agents SDK

*Câu 5. Responses API và Agents SDK*

Xem [Kiến trúc agent của OpenAI](#1-openai-agent-stack).

- **Theo cách phân loại trong khóa học, khi nào Agents SDK phù hợp hơn?** Khi ứng dụng cần runner để quản lý các bước của agent, guardrail hoặc việc phối hợp giữa các agent.
- **Khi nào chỉ cần gọi trực tiếp Responses API?** Khi ứng dụng cần một phản hồi hoặc đã tự điều khiển được các bước trong workflow.
- **Tích hợp trực tiếp Responses API có dùng được tool tùy chỉnh không?** Có. Mô hình có thể yêu cầu gọi hàm. Ứng dụng thực thi hàm rồi trả kết quả trong một lời gọi API tiếp theo.
- **Chỉ riêng việc hội thoại nhiều lượt có đòi hỏi Agents SDK không?** Responses API có thể duy trì ngữ cảnh qua `previous_response_id`. SDK hữu ích khi ứng dụng còn cần điều phối, chẳng hạn quản lý vòng lặp gọi tool hoặc các handoff.
