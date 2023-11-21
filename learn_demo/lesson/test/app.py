# -*- coding: utf-8 -*-
from flask import Flask,request,render_template,flash,redirect,url_for
from forms import RegisterForm

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world!!!'


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        # request.form 是html模版提交上来的表单数据
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data

            # 该操作相当于保存数据库
            print(email,'---',username,'---',password)
            return '注册成功！'
        else:
            for errors in form.errors.values():
                for error in errors:
                    flash(error)
            return redirect(url_for('register'))


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=2000)