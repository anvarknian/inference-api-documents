import traceback

from fastapi import APIRouter, HTTPException

from app.models.chat import ChatRequest, ChatResponse
from app.utils.custom_logger import setup_logger
from app.utils.llms import query_llama

logger = setup_logger(__name__)

router = APIRouter()


@router.post("/", response_model=ChatResponse)
async def chat_with_llama(request: ChatRequest):
    try:
        logger.info(f"Received question: {request.prompt}")

        response, sources = query_llama(request.prompt)

        logger.info(f"Generated response: {response}")
        logger.info(f"Sources: {sources}")

        return ChatResponse(response=response, sources=sources)

    except Exception as e:
        logger.error(f"Error while querying LLaMA: {str(e)}")
        logger.debug(traceback.format_exc())
        raise HTTPException(status_code=500, detail="An internal error occurred while processing the request.")
