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
    cur.execute('select "name","password" from "customer" where "name"=? and "password"=?;', [name,password])
    res = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return res

def view_products():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute('select "id","namepr","price","size","img" from "product";')
    res = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return res

def sizeof_product():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute('select count("id") from "product";')
    res = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return res[0][0]

def insert_bsk(name,idpr,namepr,size,price):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute('insert into "bsk" values(?,?,?,?,?);',(name,idpr,namepr,size,price))
    res = cur.fetchall()
    con.commit()
    cur.close()
    con.close()

def update_products(idpr,size):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute('update "product" set size = size - ? where id = ?', ( size,idpr))
    res = cur.fetchall()
    con.commit()
    cur.close()
    con.close()

def bsk_name_data(name):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute('select * from "bsk" where "name" =?;',(name))
    res = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return res

def sizeof_bsk_name(name):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute('select count("id") from "bsk" where "name" =?;', (name))
    res = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return res[0][0]
def itog_price(name):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute('select sum("size" * "price") from "bsk" where "name" =?;', (name))
    res = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return res[0][0]
def ord_registred(name,idpr,namepr,size,price):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute('insert into "ord"("name","idpr","namepr","size","price") values(?,?,?,?,?);', (name,idpr,namepr,size,price))
    res = cur.fetchall()
    con.commit()
    cur.close()
    con.close()

def clear_bsk(name):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute('delete from "bsk" where "name" = ?;', [name])
    res = cur.fetchall()
    con.commit()
    cur.close()
    con.close()

def add_comment(name,text):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute('insert into "comments" values(?,?);',(name,text))
    res = cur.fetchall()
    con.commit()
    cur.close()
    con.close()

def all_comments():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute('select * from "comments";')
    res = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return res

#print(sizeof_product())
#insert_bsk("Ivan",1,"teststylo1",2,2.45)
#print(itog_price('q'))