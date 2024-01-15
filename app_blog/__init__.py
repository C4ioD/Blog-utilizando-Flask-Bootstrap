from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, 'data.db')

app.config['SECRET_KEY'] = '6d4c58a5ff51f3bbed5233f0c5a95a76d9a650ee264fdc3fad827529e585b0ef'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path  # o banco de dados sera criado na mesma pasta em que estiver o arquivo __init__.py


db= SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view ='login'
login_manager.login_message_category = 'alert-info'


from app_blog import routes