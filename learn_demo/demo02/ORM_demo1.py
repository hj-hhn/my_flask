#!/usr/bin python3
# -*- encoding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import learn_demo.demo02.mysql_config_utils as my_conf
from sqlalchemy import text

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{my_conf.USERNAME}:{my_conf.PASSWORD}@{my_conf.HOSTNAME}:{my_conf.PORT}/{my_conf.DATABASE}?charset=utf8'

print(app.config['SQLALCHEMY_DATABASE_URI'])

db = SQLAlchemy(app)

# with app.app_context():
#     with db.engine.connect() as conn:
#         rs = conn.execute(text("show databases"))
#         print(rs.fetchone())


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    username = db.Column(db.String(100), nullable=False)

    password = db.Column(db.String(100))

# with app.app_context():
#     db.create_all()


@app.route("/user/add")
def add_user():
    user = User(username='张三', password='111111')
    db.session.add(user)

    db.session.commit()

    return '用户添加成功'


@app.route("/user/query")
def query_user():
    # 1.get查找：根据主键查找
    user = User.query.get(1)
    print(f'{user.id} : {user.username} -- {user.password}')

    # 2.filter_by 查找
    users2 = User.query.filter_by(username='张三') # Query
    for user1 in users2:
        print(f'{user1.id} : {user1.username} -- {user1.password}')

    return '用户查找成功'


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=2000)