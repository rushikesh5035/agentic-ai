# StructuredOutputParser

# in this StructuredOutputParser, we only predefined field schemas, so that llm will always return the output in the expected format, and we can enforce the schema of the output.

# it works by defining a list of fields(ResponseSchema) that the model should return, ensuring the output follows a specific structure format.

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import ResponseSchema, StructuredOutputParser

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="openai/gpt-oss-120b")

# define the expected output schema
schema = [
    ResponseSchema(name="fact_1", description="The first fact about the topic"),
    ResponseSchema(name="fact_2", description="The second fact about the topic"),
    ResponseSchema(name="fact_3", description="The third fact about the topic"),
]

# create an instance of the StructuredOutputParser with the defined schema
parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give 3 fact about {topic} \n {format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# prompt = template.invoke({"topic":"Black Holes"})

# result = model.invoke(prompt)

# parsed_output = parser.parse(result.content)

# print("Parsed Output:", parsed_output)

# using chain
chain = template | model | parser

result = chain.invoke({"topic":"Black Holes"})

print("Parsed Output from Chain:", result)

# In StructuredOutputParser, we can define schema but we can't perform the data validation on the output.
# To perform data validation, we can use PydanticOutputParser, which allows us to define a Pydantic model for the expected output and validate the output against that model.