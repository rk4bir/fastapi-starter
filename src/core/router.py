from logging import Logger

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from src.config import get_logger
from src.core.schema import CoreResponseSchema

core_router = APIRouter()
resp_data = CoreResponseSchema()


@core_router.get("/")
def home(
    logger: Logger = Depends(get_logger),
):
    logger.info("GET / - welcome")
    resp_data.message = "Welcome to FastAPI!"
    return JSONResponse(resp_data.dict(), status_code=200)


@core_router.get("/heartbeat")
def heartbeat(
    logger: Logger = Depends(get_logger),
):
    logger.info("GET /heartbeat - pong")
    resp_data.message = "PONG!"
    return JSONResponse(resp_data.dict(), status_code=200)
