# 🤖 FAQ Support Chatbot

> An AI-powered **customer support assistant** built with **Streamlit** and **Groq API**, designed to answer questions from a structured FAQ database — fast, accurate, and hallucination-free.
> Try it live here → [**webchatpy.streamlit.app**](https://webchatpy.streamlit.app/)

---

## 🧩 Features

* 💬 **Interactive Chat Interface** — built on Streamlit with clean, responsive UI
* 🧠 **Deterministic Answers** — powered by `llama-3.1-8b-instant` with `temperature=0`
* 📚 **Structured FAQ Knowledge Base** — ensures factual, scoped answers only
* 🗣️ **Chat Memory** — remembers your questions during a session
* 🎨 **Custom Styling** — modern layout with soft pastel backgrounds and rounded elements
* ♻️ **Session Controls** — clear chat anytime and start fresh easily

---

## 🚀 Live Demo

🔗 **Access the chatbot:** [https://webchatpy.streamlit.app/](https://webchatpy.streamlit.app/)

Use the web version to explore all core functionalities — no local setup needed.

---

## 🗂️ Project Structure

```
📁 project/
├── .env                   # API key storage (local only)
├── WebChat.py             # Main Streamlit web app
├── requirements.txt       # Added the required packages
├── chatbot.py             # Core chatbot logic (optional modular version)
├── faq_chatbot.py         # FAQ data and system prompt management
├── stats.py               # Session analytics (optional)
├── test_determinism.py    # Test deterministic response behavior
```

---

## ⚙️ Setup Instructions (for local use)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/faq-support-chatbot.git
cd faq-support-chatbot
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Your API Key

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

*(If hosting on Streamlit Cloud, use “Secrets” instead of `.env`.)*

### 5️⃣ Run the App

```bash
streamlit run WebChat.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🧠 How It Works

1. The app loads a **system prompt** containing all FAQ data.
2. User questions are added to a **conversation history**.
3. This history is passed to **Groq’s LLaMA 3.1 model**, which returns factual answers only from the FAQ database.
4. The Streamlit UI displays the response and retains chat memory for context.

---

## 👩‍💻 Author

**Manya Kapoor**
🎓 Engineering Student | NITJ
📧 [lm.manyakapoor@gmail.com](mailto:lm.manyakapoor@gmail.com)
🌐 [LinkedIn](https://www.linkedin.com/in/manyaakapoor) • [GitHub](https://github.com/Manyaakapoor)

---

## 🪪 License

© 2025 Manya Kapoor
