from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="openai/gpt-oss-120b")

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me a joke."),
]

model_response = model.invoke(messages)

messages.append(AIMessage(content=model_response.content))

print("AI: ", model_response.content)