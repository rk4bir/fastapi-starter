from pydantic import BaseModel


class CoreResponseSchema(BaseModel):
    status: bool
    message: str
