# 🤖 AI ChatBot

An intelligent AI-powered chatbot built with **Streamlit**, **LangChain**, and **Groq LLM**. This chatbot provides a clean conversational interface with real-time responses using the powerful **OpenAI GPT-OSS-120B** model hosted by Groq.

---

## 🚀 Features

- 💬 Real-time AI conversation
- ⚡ Fast inference using Groq API
- 🧠 Powered by OpenAI GPT-OSS-120B
- 📝 Conversation history using Streamlit Session State
- 🎨 Clean and responsive chat interface
- 👤 User messages aligned to the right
- 🤖 AI responses displayed with Streamlit's chat interface
- 🔒 Secure API key management using `.env`

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- LangChain-Groq
- Groq API
- python-dotenv

---

## 📂 Project Structure

```text
AI-ChatBot/
│
├── chatbot.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env (not included)
```

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/TamimBhaii/AI-Chatbot.git
```

Go to the project directory

```bash
cd AI-Chatbot
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Git Bash

```bash
source venv/Scripts/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run chatbot.py
```

The application will open in your browser.

---

## 💡 Model Used

- OpenAI GPT-OSS-120B (via Groq API)

---

## ⚠️ Disclaimer

This chatbot may generate incorrect or outdated information.

Current knowledge cutoff of the model is **June 2024**.

Please verify important information from trusted sources.

---

## 📸 Demo

_Add screenshots or a live demo link here after deployment._

---

## 👨‍💻 Author

**Tamim Islam**

- GitHub: https://github.com/TamimBhaii
- LinkedIn: *(Add your LinkedIn profile here)*

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub.
