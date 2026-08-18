# Sequential Chain is a chain that runs multiple chains in sequence, passing the output of one chain as the input to the next. It is useful for breaking down complex tasks into smaller, manageable steps.

import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="llama-3.1-8b-instant")

prompt1 = PromptTemplate(
    template="Generate a report on {topic}.",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a 5 short summary of the following text: {text}.",
    input_variables=["text"]
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

response = chain.invoke({"topic": "Unemployment in India"})

print(response)

chain.get_graph().print_ascii()

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