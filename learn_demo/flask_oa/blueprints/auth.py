#!/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author : jie.hou
# @File : auth.py
# @Time : 2023/11/19 22:31

from flask import Blueprint


# /auth
bp = Blueprint('auth' , __name__ , url_prefix='/auth')


@bp.route('login')
def login():
    pass