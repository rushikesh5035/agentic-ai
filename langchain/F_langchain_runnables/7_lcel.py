# LCEL -> LangChain Expression Language

"""As you can see, from all the 5 runnable primitives, the most used one is RunnableSequence, But everytime we need to create a RunnableSequence instance like -> RunnableSequence(prompt, model, parser........

To make it simple to use, now we can use the new way to create a RunnableSequence instance using the new LCEL syntax, i.e. using '|' pipe operator

[prompt | model | parser..........]

this is called the LangChain Expression Language (LCEL) syntax. 
"""

import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="openai/gpt-oss-20b")

parser = StrOutputParser()


prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}.",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="Summarize the following report: {report}.",
    input_variables=["report"],
)


# Create the report generator chain using LCEL syntax
report_generator_chain = prompt1 | model | parser

branch = RunnableBranch(
    (lambda x: len(x.split()) > 300, 
     prompt2 | model | parser),
    RunnablePassthrough() 
)

final_chain = report_generator_chain | branch

result = final_chain.invoke({"topic": "The impact of AI on modern society and its implications for the future of work, ethics, and human interaction."})

print(result)