from sqlmodel import SQLModel, Field, Session
from datetime import datetime
from .database import engine

# Tablo modeli
class Email(SQLModel, table=True):
    __tablename__ = "email"  # tablo adını açıkça tanımlıyoruz
    id: int = Field(default=None, primary_key=True)
    content: str
    classification: str
    label: int
    created_at: datetime = Field(default_factory=datetime.utcnow)

# Bu satır tabloyu oluşturur
SQLModel.metadata.create_all(engine)

# Toplu veri ekleme fonksiyonu
def bulk_insert_emails(emails: list[dict]):
    with Session(engine) as session:
        for e in emails:
            session.add(Email(**e))
        session.commit()

# Eğitim verisini alma fonksiyonu
def get_training_data():
    with Session(engine) as session:
        return session.exec(
            SQLModel.select(Email).where(Email.label.in_([0, 1]))
        ).all()

# Tekli veri kaydı
def save_email(content: str, classification: str, label: int):
    with Session(engine) as session:
        email = Email(content=content, classification=classification, label=label)
        session.add(email)
        session.commit()
