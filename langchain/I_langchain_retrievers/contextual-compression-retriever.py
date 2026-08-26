## Contextual Compression Retriever

## the contexutal compression retriever in langchain is an advanced retriever that improves retrieval quality by compressing documents after retrieval -- keeping only the relevant content based on the user's query.

"""
Query: "What is photosynthesis?

Retrieved Document (by a traditional retriever):
 "The grand canyon sia famous natural side.
  Photosynthesis is how plants convert light into energy.
  Many tourists visit every year. 

Problem:
 - the retriever returns the entire paragraph
 - Only one sentence is actually relevant to the query
 - the rest is irrelevant noise that wastes context window and can confuse the LLM

What Contextual Compression Retriever does:
Returns only the relevant part e.g.
    - Photosynthesis is how plants convert light into energy.

How it works:
    1. Base Retriever (e.g., FAISS, Chroma) retrives N documents
    2. A compressor (usially an LLM) is applied to each document
    3. the compressor keeps only the parts relevant to the query, 
    4. irrelevant content is discarded, and the compressed documents are returned to the user.

When to use:
- documents are long and contain mixed information.
- want to reduce context lenght of LLMs
- need to improve answer accuracy in RAG pipelines
"""

import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_core.documents import Document
from langchain_groq import ChatGroq

load_dotenv()

os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


# Recreate the document objects from the previous data
docs = [
    Document(page_content=(
        """The Grand Canyon is one of the most visited natural wonders in the world.
        Photosynthesis is the process by which green plants convert sunlight into energy.
        Millions of tourists travel to see it every year. The rocks date back millions of years."""
    ), metadata={"source": "Doc1"}),

    Document(page_content=(
        """In medieval Europe, castles were built primarily for defense.
        The chlorophyll in plant cells captures sunlight during photosynthesis.
        Knights wore armor made of metal. Siege weapons were often used to breach castle walls."""
    ), metadata={"source": "Doc2"}),

    Document(page_content=(
        """Basketball was invented by Dr. James Naismith in the late 19th century.
        It was originally played with a soccer ball and peach baskets. NBA is now a global league."""
    ), metadata={"source": "Doc3"}),

    Document(page_content=(
        """The history of cinema began in the late 1800s. Silent films were the earliest form.
        Thomas Edison was among the pioneers. Photosynthesis does not occur in animal cells.
        Modern filmmaking involves complex CGI and sound design."""
    ), metadata={"source": "Doc4"})
]

# Create a FAISS vector store from the documents
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vectorstore = FAISS.from_documents(
    documents=docs,
    embedding=embedding_model
)

base_retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

# set up the compressor using an LLM (ChatGroq in this case) with the LLMChainExtractor
llm = ChatGroq(model="openai/gpt-oss-20b")
compressor = LLMChainExtractor.from_llm(llm)

# create the contextual compression retriever
compression_retriever = ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=compressor
)

# Query
query = "What is photosynthesis?"

compressed_results = compression_retriever.invoke(query)

for i, doc in enumerate(compressed_results):
    print(f"\n ---- Result {i+1} ----")
    print(doc.page_content)

"""
---- Result 1 ----
Photosynthesis is the process by which green plants convert sunlight into energy.

---- Result 2 ----
The chlorophyll in plant cells captures sunlight during photosynthesis.

"""