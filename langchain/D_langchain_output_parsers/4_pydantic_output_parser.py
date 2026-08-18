# PydanticOutputParser
# It is a structured output parser in langchain that uses Pydantic models to define the expected output schema and validate the output against that schema.

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="openai/gpt-oss-120b")


# define a Pydantic model for the expected output schema
class Person(BaseModel):
    name: str = Field(description="The name of the person")
    age: int = Field(gt=18, description="The age of the person")
    city: str = Field(description="The city of the person")


# create an instance of the PydanticOutputParser with the defined Pydantic model
parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate the name, age and city of a fictional {place} person \n{format_instructions}",
    input_variables=["place"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# prompt = template.invoke({"place": "Indian"})

# print(prompt)

# result = model.invoke(prompt)

# parsed_result = parser.parse(result.content)

# print(parsed_result)


# using chains
chain  = template | model | parser

result = chain.invoke({"place": "Indian"})

print(result)