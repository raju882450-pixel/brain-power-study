import streamlit as st
from openai import OpenAI

# ---------- PAGE ----------
st.set_page_config(
    page_title="AI Smart Learning App",
    page_icon="🧠",
    layout="centered"
)

st.title("AI Smart Learning App")

# ---------- OPENAI ----------
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# ---------- UI ----------
topic = st.text_input("📘 Topic लिखो (Hindi / English)")

mode = st.radio(
    "आप कैसे सीखना चाहते हैं?",
    ["📖 Reading", "🎧 Listening"]
)

if st.button("🚀 Start Learning"):
    if topic.strip() == "":
        st.warning("Topic लिखना जरूरी है")
    else:
        with st.spinner("AI पढ़ा रहा है..."):
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a smart teacher. Explain simply with examples."
                    },
                    {
                        "role": "user",
                        "content": f"Explain {topic} in simple Hindi + English mix"
                    }
                ]
            )

            answer = response.choices[0].message.content
            st.success("📘 Explanation")
            st.write(answer)
