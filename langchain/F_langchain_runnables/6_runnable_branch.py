# RunnableBranch
# It is a control flow component in langchain that allows you to conditionally route input data to different chains or runnanles based on the custom logic/evaluation of a condition.
# it functions like an if/elif/else block for chains - where you define a set of condition functions, each associated with a runnble (e.g., LLM call, prompt chain, or tool). the first matching condition is executed. if no condition matches, a default runnable is used (if provided).

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

# Input topic -> generate prompt -> LLM -> parse output -> if report >= 500 words -> summarize -> if report < 500 words -> return report as is.

prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}.",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="Summarize the following report: {report}.",
    input_variables=["report"],
)

# 1st sequencial chain that generates a report on the given topic. [topic -> prompt1 -> model -> parser]
report_generator_chain = RunnableSequence(prompt1, model, parser)

# 2nd is branch chain that checks the word count of the generated report and routes it to either the summarization chain or returns the report as is.
branch = RunnableBranch(
    # check generated report word count 
    (lambda x: len(x.split()) > 300, 
     RunnableSequence(prompt2, model, parser)),  # if report >= 500 words -> summarize

    RunnablePassthrough()  # if report < 500 words -> return report as is
)

# final chain that combines the report generation and branching logic. [topic -> report_generator_chain -> branch]
final_chain = RunnableSequence(report_generator_chain, branch)

result = final_chain.invoke({"topic": "The impact of AI on modern society and its implications for the future of work, ethics, and human interaction."})

print(result)