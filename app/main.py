from fastapi import FastAPI
from app.api.student.router import router as student_router

app = FastAPI()

app.include_router(student_router, prefix="/students", tags=["Students"])
