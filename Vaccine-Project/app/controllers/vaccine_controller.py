
from flask import jsonify, request
import datetime as dt
from app.models.vaccine_model import Vaccine
from app.configs.database import db
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.query import Query
from sqlalchemy.exc import IntegrityError, InvalidRequestError

def post_vaccine():
    try:
        session:Session = db.session()

        data = request.get_json()
        vaccine = Vaccine(**data)
        cpf_valid = len(vaccine.cpf)
        if cpf_valid != 11:
            raise InvalidRequestError
        
        vaccine.first_shot_date = dt.datetime.utcnow()
        vaccine.second_shot_date = dt.datetime.utcnow() + dt.timedelta(days=90)

        session.add(vaccine)
        session.commit()
    
        return jsonify(vaccine), 201
    except InvalidRequestError:
        return {"Err": "Wrong Key"},400
    except IntegrityError:
        return {"Err" : "Duplicated Key or Invalid"},400
    except TypeError:
        return {"Err": "Invalid Key"}, 400
def person_vaccine(cpf : str):
    base_query:Query = db.session.query(Vaccine)
    card:Vaccine = base_query.filter(Vaccine.cpf == cpf).first()
    if not card:
        return {"Err": "Cpf is not found"}, 404


    return jsonify(card),200
def read_vacine():
    try:

        base_query : Query = db.session.query(Vaccine)
        cards = base_query.order_by(Vaccine.name).all()

        return jsonify(cards),200
    except :
        return {"Error": "DataBase Not Found"}, 404