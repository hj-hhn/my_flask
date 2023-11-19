#!/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author : jie.hou
# @File : qa.py
# @Time : 2023/11/19 22:31

from flask import Blueprint


# /
bp = Blueprint('qa' , __name__ , url_prefix='/')


@bp.route('login')
def index():
    pass