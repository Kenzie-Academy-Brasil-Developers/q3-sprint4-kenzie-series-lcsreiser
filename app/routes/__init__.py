from flask import Flask

from .series_route import bp as bp_series


def init_app(app: Flask):
    app.register_blueprint(bp_series)
