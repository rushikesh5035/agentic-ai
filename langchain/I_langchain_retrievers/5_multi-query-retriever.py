## Multi-Query Retriever
## Sometimes a single query might not capture all the ways information is phrased in your documents. 

"""
For Example,

Query : "How can i stay healthy?"

Could means:
 - What should I eat?
 - How often should I exercise?
 - How can i manage stress?

A simple similarity search might miss documents that talk about those things but don't use the word "healthy" in them.

so in Multi-Query Retriever, you can provide user's query to LLM and then LLM will generate multiple queries that capture different ways the information could be phrased.

Example:
    - What are the best foods to eat to stay healthy?
    - How often should I exercise to stay healthy?
    - What lifestyle changes can I make to manage stress and stay healthy?
    - How can i boost my immune system to stay healthy?
    - What daily routines support long-term health and wellness?

and then the retriever will run all those queries and return the most relevant documents from all of them.
"""


import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_groq import ChatGroq

load_dotenv()

os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

all_docs = [
    Document(page_content="Regular walking boosts heart health and can reduce symptoms of depression.", metadata={"source": "H1"}),
    Document(page_content="Consuming leafy greens and fruits helps detox the body and improve longevity.", metadata={"source": "H2"}),
    Document(page_content="Deep sleep is crucial for cellular repair and emotional regulation.", metadata={"source": "H3"}),
    Document(page_content="Mindfulness and controlled breathing lower cortisol and improve mental clarity.", metadata={"source": "H4"}),
    Document(page_content="Drinking sufficient water throughout the day helps maintain metabolism and energy.", metadata={"source": "H5"}),
    Document(page_content="The solar energy system in modern homes helps balance electricity demand.", metadata={"source": "I1"}),
    Document(page_content="Python balances readability with power, making it a popular system design language.", metadata={"source": "I2"}),
    Document(page_content="Photosynthesis enables plants to produce energy by converting sunlight.", metadata={"source": "I3"}),
    Document(page_content="The 2022 FIFA World Cup was held in Qatar and drew global energy and excitement.", metadata={"source": "I4"}),
    Document(page_content="Black holes bend spacetime and store immense gravitational energy.", metadata={"source": "I5"}),
]

embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_documents(
    documents=all_docs,
    embedding=embedding_model
)

# Normal retriever that uses similarity search
similarity_retriever = vectorstore.as_retriever(
    search_type="similarity", 
    search_kwargs={"k": 5}
)

# Multi-Query Retriever that uses LLM to generate multiple queries and then retrieves documents based on those queries
multi_query_retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
    llm=ChatGroq(model="openai/gpt-oss-20b")
)


# Query
query = "How to improve energy level and maintain balance?"

# Retrieve results
similarity_results = similarity_retriever.invoke(query)
multi_query_retriever_results = multi_query_retriever.invoke(query)

# Retrieved Results
for i, doc in enumerate(similarity_results):
    print(f"Similarity Search Result {i+1}: {doc.page_content} (Source: {doc.metadata['source']})")


for i, doc in enumerate(multi_query_retriever_results):
    print(f"Multi-Query Retriever Result {i+1}: {doc.page_content} (Source: {doc.metadata['source']})")
