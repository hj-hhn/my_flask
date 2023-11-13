# -*- coding: utf-8 -*-
import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3307,
    user='root',
    password='root',
    database='mysql'
)


cursor= conn.cursor()


cursor.execute("select host,user from user")

print(cursor.fetchall())


cursor.close()