from flask import Blueprint
from app.controllers import vaccine_controller

bp = Blueprint("vaccine", __name__, url_prefix="/vaccinations")


bp.post("")(vaccine_controller.post_vaccine)
bp.get("/<cpf>")(vaccine_controller.person_vaccine)
bp.get("")(vaccine_controller.read_vacine)