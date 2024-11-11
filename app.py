from flask import Flask,request
from loans import loan_bp
from user import user_bp
from userAccount import updateAccount_bp
from userLogin import login_bp
from userLogout import logout_bp
from userRegistration import reg_bp
from flask_sqlalchemy import SQLAlchemy
from models import db
from flask_jwt_extended import JWTManager
import secrets
from flask_smorest import Api

app = Flask(__name__)

# Generate secret keys
secret_key = secrets.token_hex(32)
jwt_secret_key = secrets.token_hex(32)
# app.debug=True
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://Alok:password@localhost:5433/LoanManagement"
app.config["PROPAGATE_EXCEPTION"] = True
app.config["API_TITLE"] = "Policy REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PRIFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@localhost:5432/bank_management_system"
app.config['SQLALCHEMy_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = secret_key
app.config['JWT_SECRET_KEY'] = jwt_secret_key

db.init_app(app)
jwt = JWTManager(app)
# blacklist = set()

with app.app_context():
        db.create_all()

# JWT token blacklist check
@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
        jti = jwt_payload['jti']
        return jti in blacklist

api = Api(app)

app.register_blueprint(loan_bp)
app.register_blueprint(user_bp)
app.register_blueprint(updateAccount_bp)
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(reg_bp)

if __name__ == "__main__":
        app.run(debug=True)