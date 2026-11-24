# LangChain for AI Agents

Student Guide · What You’ve Learned · trang 89 · [Mục lục](README.md)

1. **LangChain** cung cấp giao diện thống nhất cho nhiều LLM providers.
2. `chain = prompt | model | StrOutputParser()`. Toán tử `|` nối các bước trong chain.
3. **LLM = Reasoning.** Model quyết định gọi tool nào và truyền arguments gì. Việc thực thi thuộc lớp application.
4. **Application = Execution.** LangChain phân tích tool request, chạy hàm Python rồi gửi kết quả về model.
5. **ReAct Loop** chạy theo vòng `Reason → Act → Observe → Repeat` đến khi model không cần gọi thêm tool.
6. **Conversation = State.** Mỗi message được thêm vào history. Trong flow của bài, toàn bộ history được gửi lại trong mỗi LLM API call.
7. **`agent.invoke()`** gói việc chuẩn bị schemas, gọi API, parsing và execution vào một lời gọi.

![Pipeline LangChain truyền output từ prompt đến model rồi qua StrOutputParser.](images/02-langchain-chain.png)
