from app.configs.database import db
from sqlalchemy import Column, String, DateTime
from dataclasses import dataclass


@dataclass
class Vaccine(db.Model):
    cpf:str
    name:str
    vaccine_name:str
    first_shot_date:str
    second_shot_date:str
    health_unit_name:str
    
    __tablename__ = "vaccine_cards"

    cpf = Column(String(11), primary_key = True)
    name = Column(String, nullable = False)
    vaccine_name = Column(String, nullable= False)
    first_shot_date = Column(DateTime)
    second_shot_date = Column(DateTime)
    health_unit_name = Column(String)
