# Retrievers in langchain
"""
Data Source <------- Retriever ----------> Documents
                         |
                         |
                         |
                        Query
"""
# Retriver is Component in langchain that fetches relevant documents from a data souce in response to a user's query.
# All retrivers in LangChain are runnanles.

# Types of Retrivers:
"""
Types are based on the data source they fetch documents from. Some common types of retrievers are:

    1. WikipediaRetriever: Fetches documents from Wikipedia based on a query.
    2. VectorStoreRetriever: Fetches documents from a vector store based on a query.
    3. ArxivRetriever: Fetches documents from Arxiv based on a query.

Another types are based on search strategy they use to fetch documents.  [search strategy means the way in which the retriever fetches documents from the data source based on a query].
Some common types of retrievers are:

    1. MMR (Maximal Marginal Relevance) Retriever: Fetches documents based on a query using MMR search strategy.
    2. MultiQuery Retriever: Fetches documents based on a query using multiple queries to fetch relevant documents.
    3. Contextual Compression Retriever: Fetches documents based on a query using contextual compression search strategy.
"""
