from sqlalchemy.orm import Session
from app.models import Subject, Score
from app.schemas import student as student_schemas, subjects as subject_schemas, scores as score_schemas
from app.models import students

# CRUD Operations for Students

def get_student(db: Session, student_id: int):
    return db.query(students.Student).filter(students.Student.id == student_id).first()

def create_student(db: Session, student_data: student_schemas.StudentCreate):
    db_student = students.Student(**student_data.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(db: Session, student_id: int, update_data: dict):
    db_student = get_student(db, student_id)
    if db_student:
        for key, value in update_data.items():
            setattr(db_student, key, value)
        db.commit()
        db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    db_student = get_student(db, student_id)
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student

# CRUD Operations for Subjects

def get_subject(db: Session, subject_id: int):
    return db.query(subjects.Subject).filter(subjects.Subject.id == subject_id).first()

def create_subject(db: Session, subject_data: subject_schemas.SubjectCreate):
    db_subject = subjects.Subject(**subject_data.dict())
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject

# CRUD Operations for Scores

def get_score(db: Session, score_id: int):
    return db.query(scores.Score).filter(scores.Score.id == score_id).first()

def create_score(db: Session, score_data: score_schemas.ScoreCreate):
    db_score = scores.Score(**score_data.dict())
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score

def update_score(db: Session, score_id: int, update_data: dict):
    db_score = get_score(db, score_id)
    if db_score:
        for key, value in update_data.items():
            setattr(db_score, key, value)
        db.commit()
        db.refresh(db_score)
    return db_score

def delete_score(db: Session, score_id: int):
    db_score = get_score(db, score_id)
    if db_score:
        db.delete(db_score)
        db.commit()
    return db_score