import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_groq import ChatGroq

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# model = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
# )

# response = model.invoke("What is the capital of India?")

# model = ChatGroq(
#     model="openai/gpt-oss-120b",
#     temperature=0
# )

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to Hindi. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
    
ai_msg = model.invoke(messages)

print(ai_msg.content)