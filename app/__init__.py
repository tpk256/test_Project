from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from api_1_0 import api as api_1_0_blueprint


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mariadb+mariadbconnector://root:rus077@127.0.0.1:3306/test"
app.register_blueprint(api_1_0_blueprint, url_prefix="/api/v1.0")

db = SQLAlchemy(app)
