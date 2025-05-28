## Run: streamlit run Prompts/static.py
from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=0.7, max_completion_tokens=10)

st.title("Summarize Tool")
user_input = st.text_input("What can I help with?")
if st.button("Summarize"):
    response = model.invoke(user_input)
    st.write(response.content)