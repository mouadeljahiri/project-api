from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = FastAPI()

# Load model and tokenizer once
tokenizer = AutoTokenizer.from_pretrained(
    "./", trust_remote_code=True
)
model = AutoModelForCausalLM.from_pretrained(
    "./",
    torch_dtype=torch.float16,
    device_map="auto"
)

# Input schema
class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_text(data: PromptRequest):
    inputs = tokenizer(data.prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=100,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7
    )
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": result}
