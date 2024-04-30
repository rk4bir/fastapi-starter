from logging import Logger

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from src.config import get_logger
from src.core.deps import get_response_schema
from src.core.schemas import CoreResponseSchema

core_router = APIRouter()


@core_router.get("/")
def home(
    logger: Logger = Depends(get_logger),
    resp_data: CoreResponseSchema = Depends(get_response_schema),
):
    logger.info("GET / - welcome")
    resp_data.message = "Welcome to FastAPI!"
    return JSONResponse(resp_data.dict(), status_code=200)


@core_router.get("/heartbeat")
def heartbeat(
    logger: Logger = Depends(get_logger),
    resp_data: CoreResponseSchema = Depends(get_response_schema),
):
    logger.info("GET /heartbeat - pong")
    resp_data.message = "PONG!"
    return JSONResponse(resp_data.dict(), status_code=200)
