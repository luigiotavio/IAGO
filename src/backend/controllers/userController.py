from flask import Blueprint, request, jsonify
from services.userService import UserService

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.json
    result = UserService.create_user(
        name=data.get('name'),
        email=data.get('email'),
        occupation=data.get('occupation'),
        cell=data.get('cell'),
        age=data.get('age'),
        gender=data.get('gender'),
        subscription_id=data.get('subscription_id'),
        role=data.get('role')
    )
    return jsonify(result)

@user_bp.route('/', methods=['GET'])
def get_all_users():
    try:
        users = UserService.get_all_user()
        return jsonify(users)
    except Exception as e:
        return jsonify({"error": str(e)})

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    result = UserService.get_user(user_id)
    return jsonify(result)

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    result = UserService.update_user(
        user_id,
        name=data.get('name'),
        email=data.get('email'),
        occupation=data.get('occupation'),
        cell=data.get('cell'),
        age=data.get('age'),
        gender=data.get('gender'),
        subscription_id=data.get('subscription_id'),
        role=data.get('role')
    )
    return jsonify(result)

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = UserService.delete_user(user_id)
    return jsonify(result)

