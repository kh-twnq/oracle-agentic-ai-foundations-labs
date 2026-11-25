# Oracle Agentic AI Foundations

Tài liệu học và lab thực hành theo Oracle Agentic AI Foundations Workshop.

| Thư mục | Nội dung |
| --- | --- |
| [study-notes/](study-notes/README.md) | Bản tóm tắt tiếng Việt và sơ đồ cho toàn bộ 6 Module, kèm số trang trong Student Guide. |
| [labs/](labs/README.md) | Hướng dẫn chạy, local fixtures, Oracle AI Vector Search, Customer Return Agent và kết quả mẫu. |
| [Mã lab Oracle University](https://github.com/oracle-university-labs/ou-generativeai-pro/tree/085b7b13eeae897e3017ad110b703e2dcfd3a38c/agentic-ai-foundations) | Các ví dụ LangChain, MCP, OpenAI và OCI gốc. Git submodule lấy đúng commit dùng trong workshop. |

## Lấy mã lab

```sh
git clone --recurse-submodules https://github.com/kh-twnq/oracle-agentic-ai-foundations-labs.git
cd oracle-agentic-ai-foundations-labs
```

Với bản clone đã có, chạy `git pull` rồi `git submodule update --init` ở thư mục gốc. Source Oracle nằm tại `labs/oracle-university/agentic-ai-foundations/`.

Xem [hướng dẫn chạy và kết quả lab](labs/README.md) để cài dependencies bằng Python 3.11, chạy bộ fixture cục bộ và thử Vector Search hoặc Customer Return Agent.
