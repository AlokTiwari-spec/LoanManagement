from flask import Blueprint, request,jsonify
from werkzeug.security import generate_password_hash
from models import UserModel, db
from sqlalchemy.exc import IntegrityError


reg_bp = Blueprint('reg', __name__)

@reg_bp.route('/register/',methods=['Post'])
def userRegistration():
    request_data = request.get_json()
    hashed_password = generate_password_hash(request_data['password'], method='pbkdf2:sha256')
    user_name=request_data['userName']
    new_user = UserModel(
            id=request_data['id'],
            userName=user_name,
            password=hashed_password
        )
    # new_user = UserModel(**request_data)
    try:
        db.session.add(new_user)
        db.session.commit()
        return {user_name: "  added successfully"}
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "User_id already exists!"}), 409 

