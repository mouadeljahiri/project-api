from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class EmailData(BaseModel):
    subject: str
    body: str

@router.post("/parse-email")
def parse_email(data: EmailData):
    return {
        "project_name": "Extracted XYZ",
        "deadline": "2025-06-30",
        "actions": ["follow up", "create schedule"]
    }