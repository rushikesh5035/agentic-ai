import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="openai/gpt-oss-20b")

prompt1 = PromptTemplate(
    template="Write a joke about {topic}.",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="Explain the following joke {joke}.",
    input_variables=["joke"],
)

parser = StrOutputParser()

# this is the RunnableSequence that will run the prompts and model in order, passing the output of one step as the input to the next step.
chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

print(chain.invoke({"topic": "chickens"}))