from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory

chat_history = ConversationBufferMemory(return_messages=True)

chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    # chat history injection before starting conversation:
    MessagesPlaceholder(variable_name='chat_history'),
    ('user','{input}') # Latest user message
])

prompt = chat_template.invoke({'chat_history':chat_history, 'input':'Where is my refund'})

print(prompt)