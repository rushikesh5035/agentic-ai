# JSON Output parser - JSONOutputParser

# JSONOutputParser is an output parser that converts the raw string output from the LLM into a structured JSON format. It uses the built-in json module to parse the string and return a Python dictionary.


import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="openai/gpt-oss-120b")

# create an instance of the JsonOutputParser
parser = JsonOutputParser()

template = PromptTemplate(
    template="GIve me the name, age and city of fictional person: \n {format_instructions}",
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()} # this will provide the model with the necessary instructions to format the output as JSON
)

#prompt = template.format()

#response = model.invoke(prompt)

# print("Response:", response)

# it will parse the response content and return a Python dictionary
# parsed_output = parser.parse(response.content)

# print("Parsed Output:", parsed_output)

# Parsed Output: {'name': 'Lena Alvarez', 'age': 34, 'city': 'Portland'}


# Using chain
chain = template | model | parser

result = chain.invoke({})

print("Result:", result)

# Result: {'name': 'Lena Marlowe', 'age': 34, 'city': 'Cedarbrook'}

# But JsonOutputParser was some problem, we can't enforce the schema of the output, means you can't guarantee that the model will always return the output in the expected format. If the model returns an output that doesn't match the expected format, the parser will raise a ValueError.

# So we use the StructuredOutputParser.