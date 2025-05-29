from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

model = ChatOpenAI()

class Review(TypedDict):
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "Return sentiment of the review either negative, positive or neutral"]

strctured_model = model.with_structured_output(Review)

response = strctured_model.invoke("""The hardware is great but the software looks outdated.""")

print(response)