# WebBaseLoader is a document loader that loads documents from a web page. It uses the requests library to fetch the HTML content of the web page, and then uses BeautifulSoup to parse the HTML and extract the text content. The extracted text content is then returned as a list of Document objects.

from langchain_community.document_loaders import WebBaseLoader
import bs4 # bs4 - BeautifulSoup4 is a library for parsing HTML and XML documents.

url = "https://lilianweng.github.io/posts/2023-06-23-agent"

loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))

print(docs[0].page_content)