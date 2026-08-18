# Traditional LLMs take a raw string prompt and return a raw string response.


import os
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

llm = GoogleGenerativeAI(model="gemini-2.5-flash-lite")

response = llm.invoke("What are some of the pros and cons of Python as a programming language?")

print(response)