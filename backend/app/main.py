import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.config.settings import APP_NAME
from app.api.routes import healthy

load_dotenv()

# ✅ FastAPI instance (QUAN TRỌNG)
app = FastAPI(
    title= APP_NAME,
    debug=os.getenv("DEBUG", "False") == "True"
)

app.include_router(healthy.router)

# =========================
# CORS
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# ROUTES TEST
# =========================
@app.get("/api")
def root():
    return {"message": "API is running"}


app.mount(
    "/",
    StaticFiles(directory="../frontend", html=True),
    name="frontend"
)
