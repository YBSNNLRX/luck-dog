# -*- coding: utf-8 -*-
import mysql.connector
import string, random
import pymysql

conn =pymysql.connect(
        host = 'localhost',
        user = 'root',
        port = 3306,
        passwd = 'root',
        db = 'test',
        charset='utf8'
        )
cmd =conn.cursor()

field = string.ascii_letters + string.digits

def getRandom(): 
    return "".join(random.sample(field,4))

def concatenate(group): 
    return "-".join([getRandom() for i in range(group)])

for i in range(200):
    value = concatenate(4)
    cmd.execute("insert into userss (id, code) values (%s, %s)", [i, value])
    
cmd.close()
conn.close()