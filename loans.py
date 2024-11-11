from flask import Blueprint,request,jsonify
from flask.views import MethodView
from models import UserModel,LoanModel,db
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import SQLAlchemyError

loan_bp = Blueprint("loan",__name__)

class Loan(MethodView):
    
    @loan_bp.route('/loan/<loan_id>',methods=['Get'])
    @jwt_required()
    def get(loan_id):
        userId = get_jwt_identity()
        user_data_from_db = UserModel.query.filter_by(id=userId).first()
        if user_data_from_db is not None :
            try:
                loan_data_from_db = LoanModel.query.filter_by(user_id=user_data_from_db.id, id=loan_id).first()
                if loan_data_from_db is not None :
                    return {"loan name is ":loan_data_from_db.loanName}
                return {" no loans found for ": user_data_from_db.userName}
            except SQLAlchemyError as e:
                db.session.rollback()
                return jsonify({"error": "Database error", "message": str(e)}), 500
            
        return {" no user data found ": "with given user"}
        
    
    @loan_bp.route('/loan/',methods=['Post'])
    @jwt_required()
    def post():
        request_data = request.get_json()
        print(request_data)
        userId = get_jwt_identity()
        print(userId)
        user_data_from_db = UserModel.query.filter_by(id=userId).first()
        if user_data_from_db is not None :
            try:
                new_loan = LoanModel(
                id=request_data['id'],
                loanName=request_data['loanName'],
                user_id=user_data_from_db.id,
                userName =user_data_from_db.userName,
                address = request_data['address'],
                contact = request_data['contact'],
                email = request_data['email']
                )
                print(new_loan)
                # new_loan = LoanModel(**request_data)
                db.session.add(new_loan)
                db.session.commit()
                return {"Successfully loan added ": "successfully"}
            
            except SQLAlchemyError as e:
                db.session.rollback()
                return jsonify({"error": "Database error", "message": str(e)}), 500
            
        return {" no user data found ": "with given user"}
        
    @loan_bp.route('/loan/<int:loan_id>',methods=['Put'])
    @jwt_required()
    def put(loan_id):
        userId = get_jwt_identity()
        user_data_from_db = UserModel.query.filter_by(id=userId).first()
        loan_data_from_db = LoanModel.query.filter_by(user_id=user_data_from_db.id, id=str(loan_id)).first()
        if loan_data_from_db is not None:
            request_data = request.get_json()
            # data_from_db = LoanModel.query.filter_by(id= str(loan_data_from_db.id)).first()
            loan_data_from_db.loanName = request_data["loanName"]
            try:
                db.session.commit()
                return {"loan details updated ": "successfully"}
            except SQLAlchemyError as e:
                db.session.rollback()
                return jsonify({"error": "Database error", "message": str(e)}), 500
            
        return {" no loans found for ": user_data_from_db.userName}


    @loan_bp.route('/loan/<int:loan_id>',methods=['Delete'])
    @jwt_required() 
    def delete(loan_id):
        userId = get_jwt_identity()
        user_data_from_db = UserModel.query.filter_by(id=userId).first()
        loan_data_from_db = LoanModel.query.filter_by(user_id=user_data_from_db.id, id=str(loan_id)).first()
        if loan_data_from_db is not None :
            try:
                db.session.delete(loan_data_from_db)
                db.session.commit()
                return {"loan details deleted ": "successfully"}
            
            except SQLAlchemyError as e:
                db.session.rollback()
                return jsonify({"error": "Database error", "message": str(e)}), 500
            
        return {" no loans found for ": user_data_from_db.userName}