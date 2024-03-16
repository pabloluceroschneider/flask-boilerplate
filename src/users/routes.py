from flask import Blueprint, abort

from .controller import UserController

users = Blueprint('users', __name__)

@users.route('/', methods=["GET"])
def get_all_users():
    try:
        return UserController.get_all_users()
    except:
        return "error"

@users.route('/', methods=["POST"])
def create_user():
    try:
        return UserController.create_user()
    except:
        return "error"

@users.route('/<user_id>', methods=["PUT"])
def update_user(user_id):
    try:
        return UserController.update_user(user_id)
    except:
        return "error"

@users.route('/<user_id>', methods=["DELETE"])
def remove_user(user_id):
    try:
        return UserController.remove_user(user_id)
    except:
        return "error"

@users.route('/error-500', methods=["GET"])
def throw_error_500():
    abort(500)

@users.route('/error-400', methods=["GET"])
def throw_error_400():
    abort(400)
