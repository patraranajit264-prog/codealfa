import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

st.set_page_config(page_title="Language Translator", page_icon="🌐")

st.title("🌐 Language Translation Tool with Voice 🔊")
text = st.text_area("Enter text to translate:")
languages = {
    "Hindi": "hi",
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Bengali": "bn"
}
source_lang = st.selectbox("Select Source Language", list(languages.keys()))
target_lang = st.selectbox("Select Target Language", list(languages.keys()))

source_code = languages[source_lang]
target_code = languages[target_lang]
if st.button("Translate"):
    if text.strip() == "":
        
        st.warning("⚠️ Please enter text")
    else:
        try:
            translated = GoogleTranslator(
                source=source_code,
                target=target_code
            ).translate(text)

            st.success("✅ Translated Text:")
            st.write(translated)
            tts = gTTS(text=translated, lang=target_code)
            tts.save("output.mp3")

            st.audio("output.mp3")

        except Exception as e:
            st.error("❌ Error occurred")