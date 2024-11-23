from flask import Blueprint, jsonify

database_controller = Blueprint('database_controller', __name__)

@database_controller.route('/users', methods=['GET'])
def get_users():
    ...
