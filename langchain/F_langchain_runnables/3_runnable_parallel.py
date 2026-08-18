## RunnableParallel is a Runnable that runs multiple Runnables in parallel and returns their results as a list.

import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="openai/gpt-oss-20b")

prompt1 = PromptTemplate(
    template="Write a tweet about {topic}.",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="Write a linkedin post about {topic}.",
    input_variables=["topic"],
)

parser = StrOutputParser()

# this is the RunnableParallel that will run the prompts and model in parallel, returning their results as a dictionary.
parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser),
})

result = parallel_chain.invoke({"topic": "AI Agents"})

print(result)