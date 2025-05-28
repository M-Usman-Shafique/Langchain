## Run: python3 Models/EmbedModels/queryOpenAI.py
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)
prompt = "What's the capital of France?"

vector = embedding.embed_query(prompt)
print(str(vector))