from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ScheduleRequest(BaseModel):
    description: str

@router.post("/extract-schedule")
def extract_schedule(data: ScheduleRequest):
    return {
        "tasks": [
            {"name": "Excavation", "start": "2025-06-01", "end": "2025-06-05"},
            {"name": "Foundation", "start": "2025-06-06", "end": "2025-06-15"}
        ]
    }
