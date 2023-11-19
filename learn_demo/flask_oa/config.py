#!/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author : jie.hou
# @File : config.py
# @Time : 2023/11/17 18:13
'''
创建数据库 SQL ：
create database flask_oa default character set utf8mb4;
'''


# 数据库配置信息
HOSTNAME = 'localhost'
PORT = '3307'
USERNAME = 'root'
PASSWORD = 'root'
DATABASE = 'flask_oa'
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8'

SQLALCHEMY_DATABASE_URI = DB_URI
