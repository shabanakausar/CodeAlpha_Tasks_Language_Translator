# CodeAlpha_Tasks_Language_Translator
A simple language translation tool that translates text from one language to another. Use  machine translation techniques and pre-trained  models like Google Translate API or Microsoft  Translator API to translate text.

# 🌐 Language Translator using Streamlit + Groq LLaMA3

This is a simple web-based language translator built with [Streamlit](https://streamlit.io/) and [Groq's LLaMA3](https://console.groq.com/). It auto-detects the input language and translates it into a selected target language using natural language processing.

---

## 🚀 Features

- 🌍 Auto-detect source language
- 🔤 Translate into multiple languages (e.g., Spanish, French, Chinese, etc.)
- 💬 Supports multi-line text
- 🧠 Powered by Groq's LLaMA3 (via LangChain)

---

## 🛠 Installation

1. **Clone the repo**

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set your API key**

Create a `.env` file and add your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

Get your key from [Groq Console](https://console.groq.com/keys)

4. **Run the app**

```bash
streamlit run translator_app.py
```

---

## 📸 Screenshot

![screenshot](screenshot.png)

---

## 🧠 Note

This app uses LLaMA3 for translation via prompts. It is not as accurate as dedicated translation APIs like Google Translate, but works well for general text.

---

## 📄 License

MIT License

