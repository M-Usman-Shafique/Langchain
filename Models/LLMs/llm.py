## Run python3 Models/LLMs/llm.py
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model = 'gpt-3.5-turbo-instruct')
prompt = "What's the capital of France?"

response = llm.invoke(prompt)
print(response)