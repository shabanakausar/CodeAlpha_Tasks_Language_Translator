# translator_app.py

import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# --- Load environment variables ---
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
api_key = os.getenv("GROQ_API_KEY")

# --- Check API Key ---
if not api_key:
    st.error("🚨 Groq API key not found. Please set GROQ_API_KEY in .env file or environment.")
    st.stop()

# --- Initialize Groq Chat Client ---
client = ChatGroq(api_key=api_key, model="llama3-8b-8192")

# --- Streamlit UI ---
st.title("🌐 Translator with Language Detection")
st.write("Enter text and select a target language to translate.")

text_input = st.text_area("Text to translate", placeholder="Type or paste your text here...", height=100)
target_lang = st.selectbox("Target language", 
                           ["English", "Spanish", "French", "German", "Chinese", "Hindi", "Arabic", "Russian", "Portuguese", "Japanese", "Korean", "Other"])

if st.button("Translate"):
    if not text_input.strip():
        st.warning("Please enter some text to translate.")
    else:
        with st.spinner("Detecting language..."):
            try:
                detect_msg = [
                    {"role": "system", "content": "You are an expert language detector."},
                    {"role": "user", "content": f"What language is this? Just respond with the name of the language:\n\n{text_input.strip()}"}
                ]
                detect_response = client.invoke(detect_msg)
                detected_lang = detect_response.content.strip()
                st.info(f"🕵️ Detected Language: **{detected_lang}**")
            except Exception as e:
                st.error(f"❌ Language detection failed: {e}")
                st.stop()

        with st.spinner("Translating..."):
            try:
                system_msg = {"role": "system", "content": "You are a helpful assistant that accurately translates text from any language to the target language."}
                user_msg = {"role": "user", "content": f"Translate the following text to {target_lang}:\n\n{text_input.strip()}"}
                response = client.invoke([system_msg, user_msg])
                translated = response.content
                st.success("✅ Translation Complete")
                st.text_area("Translation", value=translated, height=150)
            except Exception as e:
                st.error(f"❌ Translation failed: {e}")
