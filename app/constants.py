EMBEDDING_MODEL='nomic-embed-text'
LLM_MODEL='llama3.2'
CHROMA_PATH = "chroma"
DATA_PATH = "data/books"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""