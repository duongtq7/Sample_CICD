from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.routers import students, subjects, scores

Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(students.router, prefix="/api", tags=["students"])
app.include_router(subjects.router, prefix="/api", tags=["subjects"])
app.include_router(scores.router, prefix="/api", tags=["scores"])