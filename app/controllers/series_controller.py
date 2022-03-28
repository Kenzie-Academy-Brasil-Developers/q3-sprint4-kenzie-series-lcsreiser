from http import HTTPStatus
from flask import request
from app.models.series_models import Series
from psycopg2.errors import UniqueViolation

keys = ["id", "serie", "seasons", "released_date", "genre", "imdb_rating"]
keys_str = ", ".join(keys)


def table_controller():
    return Series.table_models()


def get_controller():
    try:
        table_controller()
        data = Series.get_series()

        if len(data) == 0:
            return {"data": (data)}, HTTPStatus.OK

        registers = []

        for register in data:
            registers.append(dict(zip(keys, register)))

        return {"data": (registers)}, HTTPStatus.OK

    except:
        return {"error": "Error"}, HTTPStatus.NOT_FOUND


def get_by_id_controller(serie_id):
    try:
        table_controller()
        data = Series.get_by_id_series(serie_id)

        series = dict(zip(keys, data))

        return {"data": (series)}, HTTPStatus.OK

    except:
        return {"error": "Not Found"}, HTTPStatus.NOT_FOUND


def create_controller():
    try:
        table_controller()
        data = request.get_json()

        payload = Series(**data)

        created_series = Series.create_series(payload)

        series = dict(zip(keys, created_series))

        return series, 201

    except UniqueViolation:
        return {"error": "The serie field cannot be repeated"}, HTTPStatus.BAD_REQUEST

    except:
        return {"error": f"The acceptable keys are: {keys_str}"}, HTTPStatus.BAD_REQUEST
