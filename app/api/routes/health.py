from fastapi import APIRouter
from app.utils.custom_logger import setup_logger

from app.models.health import Health

# Set up logging
logger =setup_logger(__name__)

router = APIRouter()

@router.get("/", response_model=Health, summary="Health check", tags=["Health"])
async def status():
    logger.debug("Health check endpoint called.")
    return Health()
