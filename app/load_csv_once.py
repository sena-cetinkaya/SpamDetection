from app.services.train_model import prepare_data_from_csv
from app.db.database import engine
from app.db.crud import Email
from sqlmodel import Session

emails = prepare_data_from_csv()

with Session(engine) as session:
    for data in emails:
        email = Email(
            content=data["content"],
            classification=data["Classification"],
            label=data["label"]
        )
        session.add(email)
    session.commit()

print(f"{len(emails)} The record was successfully uploaded to the database.")
