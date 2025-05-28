## Run: python3 Models/EmbedModels/docsOpenAI.py
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

docs = [
    "Paris is the capital of France",
    "London is the capital of England",
    "New York is the capital of America"
]

vector = embedding.embed_documents(docs)

print(str(vector))