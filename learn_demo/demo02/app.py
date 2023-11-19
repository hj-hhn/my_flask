#!/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author : jie.hou
# @File : app.py
# @Time : 2023/11/13 22:28
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import learn_demo.demo02.mysql_config_utils as my_conf
from sqlalchemy import text

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{my_conf.USERNAME}:{my_conf.PASSWORD}@{my_conf.HOSTNAME}:{my_conf.PORT}/{my_conf.DATABASE}?charset=utf8'

print(app.config['SQLALCHEMY_DATABASE_URI'])

db = SQLAlchemy(app)

with app.app_context():
    with db.engine.connect() as conn:
        rs = conn.execute(text("show databases"))
        print(rs.fetchone())


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    username = db.Column(db.String(100), nullable=False)

    password = db.Column(db.String(100))

with app.app_context():
    db.create_all()