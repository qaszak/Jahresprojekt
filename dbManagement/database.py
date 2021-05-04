import sqlite3
from tkinter import TRUE, FALSE
import dbManagement


class DB:
    def __init__(self):
        self.con = sqlite3.connect("../login/JAHRESPROJEKT.db")
        self.cursor = self.con.cursor()
        sql = "CREATE TABLE IF NOT EXISTS USER(" \
              "ID_USER INTEGER PRIMARY KEY AUTOINCREMENT," \
              "LOGIN VARCHAR(25) NOT NULL," \
              "PASSWORD VARCHAR(25) NOT NULL)"
        self.cursor.execute(sql)

        sql = "CREATE TABLE IF NOT EXISTS PLAYER_STATS(" \
              "ID_PLAYER_STATS INTEGER PRIMARY KEY AUTOINCREMENT," \
              "LOGIN VARCHAR(25) NOT NULL," \
              "GAME VARCHAR(12) NOT NULL," \
              "DIFFICULTY VARCHAR(7) NOT NULL," \
              "WIN INTEGER DEFAULT 0," \
              "DRAW INTEGER DEFAULT 0," \
              "LOSE INTEGER DEFAULT 0," \
              "CANCELED INTEGER DEFAULT 0," \
              "USER_ID INTEGER NOT NULL," \
              "CONSTRAINT FK_USER_PLAYER_STATS FOREIGN KEY (USER_ID)" \
              "REFERENCES USER(ID_USER)" \
              "ON DELETE CASCADE)"
        self.cursor.execute(sql)
        sql = "CREATE TABLE IF NOT EXISTS PAWN_CHESS_BEST_LIST(" \
              "ID_PAWN_CHESS_BEST_LIST INTEGER PRIMARY KEY AUTOINCREMENT," \
              "LOGIN VARCHAR(25) NOT NULL," \
              "GAME_PLAYED INTEGER DEFAULT 0," \
              "WIN INTEGER INTEGER DEFAULT 0," \
              "DRAW INTEGER INTEGER DEFAULT 0," \
              "LOSE INTEGER INTEGER DEFAULT 0," \
              "CANCELED INTEGER INTEGER DEFAULT 0," \
              "SCORE INTEGER DEFAULT 1000," \
              "USER_ID INTEGER NOT NULL," \
              "CONSTRAINT FK_USER_BEST_LIST FOREIGN KEY (USER_ID)" \
              "REFERENCES USER(ID_USER)" \
              "ON DELETE CASCADE)"
        self.cursor.execute(sql)

        sql = "CREATE TABLE IF NOT EXISTS DAME_BEST_LIST(" \
              "ID_DAME_BEST_LIST INTEGER PRIMARY KEY AUTOINCREMENT," \
              "LOGIN VARCHAR(25) NOT NULL," \
              "GAME_PLAYED INTEGER DEFAULT 0," \
              "WIN INTEGER INTEGER DEFAULT 0," \
              "DRAW INTEGER INTEGER DEFAULT 0," \
              "LOSE INTEGER INTEGER DEFAULT 0," \
              "CANCELED INTEGER INTEGER DEFAULT 0," \
              "SCORE INTEGER DEFAULT 1000," \
              "USER_ID INTEGER NOT NULL," \
              "CONSTRAINT FK_USER_BEST_LIST FOREIGN KEY (USER_ID)" \
              "REFERENCES USER(ID_USER)" \
              "ON DELETE CASCADE)"
        self.cursor.execute(sql)
        sql = "CREATE TABLE IF NOT EXISTS TIC_TAC_TOE_BEST_LIST(" \
              "ID_TIC_TAC_TOE_BEST_LIST INTEGER PRIMARY KEY AUTOINCREMENT," \
              "LOGIN VARCHAR(25) NOT NULL," \
              "GAME_PLAYED INTEGER DEFAULT 0," \
              "WIN INTEGER INTEGER DEFAULT 0," \
              "DRAW INTEGER INTEGER DEFAULT 0," \
              "LOSE INTEGER INTEGER DEFAULT 0," \
              "CANCELED INTEGER INTEGER DEFAULT 0," \
              "SCORE INTEGER DEFAULT 1000," \
              "USER_ID INTEGER NOT NULL," \
              "CONSTRAINT FK_USER_BEST_LIST FOREIGN KEY (USER_ID)" \
              "REFERENCES USER(ID_USER)" \
              "ON DELETE CASCADE)"
        self.cursor.execute(sql)

    def get_player_stats(self, login):
        self.cursor.execute("SELECT * FROM PLAYER_STATS WHERE LOGIN=?", (login,))
        rows = self.cursor.fetchall()
        return rows

    # remember before closing the game to modify the state of the game (win,draw,lose or canceled)
    def add_player_stats(self, login, game, difficulty):
        id = self.find_user(login)
        if id == 0:
            raise Exception("USER NOT FOUND !!")

        self.cursor.execute("INSERT INTO PLAYER_STATS (LOGIN,GAME,DIFFICULTY,USER_ID,CANCELED) VALUES(?,?,?,?,1)",
                            (login, game, difficulty, id))
        self.con.commit()

        return self.cursor.lastrowid

    def alter_player_stats(self, id, state):
        if state == "win":
            self.cursor.execute("UPDATE PLAYER_STATS SET WIN = 1, CANCELED = 0 WHERE USER_ID=? ",
                                (id,))
        elif state == "lose":
            self.cursor.execute("UPDATE PLAYER_STATS SET LOSE = 1, CANCELED = 0 WHERE USER_ID=? ",
                                (id,))
        self.con.commit()

    # TODO player stats win quote and number of games

    def get_player_stats(self, login):
        id = self.find_user(login)
        if id == 0:
            raise Exception("USER NOT FOUND !!")
        self.cursor.execute("SELECT * FROM PLAYER_STATS WHERE USER_ID=?", (id,))
        rows = self.cursor.fetchall()
        return rows

    def get_dame_best_list(self):
        sql = "SELECT * FROM DAME_BEST_LIST"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

    def get_pawn_chess_best_list(self):
        sql = "SELECT * FROM PAWN_CHESS_BEST_LIST"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

    def get_tic_tac_toe_best_list(self):
        sql = "SELECT * FROM TIC_TAC_TOE_BEST_LIST"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

    def get_best_list(self, game):
        if game == "pawnchess":
            return self.get_pawn_chess_best_list()
        if game == "dame2":
            return self.get_dame_best_list()
        if game == "tic-tac-toe":
            return self.get_tic_tac_toe_best_list()

    def add_best_list(self, login):
        self.add_pawn_chess_best_list(login)
        self.add_dame_best_list(login)
        self.add_tic_tac_toe_best_list(login)

    def add_dame_best_list(self, login):
        id = self.find_user(login)
        if id == 0:
            raise Exception("USER NOT FOUND !!")

        self.cursor.execute("INSERT INTO DAME_BEST_LIST (LOGIN ,USER_ID) VALUES(?,?)",
                            (login, id))
        self.con.commit()

    def add_pawn_chess_best_list(self, login):
        print("asdasdasda  ", login)
        id = self.find_user(login)
        if id == 0:
            raise Exception("USER NOT FOUND !!")
        print("asdasdasda  ", login, id)
        self.cursor.execute("INSERT INTO PAWN_CHESS_BEST_LIST(LOGIN ,USER_ID) VALUES(?,?)", (login, id))
        self.con.commit()

    def add_tic_tac_toe_best_list(self, login):
        id = self.find_user(login)
        if id == 0:
            raise Exception("USER NOT FOUND !!")

        self.cursor.execute("INSERT INTO TIC_TAC_TOE_BEST_LIST (LOGIN ,USER_ID) VALUES(?,?)",
                            (login, id))
        self.con.commit()

    def add_user(self, login, password):
        self.cursor.execute("INSERT INTO USER (LOGIN,PASSWORD) VALUES(?,?)", (login, password))
        self.con.commit()

    def set_score(self, login, game, score):
        if game == "pawnchess":
            return self.set_pawn_chess_score(login, score)
        if game == "dame":
            return self.set_dame_score(login, score)
        if game == "tic-tac-toe":
            return self.set_tic_tac_toe_score(login, score)

    def set_tic_tac_toe_score(self, login, score):
        self.cursor.execute("SELECT * FROM TIC_TAC_TOE_BEST_LIST WHERE LOGIN=?", (login,))
        row = self.cursor.fetchone()
        self.cursor.execute("UPDATE TIC_TAC_TOE_BEST_LIST SET SCORE = ? WHERE LOGIN  = ?", (row[7] + score, login))
        self.con.commit()

    def set_dame_score(self, login, score):
        self.cursor.execute("SELECT * FROM DAME_BEST_LIST WHERE LOGIN=?", (login,))
        row = self.cursor.fetchone()
        self.cursor.execute("UPDATE DAME_BEST_LIST SET SCORE = ? WHERE LOGIN  = ?", (row[7] + score, login))
        self.con.commit()

    def set_pawn_chess_score(self, login, score):
        self.cursor.execute("SELECT * FROM PAWN_CHESS_BEST_LIST WHERE LOGIN=?", (login,))
        row = self.cursor.fetchone()
        print(row[7])
        print(score)
        x = int(row[7]) + score
        self.cursor.execute("UPDATE PAWN_CHESS_BEST_LIST SET SCORE = ? WHERE LOGIN  = ?", (x, login))
        self.con.commit()

    # return 0 where not found , id where found
    def find_user(self, login):
        self.cursor.execute("SELECT * FROM USER WHERE LOGIN=?", (login,))
        row = self.cursor.fetchone()
        if not row:
            return 0
        else:
            return row[0]

    def all_player_stats(self):
        sql = "SELECT * FROM PLAYER_STATS"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

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

    def is_exist_register(self, login):
        rows = self.all_users()
        for row in rows:
            if row[1] == login:
                return TRUE
        return FALSE

    def close_con(self):
        self.con.close()


db = DB()
# db.add_user("zak", "123")
# rows = db.all_users()
# for row in rows:
#    print(row)

# db.add_player_stats("zak", "pawnchess", "hard")

# rows = db.all_player_stats()
# for row in rows:
#   print(row)
#db.add_best_list("zak")
#db.set_score("", "pawnchess", 2)
# id = db.add_player_stats("zak", "pawnchess", "easy")
#rows = db.get_pawn_chess_best_list()
#for row in rows:
#  print(row)

# db.alter_player_stats(id, 1)

# rows = db.get_player_stats("zak")
# for row in rows:
#    print(row)
# print("best_list_dame ", db.get_best_list("dame2"))
# print("best_list_pawn ", db.get_best_list("pawnchess"))
# print("best_list_tic ", db.get_best_list("tic-tac-toe"))
# print(db.find_user("zak"))
