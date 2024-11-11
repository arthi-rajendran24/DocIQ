# chatbot.py

import os
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain_ollama import ChatOllama
from langchain import PromptTemplate
from langchain.chains import RetrievalQA
import streamlit as st

class ChatbotManager:
    def __init__(
        self,
        model_name: str = "BAAI/bge-small-en",
        device: str = "cpu",
        encode_kwargs: dict = {"normalize_embeddings": True},
        llm_model: str = "llama3.2",
        llm_temperature: float = 0.7,
        collection_name: str = "vector_db",
        persist_directory: str = "chroma_db",  # Directory where Chroma data is stored
    ):
        self.model_name = model_name
        self.device = device
        self.encode_kwargs = encode_kwargs
        self.llm_model = llm_model
        self.llm_temperature = llm_temperature
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

        # Initialize the retriever
        self.retriever = self.chroma.as_retriever(search_kwargs={"k": 3})


        # Initialize the language model using ChatOllama
        self.llm = ChatOllama(
            model=self.llm_model,
            temperature=self.llm_temperature,
        )

        # Define the prompt template
        self.prompt_template = """Try to answer the following question by carefully checking the context. Always say "thanks for asking! " at the end of the answer. If you dont know the answer, say "I dont know".

context:
{context}

Question:
{question}
"""

        # Initialize the prompt
        self.prompt = PromptTemplate(
            template=self.prompt_template,
            input_variables=['context', 'question']
        )

        # Define chain type kwargs
        self.chain_type_kwargs = {"prompt": self.prompt}

        # Initialize the RetrievalQA chain
        self.qa = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.retriever,
            return_source_documents=False,
            chain_type_kwargs=self.chain_type_kwargs,
            verbose=False
        )

    def test_retriever(self, query: str):
        docs = self.retriever.get_relevant_documents(query)
        for doc in docs:
            print(doc.page_content)

    def get_response(self, query: str) -> str:
        try:
            response = self.qa.run(query)
            return response
        except Exception as e:
            st.error(f"⚠️ An error occurred while processing your request: {e}")
            return "⚠️ Sorry, I couldn't process your request at the moment."
