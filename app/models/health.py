from pydantic import BaseModel, Field


class Health(BaseModel):
    isHealthy: bool = Field(
        default=True,
        description="Indicates if the service is up and running."
    )
