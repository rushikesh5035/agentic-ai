# RAG - Retrival Augmented Generation

# RAG has 4 main components:
# 1. Document Loaders: Load documents from various sources (e.g., PDFs, web pages, databases).
# 2. Text Splitters: Split documents into smaller chunks for processing.
# 3. Vector Stores: Store and index the document chunks for efficient retrieval.
# 4. Retrival and Generation: Retrieve relevant document chunks based on a query and generate responses using a language model.


## 1. Document Loaders:
### 1.1. TextLoader: Load text files from local storage.
### 1.2. PDFLoader: Load PDF files from local storage.
### 1.3. WebBaseLoader: Load web pages from the internet.
### 1.4. CSVLoader: Load CSV files from local storage.