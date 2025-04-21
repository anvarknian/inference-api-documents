from typing import Optional, Set
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    prompt: str = Field(
        default="How does Alice meet the Mad Hatter?",
        description="The question or prompt to send to the LLM."
    )


class ChatResponse(BaseModel):
    response: str = Field(
        default="Somewhere in this universe 🙂",
        description="The generated response from the LLM."
    )
    sources: Optional[Set[str]] = Field(
        default=None,
        description="A set of source document identifiers (e.g., file names)."
    )
