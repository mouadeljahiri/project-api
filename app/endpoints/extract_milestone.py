@router.post("/extract-milestones")
async def extract_milestones(data: MilestoneRequest):
    try:
        prompt = (
            "Extract all project milestones from the text below. For each milestone, return a JSON object with:\n"
            "- 'description' (the milestone's name or description)\n"
            "- 'start' (start date in YYYY-MM-DD)\n"
            "- 'end' (end date in YYYY-MM-DD)\n\n"
            f"Text:\n{data.text}\n\n"
            "Only return a JSON array in this format:\n"
            '[{"description": "...", "start": "YYYY-MM-DD", "end": "YYYY-MM-DD"}]'
        )

        print("🧠 Prompt sent to model:\n", prompt[:1000])  # Log partial prompt for safety

        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        outputs = model.generate(**inputs, max_new_tokens=300)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        print("🟢 Model raw output:\n", response)

        return {"milestones": response}

    except Exception as e:
        import traceback
        print("🔥 Exception in LLaMA API:")
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"error": f"Server crash: {str(e)}"})
