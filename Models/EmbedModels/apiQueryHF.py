## Run: python3 Models/EmbedModels/apiQueryHF.py
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

embedding = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    task="feature-extraction",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),

)

vector = embedding.embed_query("Paris is the capital of France")

print(str(vector))