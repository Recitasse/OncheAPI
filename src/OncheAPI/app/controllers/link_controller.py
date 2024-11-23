from flask import Blueprint, jsonify, render_template
from src.OncheAPI.app.config import AppRoute

link_controller = Blueprint('link_controller', __name__)

@link_controller.route(f'/', methods=['GET'])
def homepage():
    return render_template('index.html')

@link_controller.route(f'/database', methods=['GET'])
def database():
    return render_template('database.html')

@link_controller.route(f'/connexion', methods=['GET'])
def connexion():
    return render_template('connexion.html')

@link_controller.route(f'/informations', methods=['GET'])
def information():
    return render_template('informations.html')