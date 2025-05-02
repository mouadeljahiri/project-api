from fastapi import FastAPI
from endpoints import generate, email, schedule

app = FastAPI()

app.include_router(generate.router)
app.include_router(email.router)
app.include_router(schedule.router)