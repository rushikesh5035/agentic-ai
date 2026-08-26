# VectorStoreRetriever 
# Vector Store retriever in LangChain is the most common type of retriever that lets you search and fetch relevant documents from a vector store based on semantic similarity using vector embeddings.
'''
1. You store your documents in a vector store liek FAISSS, Chroma, Weaviate, Pinecone etc
2. Each document is converted into a dense vector using an embedding model
3. When the user enters a query:
    - it's also turned into a vector
    - the retriver compares the query vector with the stored vectors
    - it retrives the top-k most similar ones.
'''

import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

load_dotenv()

os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")


# Step 1: Source documents
documents = [
   Document(page_contents = "LangChain is a framework for developing applications powered by language models."),
   Document(page_contents = "It can be used for chatbots, Generative Question-Answering (GQA), summarization, and much more."),
   Document(page_contents = "LangChain provides a standard interface for all LLMs, and it also provides integrations with other tools."),
   Document(page_contents = "LangChain is modular, so you can use just the parts you want."),
]

# Step 2: Initialize embeddings model
embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Step 3: Create chroma vector store in memory
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name="langchain_docs"
)

# Step 4: Create a retriever from the vector store
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# step 5: Query the retriever
query = "What is LangChain?"
results = retriever.invoke(query)

for i, result in enumerate(results):
    print(f"Result {i+1}: {result.page_content}")
