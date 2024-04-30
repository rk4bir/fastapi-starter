from src.core.schemas import CoreResponseSchema


def get_response_schema():
    yield CoreResponseSchema(**{"status": True, "message": ""})
