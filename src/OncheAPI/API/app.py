from flask import Flask, Blueprint
from ._names import RENDER

app = Flask(__name__, template_folder=RENDER)
babel_onche_api = Blueprint('babel_onche_api', __name__)

__all__ = ['app']