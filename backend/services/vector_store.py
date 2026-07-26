from typing import Optional
import chromadb
from chromadb.config import Settings
import os


class VectorStore:
    def __init__(self, persist_directory: Optional[str] = None):
        persist_directory = persist_directory or os.environ.get("CHROMA_DIR", "./chroma_db")
        self.client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory=persist_directory))
        self.collection = self.client.get_or_create_collection(name="project_ideas")

    def add_idea(self, id: str, metadata: dict, embedding: list):
        try:
            self.collection.add(ids=[id], metadatas=[metadata], embeddings=[embedding])
        except Exception:
            pass
