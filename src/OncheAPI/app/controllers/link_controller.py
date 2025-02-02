from flask import Blueprint, jsonify, render_template

link_controller = Blueprint('link_controller', __name__)

@link_controller.route(f'/', methods=['GET'])
def homepage():
    return render_template('parametres/index.html')

@link_controller.route(f'/Database', methods=['GET'])
def database():
    return render_template('parametres/Database.html')

@link_controller.route(f'/connexion', methods=['GET'])
def connexion():
    return render_template('parametres/connexion.html')

@link_controller.route(f'/informations', methods=['GET'])
def information():
    return render_template('parametres/informations.html')

@link_controller.route(f'/aide', methods=['GET'])
def aide():
    return render_template('parametres/aide.html')