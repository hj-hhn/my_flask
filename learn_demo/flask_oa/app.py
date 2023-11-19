#!/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author : jie.hou
# @File : app.py
# @Time : 2023/11/13 22:28
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import config as conf
from Models import UserModel
from exts import db
from blueprints.auth import bp as auth_bp
from blueprints.qa import bp as qa_bp

from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(conf)



db.init_app(app=app)

migrate = Migrate(app, db)

app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)




if __name__ == '__main__':
    app.run()