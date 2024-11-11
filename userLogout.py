from flask import Blueprint, request,jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from models import UserModel, db

blacklist = set()

logout_bp = Blueprint('logout', __name__)

@logout_bp.route('/logout/', methods=['POST'])
@jwt_required()
def logout():
    try:
        jti = get_jwt()['jti']  # JWT unique identifier
        blacklist.add(jti)  # Blacklist the token
        return jsonify({"message": "User logged out successfully!"}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred", "message": str(e)}), 500