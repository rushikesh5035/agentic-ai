## Parallel Chain
# In Parallel Chain, we can run multiple chains in parallel and combine their outputs. This is useful when you have multiple tasks that can be executed simultaneously, and you want to aggregate their results.


import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model1 = ChatGroq(model="llama-3.1-8b-instant")

model2 = ChatGroq(model="openai/gpt-oss-20b")

prompt1 = PromptTemplate(
    template="Generate short and simple notes from following text: {text}.",
    input_variables=["text"]
)

prompt2 = PromptTemplate(
    template="Generate 5 short questions and answers from the following text: {text}.",
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quize into a single document \n Notes: {notes} \n Quiz: {quiz}",
    input_variables=["notes", "quiz"]
)

parser = StrOutputParser()

# Create a parallel chain to run multiple chains concurrently
Parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
}) 

marge_chain = prompt3 | model1 | parser

chain = Parallel_chain | marge_chain

text = """
RAG architecture
A typical RAG pipeline is simple to describe but also easy to underbuild for production. Understanding the RAG architecture baseline and why basic setups struggle helps you move into advanced RAG techniques with the right context.
What the RAG pipeline does
A standard RAG system does four things:
Ingests content: splits documents into chunks, adds metadata, and creates embeddings.
Indexes: builds a store for efficient retrieval, often a vector index, sometimes with a keyword index as well.
Retrieves: fetches top-k context for a query.
Generates: prompts the model with the query plus the retrieved context and returns an answer.
At runtime, the system encodes the user’s query with the same model used to embed documents during ingestion, searches the index for the nearest vectors, retrieves the top-k chunks, and includes those chunks with the query in the prompt.
A typical failure mode
Naive pipelines often perform well in demos but break in production.

This might sound familiar: You ship a quick RAG helper for your team. It nails simple fact lookups. Then a PM asks, “Which enterprise customers renewed last quarter and also opened support tickets about SSO?” The bot replies with a partial list, misses a couple of key accounts, and adds an irrelevant customer.     
Here are some common symptoms you’ll recognize:
Top-k returns near duplicates or shallow snippets, so the prompt lacks diversity.
Retrieval misses proper nouns, IDs, or acronyms (SKU-123, SSO, SOC 2) because they occur rarely.
Answers cite the wrong entity or mix details across similar accounts.
Latency climbs when you raise k, use longer chunks, or rerun retrieval after follow-ups.
Poor table and PDF splitting drops headers or footnotes that change meaning.
Multi-turn chats drop constraints (“only EMEA,” “last quarter”), so follow-ups forget earlier filters, leading to off-scope answers.
Thin retrieval sets push the model to guess and fill in unsupported details.
"""

response = chain.invoke({"text": text})

print(response)

chain.get_graph().print_ascii()

"""
          +---------------------------+            
          | Parallel<notes,quiz>Input |            
          +---------------------------+            
                ***             ***                
              **                   **              
            **                       **            
+----------------+              +----------------+ 
| PromptTemplate |              | PromptTemplate | 
+----------------+              +----------------+ 
          *                             *          
          *                             *          
          *                             *          
    +----------+                  +----------+     
    | ChatGroq |                  | ChatGroq |     
    +----------+                  +----------+     
          *                             *          
          *                             *          
          *                             *          
+-----------------+            +-----------------+ 
| StrOutputParser |            | StrOutputParser | 
+-----------------+            +-----------------+ 
                ***             ***                
                   **         **                   
                     **     **                     
          +----------------------------+           
          | Parallel<notes,quiz>Output |           
          +----------------------------+           
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