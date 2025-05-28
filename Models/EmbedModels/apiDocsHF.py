## Run: python3 Models/EmbedModels/apiDocsHF.py
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

embedding = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    task="feature-extraction",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)

docs = [
    "Paris is the capital of France",
    "London is the capital of England",
    "New York is the capital of America"
]

result = embedding.embed_documents(docs)

print(str(result))