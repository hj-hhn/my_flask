# -*- coding: utf-8 -*-
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world!!!'

# 1. 修改host = 0。0。0。0  就能其他电脑访问
# --host=0.0.0.0

# 2.修改端口号

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=2000)