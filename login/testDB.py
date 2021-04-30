import sqlite3
from tkinter import TRUE, FALSE


class DB:
    def __init__(self):
        self.con = sqlite3.connect("db/test.db")
        self.cursor = self.con.cursor()
        sql = "CREATE TABLE IF NOT EXISTS USER(" \
              "ID_USER INTEGER PRIMARY KEY AUTOINCREMENT," \
              " LOGIN VARCHAR(25)," \
              "PASSWORD VARCHAR(25) )"
        self.cursor.execute(sql)

    def add_user(self, login, password):
        #sql = "INSERT INTO USER (LOGIN,PASSWORD) VALUES", " (", login, ",", password, ")"
        self.cursor.execute("INSERT INTO USER (LOGIN,PASSWORD) VALUES(?,?)", login, password)
        self.con.commit()

    def all_users(self):
        sql = "SELECT * FROM USER"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

    def is_exist(self, login, pswd):
        rows = self.all_users()
        for row in rows:
            if row[1] == login and row[2] == pswd:
                return TRUE
        return FALSE

    def close_con(self):
        self.con.close()
