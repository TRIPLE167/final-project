import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'asfsafasAF1232!@$#')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'postgresql://ui_fy97_user:jUaib7p4nRnMo4f5sZ3MDAPuVQabCJvG@dpg-cq1fvf08fa8c739t2itg-a.frankfurt-postgres.render.com/ui_fy97')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

 
db = SQLAlchemy(app)
csrf = CSRFProtect(app)
 