from pydantic import BaseModel

class ScoreBase(BaseModel):
    student_id: int
    subject_id: int
    score: float

class ScoreCreate(ScoreBase):
    pass

class Score(ScoreBase):
    id: int

    class Config:
        orm_mode = True