## Run python3 Prompts/app.py
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_history = []

while True:
    user_input = input('You: ')
    chat_history.append(user_input)

    if user_input == 'exit':
        break

    response = model.invoke(chat_history)
    chat_history.append(response.content)
    print("AI: ", response.content)

print(chat_history)