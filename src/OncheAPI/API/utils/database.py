from ..app import app
from flask import render_template
from .._names import AppRoute


@app.route(f"{AppRoute.HOMEPAGE.value[0]}")
def homepage():
    return render_template(f"{AppRoute.HOMEPAGE.value[1]}")