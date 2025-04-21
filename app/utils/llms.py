from langchain.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_ollama.llms import OllamaLLM

from app.constants import LLM_MODEL, EMBEDDING_MODEL, CHROMA_PATH, PROMPT_TEMPLATE


def query_llama(question: str):
    default_response = "Unable to find matching results."

    embedding_fn = OllamaEmbeddings(model=EMBEDDING_MODEL)
    vector_db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_fn)

    search_results = vector_db.similarity_search_with_relevance_scores(
        question, k=3, score_threshold=0.6
    )

    if not search_results:
        return default_response, None

    context = "\n\n---\n\n".join(doc.page_content for doc, _ in search_results)
    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE).format(
        context=context, question=question
    )

    model = OllamaLLM(model=LLM_MODEL)
    response = model.invoke(prompt)

    sources = {doc.metadata.get("source") for doc, _ in search_results}

    return response, sources or None
