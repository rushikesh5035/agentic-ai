## Chains in Langchain

import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="llama-3.1-8b-instant")

prompt = PromptTemplate(
    template="Generate 5 interesting facts about {topic}.",
    input_variables=["topic"]
)

# output parser to parse the output of the model into a string
parser = StrOutputParser()

# forming a chain --> (|) called the pipe operator, which is used to chain together different components in Langchain. The output of one component is passed as input to the next component in the chain.

chain = prompt | model | parser

# invoke the chain with a specific topic
response = chain.invoke({"topic": "space exploration"})

print(response)

chain.get_graph().print_ascii()  # print the graph of the chain in ASCII format

"""
     +-------------+       
     | PromptInput |       
     +-------------+       
            *              
            *              
            *              
    +----------------+     
    | PromptTemplate |     
    +----------------+     
            *              
            *              
            *              
      +----------+         
      | ChatGroq |         
      +----------+         
            *              
            *              
            *              
   +-----------------+     
   | StrOutputParser |     
   +-----------------+     
            *              
            *              
            *              
+-----------------------+  
| StrOutputParserOutput |  
+-----------------------+ 
"""