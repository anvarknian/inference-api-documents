from contextlib import asynccontextmanager

import ollama
from fastapi import FastAPI

from app.api.router import api_router
from app.constants import LLM_MODEL, EMBEDDING_MODEL
from app.utils.create_database import generate_data_store
from app.utils.custom_logger import setup_logger

logger = setup_logger(__name__)


@asynccontextmanager
async def lifespan(server: FastAPI):
    logger.info("Starting up: pulling models and generating data store...")

    try:
        ollama.pull(LLM_MODEL)
        ollama.pull(EMBEDDING_MODEL)
        generate_data_store()
        logger.info("Startup complete.")
    except Exception as e:
        logger.exception("Error during startup.")
        raise e

    yield

    logger.info("Shutting down: releasing resources...")


def create_app() -> FastAPI:
    server = FastAPI(
        title="Document RAG",
        version="0.1.0",
        debug=False,
        lifespan=lifespan
    )
    server.include_router(api_router, prefix="/api/v1")
    return server


app = create_app()
