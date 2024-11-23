from flask import Blueprint, jsonify

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/users', methods=['GET'])
def get_users():
    ...
