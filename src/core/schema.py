from pydantic import BaseModel


class CoreResponseSchema(BaseModel):
    status: bool = True
    message: str = ""
