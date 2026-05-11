from fastapi import APIRouter
from datetime import datetime


router = APIRouter(tags=["Healthy Check"])


@router.get("/health")
async def health_check():
    return {
        "status": "ok",
        "message": "API is running",
        "timestamp": datetime.utcnow().isoformat()
    }