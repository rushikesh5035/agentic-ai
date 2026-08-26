## TextLoader

## Text loader is a document loader that loads text files from local storage. It reads the content of the text file and returns it as a string (documents object)

from langchain_community.document_loaders import TextLoader

loader = TextLoader("sample.txt", encoding="utf-8")

docs = loader.load()

print(docs)
print(type(docs)) # <class 'list'>

print(docs[0].page_content) # returns the content of the text file as a string