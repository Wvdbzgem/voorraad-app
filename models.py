from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base

class Locatie(Base):
    __tablename__ = "locaties"
    id = Column(Integer, primary_key=True, index=True)
    naam = Column(String)
    type = Column(String)
    prioriteit = Column(Integer)

class Product(Base):
    __tablename__ = "producten"
    id = Column(Integer, primary_key=True, index=True)
    naam = Column(String)

class Voorraad(Base):
    __tablename__ = "voorraad"
    id = Column(Integer, primary_key=True, index=True)
    locatie_id = Column(Integer, ForeignKey("locaties.id"))
    product_id = Column(Integer, ForeignKey("producten.id"))
    aantal = Column(Integer)
    minimum = Column(Integer)

class Aanvraag(Base):
    __tablename__ = "aanvragen"
    id = Column(Integer, primary_key=True, index=True)
    van_locatie = Column(Integer, ForeignKey("locaties.id"))
    naar_magazijn = Column(Integer, ForeignKey("locaties.id"))
    product_id = Column(Integer, ForeignKey("producten.id"))
    aantal = Column(Integer)
    status = Column(String)
    datum_aangemaakt = Column(DateTime(timezone=True), server_default=func.now())
    datum_afgehandeld = Column(DateTime(timezone=True))
