import os
from typing import List

from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import DirectoryLoader
from langchain_ollama import OllamaEmbeddings

from app.constants import DATA_PATH, CHROMA_PATH, EMBEDDING_MODEL
from app.utils.custom_logger import setup_logger

logger = setup_logger(__name__)


def generate_data_store() -> None:
    """Load documents, split into chunks, and persist to Chroma vector store."""
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)


def load_documents() -> List[Document]:
    """Loads .txt files from the data directory as Document objects."""
    loader = DirectoryLoader(DATA_PATH, glob="*.txt", show_progress=True)
    documents = loader.load()
    logger.info(f"Loaded {len(documents)} documents from {DATA_PATH}")
    return documents


def split_text(documents: List[Document]) -> List[Document]:
    """Splits documents into smaller chunks for embedding."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = splitter.split_documents(documents)
    logger.info(f"Split {len(documents)} documents into {len(chunks)} chunks.")
    return chunks


def save_to_chroma(chunks: List[Document]) -> None:
    """Embeds and stores chunks in a Chroma vector database."""
    if not os.path.exists(CHROMA_PATH):
        embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
        Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=CHROMA_PATH,
        )
        logger.info(f"Saved {len(chunks)} chunks to Chroma at {CHROMA_PATH}")
    else:
        logger.warning(f"Chroma path '{CHROMA_PATH}' already exists. Skipping save.")
