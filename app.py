import streamlit as st
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("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
"))

st.set_page_config(page_title="Brain Power Study", page_icon="🧠")
st.title("🧠 Brain Power Study")
st.subheader("AI Smart Learning App")

topic = st.text_input("📘 Topic लिखो (किस topic पर पढ़ना है?)")

mode = st.radio(
    "आप कैसे सीखना चाहते हैं?",
    ("📖 Reading", "🎧 Listening", "🎥 Watching")
)

if st.button("Start Learning") and topic:
    with st.spinner("AI सोच रहा है..."):
        prompt = f"""
        Explain the topic '{topic}' for a student.
        Learning mode: {mode}
        Use simple Hindi + English mix.
        Short, easy, interesting explanation.
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        st.success("AI Explanation:")
        st.write(response.choices[0].message.content)
