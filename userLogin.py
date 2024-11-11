from flask import Blueprint, request,jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from models import UserModel, db


login_bp = Blueprint('login', __name__)
@login_bp.route('/login/',methods=['Post'])
def userLogin():
    request_data = request.get_json()
    try:
        user = UserModel.query.filter_by(userName=request_data['userName']).first()
        if user and check_password_hash(user.password, request_data['password']):
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token), 200
        return jsonify({"error": "Invalid credentials!"}), 401
    except Exception as e:
        return jsonify({"error": "An error occurred", "message": str(e)}), 500