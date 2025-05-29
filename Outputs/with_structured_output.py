from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI()

class Review(TypedDict):
    summary: str
    sentiment: str

strctured_model = model.with_structured_output(Review)

response = strctured_model.invoke("""The hardware is great but the software looks outdated.""")

print(response)