import sqlite3

DB_PATH ='D:/DJ_diplom/diplom/shop.db'

def check_user(name):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute('select "name" from "customer" where "name"=?;', [name])
    res = cur.fetchall()
    cur.close()
    con.close()
    return res

def add_user(name,email,password):
     '''Данная функция заносит информацию о пользователе в таблицу "customer"'''
     con = sqlite3.connect(DB_PATH)
     cur = con.cursor()
     cur.execute('insert into "customer"("name","email","password") values(?,?,?);',[name,email,password])
     con.commit()
     cur.close()
     con.close()
     return 0

def check_user_password(name,password):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute('select "name","password" from "customer" where "name"=? and "password=?";', [name,password])
    res = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return res


