from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import UserModel, db
from sqlalchemy.exc import SQLAlchemyError

updateAccount_bp = Blueprint('updateAccount', __name__)

@updateAccount_bp.route('/updateAccount/', methods=['Put'])
@jwt_required()
def update_account():
    user_id = get_jwt_identity()
    request_data = request.get_json()
    try:
        data_from_db = UserModel.query.filter_by(id= str(user_id)).first()
        if data_from_db is not None:
            data_from_db.userName = request_data["userName"]
            db.session.commit()
            return {"user details updated ": "successfully"}
        return {" no user data found ": "with given user"}
    except SQLAlchemyError as e:
                db.session.rollback()
                return jsonify({"error": "Database error", "message": str(e)}), 500
