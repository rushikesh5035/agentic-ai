## Output Parsers - in langchain, it help convert the raw LLM output response into structured formats, such as JSON, CSV, Pydantic models, etc.

"""1. String Output Parser - strOutputParser"""

# StrOutputParser is a simple output parser that returns the raw string output from the LLM without any additional processing or formatting.


import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="openai/gpt-oss-120b")

template1 = PromptTemplate(
    template="Write a detailed report on the following topic: {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Write a 5 line summary of the following: {text}",
    input_variables=["text"]
)

# prompt1 = template1.invoke({"topic": "The impact of AI on modern education"})

# response = model.invoke(prompt1)

# prompt2 = template2.invoke({"text": response.content})

# response2 = model.invoke(prompt2)

# print("Raw LLM Output (Detailed Report): ", response.content)
# print("Raw LLM Output (Summary): ", response2.content)

''' 
Now in above code, we have not used any output parser, so the raw output from the LLM is returned as a string. However, if we want to parse the output into a structured format, we can use the StrOutputParser.
'''

# parsing the raw output using StrOutputParser
parser = StrOutputParser()

# chain of prompts and models with output parsing
chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({"topic": "Black Hole"})

print("Final Output (Summary): ", result)