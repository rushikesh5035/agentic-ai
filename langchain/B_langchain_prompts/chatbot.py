import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="openai/gpt-oss-120b")

# history
chat_history = [
    SystemMessage(content="You are a helpful assistant."),
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))

    if user_input.lower() == "exit":
        break

    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print("AI: ", response.content)

print(chat_history)