from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Prompt(BaseModel):
    prompt: str

@router.post("/generate")
async def generate_text(data: Prompt):
    return {"response": f"Mocked response for: {data.prompt}"}