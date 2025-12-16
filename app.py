# ================================
# BRAIN POWER STUDY – ALL IN ONE
# Python + Streamlit + OpenAI
# ================================

import streamlit as st
import openai
import pyttsx3
import base64
from pathlib import Path

# ========== OPENAI CONFIG ==========
openai.api_key = "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"   # <-- apni API key yahan daalo

# ========== TEXT TO SPEECH ==========
tts = pyttsx3.init()
def speak(text):
    tts.say(text)
    tts.runAndWait()

# ========== LOGO LOAD (OPTIONAL) ==========
def show_logo():
    logo_path = "logo.png"
    if Path(logo_path).exists():
        st.image(logo_path, width=220)

# ========== AI FUNCTIONS ==========
def generate_question(material):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Create one short thinking question from the given study material."
            },
            {
                "role": "user",
                "content": material
            }
        ]
    )
    return response.choices[0].message.content


def generate_explanation(question, mode):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": f"Explain the answer very briefly (max 2 lines) using {mode}. Keep it simple."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )
    return response.choices[0].message.content


# ========== UI SETUP ==========
st.set_page_config(
    page_title="BRAIN POWER STUDY",
    layout="centered"
)

show_logo()

st.title("🧠 BRAIN POWER STUDY")
st.caption("Turn your brain into power ⚡")

st.markdown("---")

material = st.text_area(
    "📘 Apna study material paste karein (kisi bhi language me)",
    height=220
)

if st.button("🚀 Start Smart Study") and material.strip():
    st.session_state.material = material
    st.session_state.question = generate_question(material)
    st.session_state.explanation = ""

# ========== STUDY MODE ==========
if "question" in st.session_state:

    st.subheader("❓ Question")
    st.write(st.session_state.question)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📖 Read"):
            st.session_state.explanation = generate_explanation(
                st.session_state.question, "reading"
            )

    with col2:
        if st.button("🎧 Listen"):
            st.session_state.explanation = generate_explanation(
                st.session_state.question, "listening"
            )
            speak(st.session_state.explanation)

    with col3:
        if st.button("👀 Watch"):
            st.session_state.explanation = generate_explanation(
                st.session_state.question, "visual imagination"
            )

    if st.session_state.explanation:
        st.markdown("### 🧠 Explanation")
        st.write(st.session_state.explanation)

    if st.button("➡ Next Concept"):
        st.session_state.question = generate_question(
            st.session_state.material
        )
        st.session_state.explanation = ""
