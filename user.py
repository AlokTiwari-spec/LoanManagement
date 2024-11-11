from flask import Blueprint,request
from flask.views import MethodView
from models import UserModel,db

user_bp = Blueprint("user",__name__)

class User(MethodView):
    
    @user_bp.route('/user/<user_id>',methods=['Get'])
    def get(user_id):
        data_from_db = UserModel.query.filter_by(id=user_id).first()
        return {"user name is ": data_from_db.userName}
        # data_from_db = UserModel.query.all()
        # return {"loan name is ":data_from_db[0].loanName}
    
    # @user_bp.route('/user/',methods=['Post'])
    # def post():
    #     request_data = request.get_json()
    #     new_user = UserModel(**request_data)
    #     db.session.add(new_user)
    #     db.session.commit()
    #     return {"Successfully user added ": "successfully"}
    
    # @user_bp.route('/user/<int:user_id>',methods=['Put'])
    # def put(user_id):
    #     request_data = request.get_json()
    #     data_from_db = UserModel.query.filter_by(id= str(user_id)).first()
    #     data_from_db.userName = request_data["userName"]
    #     db.session.commit()
    #     return {"user details updated ": "successfully"}
        
    @user_bp.route('/user/<int:user_id>',methods=['Delete'])    
    def delete(user_id):
        data_from_db = UserModel.query.filter_by(id=str(user_id)).first()
        if data_from_db is not None :
            db.session.delete(data_from_db)
            db.session.commit()

        return {"user details deleted ": "successfully"}