import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


text = "This is a test sentence for generating embeddings."

embedding_vector = embeddings.embed_query(text)

doc_result = embeddings.embed_documents([text, "This is a testing document for embedding with hugging face"])

print(doc_result)