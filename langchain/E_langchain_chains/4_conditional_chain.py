## Conditional Chain
## In Conditional Chain, we can run different chains based on the output of a previous chain.


# Customer Feedback Analysis Example
# Customers feedback ---> Analyze feedback (Positive/Negative) ---> Positive Feedback: Generate Thank You Note ---> Negative Feedback: send email to support team and communicate with customer

import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="openai/gpt-oss-20b")

# model2 = ChatGroq(model="openai/gpt-oss-20b")

parser = StrOutputParser()

class FeedbackSentiment(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="The sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=FeedbackSentiment)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following customer feedback as positive or negative: \n {feedback} \n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

classifier_chain.invoke({"feedback": "The product is great, but the delivery was late."}).sentiment

# print(response)

prompt2 = PromptTemplate(
    template="Write an appropriat respons to this positive feedback: \n {feedback}",
    input_variables=["feedback"]
)
prompt3 = PromptTemplate(
    template="Write an appropriat respons to this negative feedback: \n {feedback}",
    input_variables=["feedback"]
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2 | model | parser),

    (lambda x: x.sentiment == "negative", prompt3 | model | parser),

    RunnableLambda(lambda x: "could not find sentiment") # this is not a chain so we converted it to a RunnableLambda
)


chain = classifier_chain | branch_chain

# response = chain.invoke({"feedback": "The product is great, but the delivery was late."})
response = chain.invoke({"feedback": "This mobile phone was amazing! I loved the camera quality and the battery life is exceptional. Highly recommend it!"})

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
+----------------------+ 
| PydanticOutputParser | 
+----------------------+ 
            *            
            *            
            *            
       +--------+        
       | Branch |        
       +--------+        
            *            
            *            
            *            
    +--------------+     
    | BranchOutput |     
    +--------------+ 
"""