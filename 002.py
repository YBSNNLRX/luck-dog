# -*- coding: utf-8 -*-

import mysql.connector

def write_to_mysql(filename):
    conn = mysql.connector.connect(user='root', password='root', database='test')
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS user")
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    f = open(filename, 'r').readlines()
    for line, num in zip(f, range(1, len(f)+1)):
        line = line[:-1]                     #去除\n符号
        cursor.execute('insert into user (id, name) values (%s, %s)', [str(num), line])
        conn.commit()
    cursor.close()
    return 0

def search_mysql():
    b = input('Search Active code（1-200）：')
    conn = mysql.connector.connect(user='root', password='986535', database='test')
    cursor = conn.cursor()
    cursor.execute('select * from user where id = %s', (b,))
    values = cursor.fetchall()
    print(values)
    cursor.close()
    conn.close()
    return 0

if __name__ == '__main__':
    filename = 'active_code.txt'
    write_to_mysql(filename)
search_mysql()