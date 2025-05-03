from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import traceback
import json

from app.services.llama_model import tokenizer, model

router = APIRouter()

class MilestoneRequest(BaseModel):
    text: str

@router.post("/extract-milestones")
async def extract_milestones(data: MilestoneRequest):
    try:
        prompt = (
            "Extract all project milestones from the text below. "
            "For each milestone, return a JSON object with:\n"
            "- 'description' (milestone description or name)\n"
            "- 'start' (start date in YYYY-MM-DD)\n"
            "- 'end' (end date in YYYY-MM-DD)\n\n"
            f"Text:\n{data.text.strip()}\n\n"
            "Only return a JSON array like this:\n"
            '[{"description": "...", "start": "YYYY-MM-DD", "end": "YYYY-MM-DD"}]'
        )

        print("🟣 Prompt sent to model (truncated):\n", prompt[:1000])

        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        outputs = model.generate(**inputs, max_new_tokens=300)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        print("🟢 Model raw output:\n", response)

        try:
            parsed = json.loads(response)
            assert isinstance(parsed, list), "Model output is not a list"
            return {"milestones": parsed}

        except Exception as parse_error:
            print("❌ Failed to parse model output:")
            print(response)
            return JSONResponse(
                status_code=500,
                content={"error": f"LLaMA returned invalid JSON: {str(parse_error)}"}
            )

    except Exception as e:
        print("🔴 Exception in LLaMA API:")
        traceback.print_exc()
        return JSONResponse(
            status_code=500,
            content={"error": f"Server crash: {str(e)}"}
        )
