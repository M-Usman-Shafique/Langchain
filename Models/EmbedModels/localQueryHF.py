## Run: python3 Models/EmbedModels/localQueryHF.py
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": False}
)

prompt = "What's the capital of France?"
vector = embedding.embed_query(prompt)
print(str(vector))