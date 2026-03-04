from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Voorraad Beheer Systeem")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Voorraad systeem draait"}

@app.get("/locaties")
def get_locaties(db: Session = Depends(get_db)):
    return db.query(models.Locatie).all()
