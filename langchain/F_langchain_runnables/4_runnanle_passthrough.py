# Runnable Passthrough
# RunnablePassthrough is a Runnable that simply returns the input it receives. It can be used as a placeholder or for testing purposes.

import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="openai/gpt-oss-20b")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Write a tweet about {topic}.",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="Write a linkedin post about {topic}.",
    input_variables=["topic"],
)

joke_generator_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke_generator': RunnablePassthrough(),
    'explanation_generator': RunnablePassthrough(prompt2, model, parser),
})

final_chain = RunnableSequence(joke_generator_chain, parallel_chain)

response = final_chain.invoke({"topic": "AI Agents"})

print(response)