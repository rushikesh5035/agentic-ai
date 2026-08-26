# Length Based Text Splitting
# This module provides a text splitter that splits text based on length. 
# Examples -> you specify a chunk size is 100, then the text will be split into chunks of 100 characters each.
# But in this approch, it will not see the semantic meaning of the text, grammatical structure, or sentence boundaries.it will just split the text based on the length of the text.

from langchain_text_splitters import CharacterTextSplitter

text = """
This is a sample text that will be split into chunks based on length. The CharacterTextSplitter class takes in a chunk size and splits the text into chunks of that size. It does not consider the semantic meaning of the text, grammatical structure, or sentence boundaries. It simply splits the text based on the specified length.
we can use this text splitter to split large documents into smaller chunks for processing or analysis. This can be useful for tasks such as text classification, information retrieval, or natural language processing. By splitting the text into smaller chunks, we can reduce the complexity of the text and make it easier to work with.
"""

splitter = CharacterTextSplitter(
    chunk_size=100, 
    chunk_overlap=0,
    separator=""
)

result = splitter.split_text(text)

print(result)