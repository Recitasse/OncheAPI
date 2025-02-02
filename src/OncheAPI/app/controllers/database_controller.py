import flask
from flask import Blueprint, jsonify
from OncheDatabase.tools.DatabaseManager import DatabaseManager

database_controller = Blueprint('database_controller', __name__)

@database_controller.route('/users', methods=['GET'])
def get_database() -> flask.Response:
    """
    Return the table of the Database
    :return:
    """
    DatabaseManager().get_all_database()
    return jsonify(dict())
