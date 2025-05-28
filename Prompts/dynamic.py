## Run: streamlit run Prompts/dynamic.py
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.prompts import load_prompt
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

st.title("Summarize Tool")

paper_input = st.selectbox( "Select Research Paper", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('template.json')

if st.button('Summarize'):
    chain = template | model
    response = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    st.write(response.content)