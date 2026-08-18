import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

chat_template = ChatPromptTemplate([
    (
        "system", "You are a helpful {domain} expert."
    ),
    (
        "user", "Explain in simple terms: what is {user_input}?"
    ),
])

model = ChatGroq(model="openai/gpt-oss-120b")


prompt = chat_template.invoke({"domain": "AI", "user_input": "LangChain"})

print("Prompt: ", prompt)