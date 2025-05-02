# app/routes/extract_milestone.py
from fastapi import APIRouter
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

router = APIRouter()

# Load model once (ideally move to shared module later)
model_name = "NousResearch/Meta-Llama-3-8B-Instruct"  # or local path if downloaded
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")

class MilestoneRequest(BaseModel):
    text: str

@router.post("/extract-milestones")
async def extract_milestones(data: MilestoneRequest):
    prompt = (
        "Extract all project milestones from the text below. For each milestone, return a JSON object with:\n"
        "- 'description' (the milestone's name or description)\n"
        "- 'start' (start date in YYYY-MM-DD)\n"
        "- 'end' (end date in YYYY-MM-DD)\n"
        f"Text:\n{data.text}\n\n"
        "Only return a JSON array in this format:\n"
        "[{\"description\": \"...\", \"start\": \"YYYY-MM-DD\", \"end\": \"YYYY-MM-DD\"}]"
    )

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=300)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {"milestones": response}
