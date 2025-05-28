## Run: streamlit run Prompts/dynamic.py
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.prompts import load_prompt
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=0.7, max_completion_tokens=10)

st.title("Summarize Tool")

paper_input = st.selectbox( "Select Research Paper", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('template.json')

prompt = template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})

if st.button('Summarize'):
    response = model.invoke(prompt)
    st.write(response.content)