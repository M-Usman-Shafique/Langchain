## Run: python3 Models/EmbedModels/localDocsHF.py
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": False}
)

docs = [
    "Paris is the capital of France",
    "London is the capital of England",
    "New York is the capital of America"
]

vector = embedding.embed_documents(docs)

print(str(vector))