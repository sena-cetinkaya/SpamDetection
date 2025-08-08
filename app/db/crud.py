from sqlmodel import SQLModel, Field, Session
from datetime import datetime
from .database import engine

class Email(SQLModel, table=True):
    __tablename__ = "email"  
    id: int = Field(default=None, primary_key=True)
    content: str
    classification: str
    label: int
    created_at: datetime = Field(default_factory=datetime.utcnow)

SQLModel.metadata.create_all(engine)

def bulk_insert_emails(emails: list[dict]):
    with Session(engine) as session:
        for e in emails:
            session.add(Email(**e))
        session.commit()

def get_training_data():
    with Session(engine) as session:
        return session.exec(
            SQLModel.select(Email).where(Email.label.in_([0, 1]))
        ).all()

def save_email(content: str, classification: str, label: int):
    with Session(engine) as session:
        email = Email(content=content, classification=classification, label=label)
        session.add(email)
        session.commit()

