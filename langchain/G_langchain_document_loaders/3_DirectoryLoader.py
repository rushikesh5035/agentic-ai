# DirectoryLoader
# it is a document loader that loads multiple documents from a directory (folder) of files.

"""
Glob Patterns

1. `**/.txt`       ----- All .txt files in subfolders
2. `*.pdf`          ----- All .pdf files in root directory
3. `data/*.csv`      ----- All .csv files in the data folder
4. `**/*`           ----- All file(any type, all folders)
"""

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

dir_loader = DirectoryLoader(
    path ="papers", 
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

# docs = dir_loader.load()

# print(len(docs))

# print(docs[10].page_content) # return the content of the 10th document in the list of documents loaded from the directory.

docs = dir_loader.lazy_load() # returns a generator of documents, which can be iterated over to get the documents one at a time.

for doc in docs:
    print(doc.page_content) # return the content of the document one at a time, as they are loaded from the directory.


## Now this code will take too much time to load.
'''
Load() v/s Lazy_load()

            load()                                              lazy_load()
---------------------------------------------------------------------------------------------------------
- Eager loading (loads everything at once)        - Lazy loading (loads documents on demand)

- Returns: A list of `Document` objects.          - Returns: A generator of `Document` objects.

- Loads all documents immediately into memory.    - Documents are not all loaded at once; they're fetches one at a time as needed

- Best When:                                      - Best When:
    1) the no of documents is small                     1) You're dealing with large documents or lots of files
    2) you want everything loaded upfront               2) you want to stream processing (e.g., chunking, embedding) without using lots of memory
'''
