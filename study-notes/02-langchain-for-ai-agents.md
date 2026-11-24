# LangChain for AI Agents

Student Guide · What You’ve Learned · trang 89 · [Mục lục](README.md)

- **LangChain** cung cấp giao diện thống nhất cho nhiều LLM providers.
- **Chain** nối các bước bằng toán tử pipe trong biểu thức `prompt | model | StrOutputParser()`.
- **Tool call** do model đề xuất, gồm tên tool và arguments. LangChain đọc request, gọi hàm Python ở phía application rồi đưa kết quả về model.
- **ReAct loop** lặp qua Reason, Act và Observe cho đến khi model đủ thông tin để trả lời.
- **Conversation state** được giữ trong message history. Trong flow minh họa, history được gửi lại ở mỗi lần gọi LLM.
- **`agent.invoke()`** điều phối tool schemas, API calls, parsing và execution.

![Pipeline LangChain truyền output từ prompt đến model rồi qua StrOutputParser.](images/02-langchain-chain.png)
