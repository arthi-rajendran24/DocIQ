# vectors.py

import os
import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

class EmbeddingsManager:
    def __init__(
        self,
        model_name: str = "BAAI/bge-small-en",
        device: str = "cpu",
        encode_kwargs: dict = {"normalize_embeddings": True},
        collection_name: str = "vector_db",
        persist_directory: str = "chroma_db",  # Directory to store Chroma data
    ):
        self.model_name = model_name
        self.device = device
        self.encode_kwargs = encode_kwargs
        self.collection_name = collection_name
        self.persist_directory = persist_directory

        # Initialize embeddings
        self.embeddings = HuggingFaceEmbeddings(
            model_name=self.model_name,
            model_kwargs={"device": self.device},
            encode_kwargs=self.encode_kwargs,
        )

        # Initialize Chroma vector store
        self.chroma = Chroma(
            collection_name=self.collection_name,
            embedding_function=self.embeddings,
            persist_directory=self.persist_directory,
        )

    def load_pdf_text(self, pdf_path: str):
        text = ""
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text("text")
        return text

    def create_embeddings(self, pdf_path: str):
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"The file {pdf_path} does not exist.")

        text = self.load_pdf_text(pdf_path)
        if not text:
            raise ValueError("No text extracted from the PDF.")

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=250
        )
        splits = text_splitter.split_text(text)
        if not splits:
            raise ValueError("No text chunks were created from the document.")

        # Add documents to Chroma
        try:
            self.chroma.add_texts(splits)
            self.chroma.persist()
        except Exception as e:
            raise ConnectionError(f"Failed to add texts to Chroma: {e}")

        return "✅ Embeddings successfully created and stored in Chroma!"
