#!/usr/bin python3
# -*- encoding: utf-8 -*-

from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text


app = Flask(__name__)



# 在app.config 中设置好连接数据库的信息
# 然后使用SQLAlchemy(app) 创建一个db对象
# db自动获取app中的config
HOSTNAME = '192.168.10.100'

PORT = 3306

USERNAME = 'root'

PASSWORD = '123456'

DATABASE = 'demo'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8'

db = SQLAlchemy(app)

with app.app_context():
    with db.engine.connect() as conn:
        rs = conn.execute(text('select 1'))
        print(rs.fetchone())