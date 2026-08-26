# WikipediaRetriever
# It is a retriver that queries the Wikipedia API to fetch relevant content for a given Query.
"""
1. You give it a query --> e.g., "Albert Einstein"
2. It sends the query to the Wikipedia API
3. It retrivers the most relevant articles from Wikipedia based on the query
4. it returns them as LangChain Document object
"""

from langchain_community.retrievers import WikipediaRetriever


# initialize the retriver
retriver = WikipediaRetriever(
    top_k_results=2,
    lang="en"
)


# Query
query = "the geographical history of india and pakistan from the perpesctive of a chinese."

# Get Relevant wikipedia document
docs = retriver.invoke(query)

# print retrieved content
for i, doc in enumerate(docs):
    print(f"\n--- Result {i+1} ---")
    print(f"Content:\n{doc.page_content}...")