from fastapi import APIRouter, UploadFile
from app.services.transaction_service import analyze_transactions

router = APIRouter()

@router.post("/analyze")
async def analyze(file: UploadFile):
    return analyze_transactions(file)
