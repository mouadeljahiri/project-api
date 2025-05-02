# app/routes/extract_milestone.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class MilestoneRequest(BaseModel):
    text: str

@router.post("/extract-milestones")
async def extract_milestones(data: MilestoneRequest):
    # dummy logic for now
    return [
        {"description": "Kickoff", "start": "2025-06-01", "end": "2025-06-02"},
        {"description": "Delivery", "start": "2025-09-10", "end": "2025-09-20"}
    ]
