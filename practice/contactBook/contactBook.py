#!/usr/bin/python3
# coding=utf-8

import sqlite3


class contackBook:
    # def __init__(self, name, phone, *address):
    def __init__(self):
        info = self.info()
        self.name = info[0]
        self.phone = info[1]
        self.address = info[2]
        self.dbfile = 'cbdb.db'

    def info(self):
        name = input("请输入用户名: ")
        phone = str(input("请输入用户号码: "))
        address = str(input("请输入用户地址: "))
        if not name:
            print("用户名不能为空")
            exit(11)
        if not phone:
            print("用户号码为空, 设置为默认号码: 00000000000")
            phone = "00000000000"
        if not address:
            address = None
        return [name, phone, address]

    def cbdb(self):
        connect = sqlite3.connect(self.dbfile, timeout=3)
        return connect

    def close(self):
        conn = self.cbdb()
        conn.commit()
        conn.close()

    def create(self):
        sql = "CREATE TABLE IF NOT EXISTS contact (id INTEGER PRIMARY KEY AUTOINCREMENT,name VARCHAR (20) NOT NULL , phone VARCHAR (16), address VARCHAR (100));"
        self.cbdb().execute(sql)

    def insert(self):
        sql = "INSERT INTO contact (name, phone, address) VALUES ('%s', '%s', '%s');" % (
        self.name, self.phone, self.address)
        conn = self.cbdb()
        conn.execute(sql)
        conn.commit()
        self.findall()

    def delete(self):
        sql = "DELETE FROM contact WHERE name = '%s';" % self.name
        conn = self.cbdb()
        conn.execute(sql)
        conn.commit()
        self.findall()

    def update(self):
        sql = "UPDATE contact SET phone='%s', address='%s' WHERE name='%s';" % (self.phone, self.address, self.name)
        conn = self.cbdb()
        conn.execute(sql)
        conn.commit()
        self.findall()
        self.close()

    def select(self):
        sql = "SELECT id, name, phone, address FROM contact WHERE name = '%s';" % self.name
        cursor = self.cbdb().execute(sql)
        for res in cursor:
            print(res)
        self.close()

    def findall(self):
        sql = "SELECT * FROM contact;"
        cursor = self.cbdb().execute(sql)
        for res in cursor:
            print(res)
        self.close()


cbook = contackBook()
cbook.create()
# cbook.insert()
#cbook.update()
# cbook.findall()
#cbook.delete()
#cbook.select()
#cbook.close()
