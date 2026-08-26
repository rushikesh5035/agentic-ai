### MMR - Maximal Marginal Relevance
## "How can we pick results that are not only relevant to the querybut also different from each other"

## MMR is an information retrieval algorithm designed to reduce redundancy in the retrived results while maintaining high relevance to the query. 

"""
Why MMR Retriever?
In regular simalirity search, you may get documents that are
    - All very similar to each others
    - Repeating the same information
    - Lacking diversity in the results

MMR Retriever avoids that by:
    - Picking the most relevant document first
    - then picking the next most relevant and least similar to already selected docs
    - and so on...

This helps especially in RAG pipelines where:
    - You want your context window to contains diverse but still relevant information
    - Especially useful when documents are semantically overlapping
"""


import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

load_dotenv()

os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")


docs = [
    Document(page_content="Langchain make it easy to work with LLMs"),
    Document(page_content="FAISS is a library for efficient similarity search and clustering of dense vectors."),
    Document(page_content="LangChain: The Foundational Framework, Purpose: Builds modular, linear, and reactive LLM workflows like Retrieval-Augmented Generation (RAG) and simple chatbots."),
    Document(page_content="LangGraph: The Agent Orchestrator, Purpose: Orchestrates complex, stateful, and multi-agent workflows that require deep autonomy and iterative loops."),
    Document(page_content="LangSmith: The Observability Platform, Purpose: Debugs, tests, evaluates, and monitors applications and agents in production.")
]

# Step 2: Initialize embeddings model
embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Step 3: Create FAISS vector store in memory
vectorstore = FAISS.from_documents(
    documents=docs,
    embedding=embedding_model
)

retriever = vectorstore.as_retriever(
    search_type="mmr", # this enables MMR
    search_kwargs={"k": 2, "lambda_mult":1} # k = top results, lambda_mult = relevance-diversity balance 
)

query = "What is Langchain?"


results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"Result {i+1}: {doc.page_content}")