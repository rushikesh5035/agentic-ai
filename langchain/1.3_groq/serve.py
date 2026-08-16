import os
from dotenv import load_dotenv

from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="openai/gpt-oss-120b", groq_api_key=groq_api_key)

system_template = "Translate the following into {language}: "

prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "{text}"),
])

parser = StrOutputParser()

# creae chain
chain = prompt_template | model | parser

# App Defination
app = FastAPI(title="Langchain server Demo With Groq Model", version="1.0.0", description="Langchain server Demo With Groq Model")

# adding chain routes to the app
add_routes(
    app, 
    chain, 
    path="/translate"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)