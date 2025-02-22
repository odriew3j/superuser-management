from extensions import db
from flask import Blueprint, request, jsonify, send_from_directory
from service.superUserService import UserService  
from controller.getUserControll import get_users_controll  

api = Blueprint('api', __name__)

@api.route("/")
def api_root():
    return jsonify({"message": "Welcome to the API"})

@api.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("../frontend/static", filename)

@api.route("/users", methods=['GET'])
def get_users():
    user_list = get_users_controll()
    return jsonify(user_list) 

@api.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or "username" not in data or "email" not in data:
        return jsonify({"error": "Missing username or email"}), 400

    try:
        new_user = UserService.create_user(data)
        return jsonify({"message": "User created successfully", "id": new_user.id}), 201
    except Exception as e:
        print(f"Error creating user: {e}")
        return jsonify({"error": "Failed to create user"}), 500