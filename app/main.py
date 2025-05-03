from fastapi import FastAPI
from app.endpoints import generate, parse_email, extract_schedule, extract_milestone

app = FastAPI(
    title="Project Intelligence API",
    version="1.0.0"
)

# Register endpoints
app.include_router(generate)
app.include_router(parse_email)
app.include_router(extract_schedule)
app.include_router(extract_milestone)
