# 🤖 FAQ Support Chatbot

> An AI-powered **customer support assistant** built with **Streamlit** and **Groq API**, designed to provide accurate, deterministic answers from a structured FAQ database.
> Think of it as a mini helpdesk — fast, reliable, and hallucination-free.

---

## 🧩 Features

✅ **Real-time Chat Interface** — Streamlit-based, clean and responsive
✅ **Deterministic Responses** — Uses `temperature=0` for consistent output
✅ **Predefined FAQ Knowledge Base** — No hallucination or fake info
✅ **Chat Memory** — Retains conversational context within session
✅ **Custom UI** — Smooth pastel background, modern sidebar, and hover effects
✅ **Session Controls** — Clear chat anytime and start fresh

---

## 🗂️ Project Structure

```
📁 project/
├── .env                   # API key storage
├── WebChat.py             # Main Streamlit web app
├── chatbot.py             # Core chatbot logic (optional modular version)
├── faq_chatbot.py         # FAQ data and prompt management
├── stats.py               # Session analytics (optional)
├── test_determinism.py    # Unit tests for deterministic response behavior
```

---

### Add Your API Key

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_api_key_here
```

### Run the Application

```bash
streamlit run WebChat.py
```

---

## 🧠 How It Works

1. **User Input:** You type a question into the Streamlit chat box.
2. **Prompt Context:** The full conversation (system + user + assistant) is sent to the Groq API.
3. **Groq Model:** LLaMA 3.1 (8B Instant) processes it with a strict system prompt tied to the FAQ data.
4. **Response:** The model replies deterministically using only valid FAQ info.
5. **Memory:** Chat history persists during the session for contextual answers.

---

## 👩‍💻 Author

**Manya Kapoor**
🎓 Engineering Student | NITJ
📧 [lm.manyakapoor@gmail.com](mailto:lm.manyakapoor@gmail.com)
🌐 [LinkedIn](https://www.linkedin.com/in/manyaakapoor) • [GitHub](https://github.com/Manyaakapoor)

---

## 🪪 License

© 2025 Manya Kapoor
