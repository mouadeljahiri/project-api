from fastapi import FastAPI
from app.routes import generate, parse_email, extract_schedule, extract_milestone

app = FastAPI()

app.include_router(generate.router)
app.include_router(parse_email.router)
app.include_router(extract_schedule.router)
app.include_router(extract_milestone.router)
