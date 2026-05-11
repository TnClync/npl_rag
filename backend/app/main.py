from fastapi import FastAPI
from app.api.routes import healthy
from app.config.settings import APP_NAME 

app = FastAPI(title=APP_NAME)

app.include_router(healthy.router)