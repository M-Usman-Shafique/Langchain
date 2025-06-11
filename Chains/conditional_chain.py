from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

# 1. Take feedback from the user.
# 2. Do sentiment Analysis of feedback: positive/negative
# 3. If positive, say thanks as response.
# 4. If negative, say sorry as response.
model = ChatOpenAI()

parser = StrOutputParser()

class Feedback(BaseModel):
    # Structural output for consistent sentiment analysis
    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

# Use parser2 for structural output:
classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

# For conditional execution of chains:
branch_chain = RunnableBranch(
    # If sentiment is positive:
    (lambda x: x["sentiment"] == 'positive', prompt2 | model | parser),
    # If sentiment is negative:
    (lambda x: x["sentiment"]== 'negative', prompt3 | model | parser),
    # If sentiment is neither positive nor negative:
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({'feedback': 'This is a beautiful phone'}))

chain.get_graph().print_ascii()