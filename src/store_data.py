from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from split_data import splitted_data

#store the data into a vector database
#convert the data into vector embeddings usng the embedding model

project_root = Path(__file__).resolve().parents[1]
embedding=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
vectors_store=Chroma.from_documents(
    splitted_data,
    embedding,
    persist_directory=str(project_root / "data_storage")
)