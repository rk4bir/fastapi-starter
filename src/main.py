from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import logger, ALLOWED_ORIGINS
from src.core.router import core_router

app: FastAPI = FastAPI()
# middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# routers
app.include_router(core_router, prefix="")
