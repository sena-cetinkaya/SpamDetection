from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models.model import predict
from app.db.crud import save_email

router = APIRouter()

class EmailRequest(BaseModel):
    content: str

@router.post("/predict")
async def predict_email(data: EmailRequest):
    if not data.content:
        raise HTTPException(status_code=400, detail="Email content is required.")
    try:
        result = predict(data.content)
        save_email(data.content, result["prediction"], result["label"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
