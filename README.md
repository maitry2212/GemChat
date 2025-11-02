# 💎 GemChat — Streamlit Chatbot with Memory & Graph-based Flow

**GemChat** is a modern **Streamlit-based chatbot** that combines real-time conversation streaming, persistent memory, and modular graph logic.
It’s designed to give a **ChatGPT-like experience** with the flexibility to plug in any **LLM backend** or custom reasoning graph.

---

## 🚀 Features

✅ **Interactive Streamlit UI** — Chat naturally with a clean interface

✅ **Real-time streaming** — See responses as they’re generated

✅ **Memory persistence** — Save and load past chats from the sidebar

✅ **Graph-based logic** — Message flow controlled via `graph.py`

✅ **Lightweight & customizable** — Extend easily for LLMs like Gemini, OpenAI, or local models

---

## 🧠 Architecture Overview

```
User → Streamlit Chat UI → Graph (LLM / logic engine)
                   ↘
                 Memory Manager (save / load)
```

**Core Components:**

* **`app.py`** → Streamlit chat frontend
* **`graph.py`** → Handles response generation and flow (LLM logic)
* **`memory_manager.py`** → Saves and retrieves chat histories

---

## 📁 Project Structure

```
📦 GemChat
├── app.py                 # Main Streamlit application
├── graph.py               # Chat flow / logic definition
├── memory_manager.py      # Conversation persistence
├── conversations/         # Auto-created folder for saved chats
├── requirements.txt       # Project dependencies
└── README.md              # Documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/maitry2212/GemChat.git
cd GemChat
```

### 2️⃣ Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Once the app is running, open the link shown in your terminal (usually `http://localhost:8501`) and start chatting! 💬

---

## 🧩 How GemChat Works

1. **Graph Engine:**
   The chat flow is powered by a graph system (defined in `graph.py`), where each node represents a processing stage (e.g., model response, memory handling, etc.).

2. **Memory Manager:**
   `memory_manager.py` provides an interface for saving, listing, and loading past conversations from local storage.

3. **Streaming Responses:**
   The assistant’s reply is streamed token-by-token for a natural typing effect.

---

## 💾 Conversation Persistence

You can:

* Load past chats from the sidebar
* Create a new chat anytime
* Click **💾 Save Conversation** to store the current session

All saved chats are kept under the `conversations/` folder.

---

## ⚙️ Example `requirements.txt`

```
streamlit
```

---

## 🧑‍💻 Author

**Maitry Chauhan**

💡 Engineering Student | Exploring AI, LangChain & Chat Systems

🔗 [GitHub](https://github.com/<your-username>)

---

## 🪪 License

This project is licensed under the **MIT License** — free for personal and academic use.

---
