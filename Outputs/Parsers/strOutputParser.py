from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
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

parser = StrOutputParser()

# Parse the 1st response into string and pass it to the 2nd template and then parse the final response as well:
chain = template1 | model | parser | template2 | model | parser

response = chain.invoke({"topic": "black hole"})

print(response)