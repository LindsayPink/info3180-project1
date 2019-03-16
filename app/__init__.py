from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./app/static/uploads"
app.config['SECRET_KEY'] = "Cz_bd3krst_n3hgj94r9x4"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:project1@localhost/users"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views