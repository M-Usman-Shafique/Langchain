## Run: python3 Models/ChatModels/chatGoogle.py
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model= "gemini-1.5-pro")
result = model.invoke("What's the capital of France?")

print(result.content)