from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate 
from dotenv import load_dotenv
import os

load_dotenv()

llmHF = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)

model = ChatHuggingFace(llm=llmHF)

template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Write a five line summary on the following text: \n{text}",
    input_variables=["text"]
)

prompt1 = template1.invoke({"topic": "blackhole"})
response1 = model.invoke(prompt1)

prompt2 = template2.invoke({"text": response1.content})
response2 = model.invoke(prompt2)

print(response2.content)