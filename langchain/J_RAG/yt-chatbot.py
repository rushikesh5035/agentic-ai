import os
from dotenv import load_dotenv

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

load_dotenv()

os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


# Document Ingestion
yt_video_id = "8DfvwZ812dM"

try: 
    ytt = YouTubeTranscriptApi()  
    transcript_list = ytt.fetch(yt_video_id, languages=["en"])

    transcript = " ".join(chunk["text"] for chunk in transcript_list)

    print(f"Transcript for video {yt_video_id}:\n{transcript}")
except TranscriptsDisabled:
    print("No caption available for this video")


# Text Splitting
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.create_documents([transcript])

print(len(f"The length of chunks is:\n ",chunks))

print(chunks[0])
print(chunks[20])

# Embedding Generation and Storing in Vector Store
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vector_store = FAISS.from_documents(chunks, embedding_model)

# generate id against the vectors
vector_store.index_to_docstore_id

# Pass id to see how the chunk look likes
# vector_store.get_by_ids("")

## Retrieval
retriever = vector_store.as_retriever(search_type="similarity",search_kwargs={"k": 4})


# Ask Query related to that video
retriever.invoke("What is deepmind")