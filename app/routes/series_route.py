from app.controllers import series_controller
from flask import Blueprint

bp = Blueprint("series", __name__, url_prefix="/series")

bp.post("")(series_controller.create_controller)
bp.get("")(series_controller.get_controller)
bp.get("/<int:serie_id>")(series_controller.get_by_id_controller)
