# PyPDFLoader
# PyPDFLoader is a document loader that uses the PyPDF2 library to load PDF files. It can extract text from PDF files and return it as a list of Document objects.

# pyPDFLoader is used mostly with text-based PDFs. It may not work well with scanned PDFs or PDFs that contain images.

# Here are some recommended loaders based on the type of PDF you are working with:
# 1 - Simple, clean PDFs             ----    pyPDFLoader
# 2 - PDFs with tables/columns       ----    PDFPlumberLoader
# 3 - Scanned/images PDFs            ----    UnstructuredPDFLoader or AmazonTextractPDFLoader
# 4 - Need layout and image data     ----    PyMuPDFLoader
# 5 - Want best structure extraction ----    UnstructuredPDFLoader

from langchain_community.document_loaders import PyPDFLoader

pdf_loader = PyPDFLoader("attention.pdf")

pdf_documents = pdf_loader.load()

# print(pdf_documents)
print(type(pdf_documents)) # <class 'list'>

print(pdf_documents[0].page_content) # returns the content of the first page of the PDF file as a string

print(len(pdf_documents)) # returns the number of pages in the PDF file