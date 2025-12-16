import streamlit as st
import os
from openai import OpenAI

# -------------------------
# OpenAI Client
# -------------------------
client = OpenAI(api_key=os.getenv("ZUsTn3z3nAKpkwat8NeX_zREmdk8HxafWWwStlp7altc34FavV7-YWbcwowzRZWfc3JSL22AaRT3BlbkFJ3_zRS9Xn2ATtc603HQhaj6YUQmAOGHIEkhYeVoQ52DcmqW9yVSH1pA0mciRBtO-hgkpFSHL5QA"))

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="Brain Power Study",
    page_icon="🧠",
    layout="centered"
)

# -------------------------
# UI
# -------------------------
st.title("🧠 Brain Power Study")
st.subheader("AI Smart Learning App")

st.markdown("📚 **AI से आसान, तेज़ और मज़ेदार पढ़ाई**")

topic = st.text_input("✍️ Topic लिखो (जैसे: Newton Law, संविधान, AI क्या है?)")

mode = st.radio(
    "आप कैसे सीखना चाहते हैं?",
    ("📖 Reading", "🎧 Listening", "🎬 Watching")
)

level = st.selectbox(
    "📊 Level चुनो",
    ("Beginner", "Medium", "Advanced")
)

# -------------------------
# Button Action
# -------------------------
if st.button("🚀 Start Learning"):
    if not topic:
        st.warning("❗ पहले topic लिखो")
    else:
        with st.spinner("🤖 AI सोच रहा है..."):
            prompt = f"""
Topic: {topic}
Mode: {mode}
Level: {level}

Explain in very simple Hindi + English mix.
Use examples and short points.
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

        st.success("✅ Learning Ready!")
        st.markdown("### 📖 Explanation")
        st.write(response.choices[0].message.content)

# -------------------------
# Footer
# -------------------------
st.markdown("---")
st.markdown("💡 Made with ❤️ by **Brain Power Study**")
