from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./app/static/uploads"
app.config['SECRET_KEY'] = "Cz_bd3krst_n3hgj94r9x4"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://vcxerksrqvcxpm:89655dba2b0f5149224f86abded8cc18b35db7ca9b802dcd7fc38cf692863b2f@ec2-50-19-109-120.compute-1.amazonaws.com:5432/d11fe5ddpihirl"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views