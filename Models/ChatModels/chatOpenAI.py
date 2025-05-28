## Run: python3 Models/ChatModels/chatOpenAI.py
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=0.7, max_completion_tokens=10)
result = model.invoke("What's the capital of France?")

print(result.content)