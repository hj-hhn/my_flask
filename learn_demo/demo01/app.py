# -*- coding: utf-8 -*-
from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)



# 在app.config 中设置好连接数据库的信息
# 然后使用SQLAlchemy(app) 创建一个db对象
# db自动获取app中的config
db = SQLAlchemy(app)

class User:
    def __init__(self,username,email):
        self.username = username
        self.email = email


@app.route('/')
def hello_world():
    return 'hello world!!!'

# 1. 修改host = 0.0.0.0  就能其他电脑访问
# --host=0.0.0.0

# 2.修改端口号

# 传参数的路径   将参数固定到path中
@app.route('/blog/<string:blog_id>')
def blog_detail(blog_id):
    return '访问的是 - > %s' % blog_id

# 查询字符串的方式传参
# /book/list  默认返回第一页
# /book/list?page=2 获取第二页
@app.route('/book/list') # 需要引用全局对象
def book_list():
    # request.args 类字段的
    page = request.args.get('page',default=1,type=int)
    return f'获取的是第{page}的book_list'

@app.route('/filter')
def filter_demo():
    user = User(username='houjiexxxxxx',email='111@163.com')
    return render_template('filter.html',user=user)


@app.route('/control')
def control_statement():
    age = 18
    books_list = [
        {'name':'aaa','author':'aaa1'},
        {'name':'bbb','author':'bbb1'},
        {'name':'ccc','author':'ccc1'}
    ]
    return render_template('control.html',age=age,books=books_list)

@app.route('/child')
def clild1():
    return render_template('child1.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=2000)