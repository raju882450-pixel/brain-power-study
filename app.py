import streamlit as st
from openai import OpenAI
from gtts import gTTS
import tempfile

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="🧠 Brain Power Study", layout="centered")

# ---------------- OPENAI CLIENT ----------------
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ---------------- UI ----------------
st.title("🧠 Brain Power Study")
st.subheader("AI Smart Learning App")

topic = st.text_input("📘 Topic लिखो (Hindi / English)")

mode = st.radio(
    "आप कैसे सीखना चाहते हैं?",
    ("📖 Reading", "🎧 Listening")
)

# ---------------- TEXT TO SPEECH ----------------
def speak(text):
    tts = gTTS(text=text, lang="hi")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        tts.save(f.name)
        st.audio(f.name, format="audio/mp3")

# ---------------- ACTION ----------------
if st.button("🚀 Start Learning") and topic:
    with st.spinner("AI सोच रहा है..."):
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a helpful teacher. Explain simply in Hindi."},
                {"role": "user", "content": f"{topic} आसान भाषा में समझाओ"}
            ]
        )

        answer = response.choices[0].message.content
        st.success("✅ Explanation Ready")
        st.write(answer)

        if mode == "🎧 Listening":
            speak(answer)
