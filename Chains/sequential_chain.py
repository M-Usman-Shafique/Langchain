from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

model = ChatOpenAI()

parser = StrOutputParser()

# Pass the response of prompt1 as input to prompt2:
chain = prompt1 | model | parser | prompt2 | model | parser

response = chain.invoke({'topic': 'Unemployment in Pakistan'})

print(response)

chain.get_graph().print_ascii()