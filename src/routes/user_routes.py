from flask import Blueprint, jsonify

user_routes = Blueprint('user_routes', __name__, url_prefix='/api/users')

@user_routes.route('/', methods=['GET'])
def get_users():
    return jsonify({ "mensaje": "Todos los usuarios"})


@user_routes.route('/', methods=['POST'])
def post_users():
    return jsonify({ "mensaje": "Crear los usuarios"})



