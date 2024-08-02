import streamlit as st
from groq import Groq
st.set_page_config("Text Summarizer","💬💬",initial_sidebar_state="collapsed")

st.header("Text Summarizer📜")
st.divider()
with st.container():
    text = st.text_area("Enter the text below to summarize : ")
    # radio = st.radio("Select the model for summarizing : ", ["Llama 3", "Gemini"])
    cols = st.columns(5)
    if cols[-1].button("Summarize"):
        model = Groq(api_key= st.secrets["api_key"]).chat.completions.create(
            model = "llama3-8b-8192",
            messages=[
                {"role": "system", "content" : "You are text analysibg agent, your role is to summarize the text with a small description"},
                {"role": "user", "content": text}
                ]
        )
        st.write(model.choices[0].message.content)
    