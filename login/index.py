from tkinter import *

###
from bauernschach.play_bauernschach import Play_bauernschach
from dbManagement.database import DB


class Window:
    def __init__(self, content_type):
        ### WINDOW PARAMS
        self.WINDOW_TITLE = "Jahresprojekt 2021 - FA11 - Gruppe 3"
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.WINDOW_COLOR = "#96bfd6"
        ### GAME PARAMS
        self.login = None
        self.game = None
        self.PAWN_CHESS = "bauernschach"
        self.DAME = "dame"
        self.TIC_TAC_TAE = "tic-tac-toe"
        self.difficulty = None
        self.EASY = "easy"
        self.NORMAL = "normal"
        self.HARD = "hard"
        ##### ERROR MESSAGES ###
        self.USERNAME_ALREADY_EXIST = "USERNAME ALREADY EXIST"
        self.USERNAME_PASSWORD_WRONG = "USERNAME OR PASSWORD WRONG"
        self.create_window(content_type)

    def leaderboard(self):
        self.create_blank_window()

    def play_easy(self):
        self.difficulty = self.EASY
        self.play()

    def play_normal(self):
        self.difficulty = self.NORMAL
        self.play()

    def play_hard(self):
        self.difficulty = self.HARD
        self.play()

    def play(self):
        if self.game == self.PAWN_CHESS:
            self.play_pawnchess(self.difficulty)

    def play_pawnchess(self, difficulty):
        db = DB()
        db.add_player_stats(self.login, self.game, self.difficulty)
        Play_bauernschach(self.window, difficulty)

    def register_btn_clicked(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        db = DB()
        if db.is_exist_register(username):
            self.lbl_result2.config(text=self.USERNAME_ALREADY_EXIST, fg="red")
            # self.create_window_content(self.window, "game_select")
            # self.create_window_content(self.window,"bauernschach")
        else:
            # self.lbl_result2.config(text="Username or password is wrong", fg="red")
            db.add_user(username, password)
            db.add_best_list(username)
        db.close_con()

    def login_btn_clicked(self):
        # print("Clicked")
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.login = username
        db = DB()
        if db.is_exist(username, password):
            # self.lbl_result2.config(text="Welcome", fg="green")
            self.create_window_content(self.window, "game_select")
            # self.create_window_content(self.window,"bauernschach")
        else:
            self.lbl_result2.config(text=self.USERNAME_PASSWORD_WRONG, fg="red")

    def create_window_content(self, window, content_type):
        if content_type == "login":
            print(content_type)
            print()
            ### Login Screen Content
            ### Params
            background_color_primary = "#96bfd6"
            background_color_secondary = "#3f6d8c"

            register_button_color = "#8aba00"
            register_button_active_color = "#648700"
            register_button_font_color = "#ffffff"
            register_button_font_active_color = "#dddddd"
            register_button_width = 16
            register_button_height = 0
            register_button_text = "Register"

            login_button_color = "#8aba00"
            login_button_active_color = "#648700"
            login_button_font_color = "#ffffff"
            login_button_font_active_color = "#dddddd"
            login_button_width = 16
            login_button_height = 0
            login_button_text = "Login"

            username_entry_width = 24

            password_entry_width = 24

            self.WINDOW_WIDTH = 800
            self.WINDOW_HEIGHT = 600

            background_square_primary_color = "#96bfd6"
            background_square_secondary_color = "#87b0c7"
            background_square_size = 16

            ### Widgets
            window_background = Canvas(self.window, width=800, height=600, bg=background_color_primary)

            # Checkerboard Pattern for Background
            for i in range(0, self.WINDOW_WIDTH, background_square_size):
                for j in range(0, self.WINDOW_HEIGHT, background_square_size):
                    if (i / background_square_size) % 2 == 0:
                        if (j / background_square_size) % 2 == 0:
                            window_background.create_rectangle(i, j, i + background_square_size,
                                                               j + background_square_size,
                                                               fill=background_square_primary_color,
                                                               outline=background_square_primary_color)
                        else:
                            window_background.create_rectangle(i, j, i + background_square_size,
                                                               j + background_square_size,
                                                               fill=background_square_secondary_color,
                                                               outline=background_square_secondary_color)
                    else:
                        if (j / background_square_size) % 2 == 0:
                            window_background.create_rectangle(i, j, i + background_square_size,
                                                               j + background_square_size,
                                                               fill=background_square_secondary_color,
                                                               outline=background_square_secondary_color)
                        else:
                            window_background.create_rectangle(i, j, i + background_square_size,
                                                               j + background_square_size,
                                                               fill=background_square_primary_color,
                                                               outline=background_square_primary_color)

            window_background.create_rectangle(150, 175, 640, 500, fill=background_color_secondary)
            self.username_entry = Entry(window, width=username_entry_width, font='sans 18')
            self.password_entry = Entry(window, show="•", width=password_entry_width, font='sans 18')
            login_button = Button(window, bg=login_button_color, fg=login_button_font_color, width=login_button_width,
                                  height=login_button_height, text=login_button_text, font='sans 16 bold',
                                  activebackground=login_button_active_color,
                                  activeforeground=login_button_font_active_color,
                                  command=self.login_btn_clicked)
            register_button = Button(window, bg=register_button_color, fg=register_button_font_color,
                                     width=register_button_width, height=register_button_height,
                                     text=register_button_text, font='sans 16 bold',
                                     activebackground=register_button_active_color,
                                     activeforeground=register_button_font_active_color,
                                     command=self.register_btn_clicked)

            username_label = Label(text="Nutzername", bg=background_color_secondary, fg="#ffffff", font='sans 16')
            password_label = Label(text="Passwort", bg=background_color_secondary, fg="#ffffff", font='sans 16')
            welcome_label = Label(text="Willkommen", bg=background_color_secondary, fg="#ffffff", font='sans 32 bold')
            credit_label = Label(text="© Jahresprojekt 2021 - FA11 - Gruppe 3",
                                 bg=background_color_primary, fg="#ffffff", font='sans 16')

            self.lbl_result2 = Label(text="", bg=background_color_secondary, fg="#ffffff", font='sans 18 bold')
            self.lbl_result2.place(x=175, y=450)

            credit_label.place(x=205, y=550)
            window_background.place(x=0, y=0)
            welcome_label.place(x=265, y=235)
            username_label.place(x=175, y=300)
            self.username_entry.place(x=300, y=300)
            password_label.place(x=175, y=350)
            self.password_entry.place(x=300, y=350)
            login_button.place(x=175, y=400)
            register_button.place(x=400, y=400)

            ###

        if content_type == "game_select":
            print(content_type)

            ### Game Select Screen Content
            ### Params
            background_color_primary = "#96bfd6"
            background_color_secondary = "#3f6d8c"

            pawnchess_button_color = "#8aba00"
            pawnchess_button_active_color = "#648700"
            pawnchess_button_font_color = "#ffffff"
            pawnchess_button_font_active_color = "#dddddd"
            pawnchess_button_width = 14
            pawnchess_button_height = 0
            pawnchess_button_text = "Bauernschach"

            checkers_button_color = "#8aba00"
            checkers_button_active_color = "#648700"
            checkers_button_font_color = "#ffffff"
            checkers_button_font_active_color = "#dddddd"
            checkers_button_width = 14
            checkers_button_height = 0
            checkers_button_text = "Dame"

            tictactoe_button_color = "#8aba00"
            tictactoe_button_active_color = "#648700"
            tictactoe_button_font_color = "#ffffff"
            tictactoe_button_font_active_color = "#dddddd"
            tictactoe_button_width = 14
            tictactoe_button_height = 0
            tictactoe_button_text = "Tic-Tac-Toe"

            back_button_color = "#858585"
            back_button_active_color = "#5e5e5e"
            back_button_font_color = "#ffffff"
            back_button_font_active_color = "#dddddd"
            back_button_width = 3
            back_button_height = 0
            back_button_text = "⬅"

            self.WINDOW_WIDTH = 800
            self.WINDOW_HEIGHT = 600

            background_square_primary_color = "#96bfd6"
            background_square_secondary_color = "#87b0c7"
            background_square_size = 16

            ### Widgets
            window_background = Canvas(self.window, width=800, height=600, bg=background_color_primary)

            # Checkerboard Pattern for Background
            for i in range(0, self.WINDOW_WIDTH, background_square_size):
                for j in range(0, self.WINDOW_HEIGHT, background_square_size):
                    if (i / background_square_size) % 2 == 0:
                        if (j / background_square_size) % 2 == 0:
                            window_background.create_rectangle(i, j, i + background_square_size,
                                                               j + background_square_size,
                                                               fill=background_square_primary_color,
                                                               outline=background_square_primary_color)
                        else:
                            window_background.create_rectangle(i, j, i + background_square_size,
                                                               j + background_square_size,
                                                               fill=background_square_secondary_color,
                                                               outline=background_square_secondary_color)
                    else:
                        if (j / background_square_size) % 2 == 0:
                            window_background.create_rectangle(i, j, i + background_square_size,
                                                               j + background_square_size,
                                                               fill=background_square_secondary_color,
                                                               outline=background_square_secondary_color)
                        else:
                            window_background.create_rectangle(i, j, i + background_square_size,
                                                               j + background_square_size,
                                                               fill=background_square_primary_color,
                                                               outline=background_square_primary_color)

            window_background.create_rectangle(75, 100, 715, 500, fill=background_color_secondary)

            window_background.create_rectangle(100, 200, 290, 390, fill="#2d4d63")
            window_background.create_oval(150 + 16 * 1, 220 + 16 * 0, 150 + 16 * 5, 220 + 16 * 4, fill="#ffffff")
            window_background.create_rectangle(150 + 16 * 1, 220 + 16 * 3, 150 + 16 * 5, 220 + 16 * 4, fill="#ffffff")
            window_background.create_polygon(150 + 16 * 2, 220 + 16 * 4, 150 + 16 * 4, 220 + 16 * 4, 150 + 16 * 5,
                                             220 + 16 * 8,
                                             150 + 16 * 1, 220 + 16 * 8, fill="#ffffff")
            window_background.create_rectangle(150 + 16 * 0, 220 + 16 * 8, 150 + 16 * 6, 220 + 16 * 9, fill="#ffffff")

            window_background.create_rectangle(300, 200, 490, 390, fill="#2d4d63")
            window_background.create_oval(340 + 16 * 0, 240 + 16 * 0, 340 + 16 * 7, 240 + 16 * 7, fill="#ffffff")
            window_background.create_oval(340 + 16 * 1, 240 + 16 * 1, 340 + 16 * 6, 240 + 16 * 6,
                                          fill=background_color_secondary)
            window_background.create_oval(340 + 16 * 1.5, 240 + 16 * 1.5, 340 + 16 * 5.5, 240 + 16 * 5.5,
                                          fill="#ffffff")

            window_background.create_rectangle(500, 200, 690, 390, fill="#2d4d63")
            window_background.create_rectangle(530 + 16 * 2, 230 + 16 * 0, 530 + 16 * 3, 230 + 16 * 8, fill="#ffffff")
            window_background.create_rectangle(530 + 16 * 5, 230 + 16 * 0, 530 + 16 * 6, 230 + 16 * 8, fill="#ffffff")
            window_background.create_rectangle(530 + 16 * 0, 230 + 16 * 2, 530 + 16 * 8, 230 + 16 * 3, fill="#ffffff")
            window_background.create_rectangle(530 + 16 * 0, 230 + 16 * 5, 530 + 16 * 8, 230 + 16 * 6, fill="#ffffff")

            pawnchess_button = Button(self.window, bg=pawnchess_button_color, fg=pawnchess_button_font_color,
                                      width=pawnchess_button_width, height=pawnchess_button_height,
                                      text=pawnchess_button_text, font='sans 16 bold',
                                      activebackground=pawnchess_button_active_color,
                                      activeforeground=pawnchess_button_font_active_color,
                                      command=self.select_difficulty_pawnchess)
            checkers_button = Button(window, bg=checkers_button_color, fg=checkers_button_font_color,
                                     width=checkers_button_width, height=checkers_button_height,
                                     text=checkers_button_text, font='sans 16 bold',
                                     activebackground=checkers_button_active_color,
                                     activeforeground=checkers_button_font_active_color,
                                     command=self.select_difficulty_dame)
            tictactoe_button = Button(self.window, bg=tictactoe_button_color, fg=tictactoe_button_font_color,
                                      width=tictactoe_button_width, height=tictactoe_button_height,
                                      text=tictactoe_button_text, font='sans 16 bold',
                                      activebackground=tictactoe_button_active_color,
                                      activeforeground=tictactoe_button_font_active_color,
                                      command=self.select_difficulty_tictactoe)
            select_label = Label(text="Wähle ein Spiel", bg=background_color_secondary, fg="#ffffff",
                                 font='sans 24 bold')
            credit_label = Label(text="© Jahresprojekt 2021 - FA11 - Gruppe 3", bg=background_color_primary,
                                 fg="#ffffff", font='sans 16')
            back_button = Button(window, bg=back_button_color, fg=back_button_font_color, width=back_button_width,
                                 height=back_button_height, text=back_button_text, font='sans 16 bold',
                                 activebackground=back_button_active_color,
                                 activeforeground=back_button_font_active_color,
                                 command=lambda: self.change_content_type(window, "login"))
            credit_label.place(x=205, y=550)
            window_background.place(x=0, y=0)
            select_label.place(x=270, y=130)
            pawnchess_button.place(x=100, y=400)
            checkers_button.place(x=300, y=400)
            tictactoe_button.place(x=500, y=400)
            back_button.place(x=643, y=450)
            ###

        if content_type == "game_settings":
            print(content_type)

            ### Game Settings Screen Content
            ### Params

            background_color_primary = "#96bfd6"
            background_color_secondary = "#3f6d8c"

            easy_button_color = "#8aba00"
            easy_button_active_color = "#648700"
            easy_button_font_color = "#ffffff"
            easy_button_font_active_color = "#dddddd"
            easy_button_width = 14
            easy_button_height = 0
            easy_button_text = "Einfach"

            normal_button_color = "#8aba00"
            normal_button_active_color = "#648700"
            normal_button_font_color = "#ffffff"
            normal_button_font_active_color = "#dddddd"
            normal_button_width = 14
            normal_button_height = 0
            normal_button_text = "Normal"

            hard_button_color = "#8aba00"
            hard_button_active_color = "#648700"
            hard_button_font_color = "#ffffff"
            hard_button_font_active_color = "#dddddd"
            hard_button_width = 14
            hard_button_height = 0
            hard_button_text = "Schwer"

            back_button_color = "#858585"
            back_button_active_color = "#5e5e5e"
            back_button_font_color = "#ffffff"
            back_button_font_active_color = "#dddddd"
            back_button_width = 3
            back_button_height = 0
            back_button_text = "⬅"

            leaderboard_button_color = "#e6ac00"
            leaderboard_button_active_color = "#648700"
            leaderboard_button_font_color = "#ffffff"
            leaderboard_button_font_active_color = "#dddddd"
            leaderboard_button_width = 18
            leaderboard_button_height = 0
            leaderboard_button_text = "Bestenliste"

            self.WINDOW_WIDTH = 800
            self.WINDOW_HEIGHT = 600

            background_square_primary_color = "#96bfd6"
            background_square_secondary_color = "#87b0c7"
            background_square_size = 16

            ### Widgets
            window_background = Canvas(self.window, width=800, height=600, bg=background_color_primary)

            # Checkerboard Pattern for Background
            for i in range(0, self.WINDOW_WIDTH, background_square_size):
                for j in range(0, self.WINDOW_HEIGHT, background_square_size):
                    if (i / background_square_size) % 2 == 0:
                        if (j / background_square_size) % 2 == 0:
                            window_background.create_rectangle(i, j, i + background_square_size,
                                                               j + background_square_size,
                                                               fill=background_square_primary_color,
                                                               outline=background_square_primary_color)
                        else:
                            window_background.create_rectangle(i, j, i + background_square_size,
                                                               j + background_square_size,
                                                               fill=background_square_secondary_color,
                                                               outline=background_square_secondary_color)
                    else:
                        if (j / background_square_size) % 2 == 0:
                            window_background.create_rectangle(i, j, i + background_square_size,
                                                               j + background_square_size,
                                                               fill=background_square_secondary_color,
                                                               outline=background_square_secondary_color)
                        else:
                            window_background.create_rectangle(i, j, i + background_square_size,
                                                               j + background_square_size,
                                                               fill=background_square_primary_color,
                                                               outline=background_square_primary_color)

            window_background.create_rectangle(75, 85, 715, 515, fill=background_color_secondary)

            window_background.create_rectangle(100, 200, 290, 390, fill="#2d4d63")
            window_background.create_oval(130 + 16 * 0, 230 + 16 * 0, 130 + 16 * 8, 230 + 16 * 8, fill="#ffffff")
            window_background.create_text(193, 284, text="😃", fill="#2d4d63", font='sans 120 bold')

            window_background.create_rectangle(300, 200, 490, 390, fill="#2d4d63")
            window_background.create_oval(330 + 16 * 0, 230 + 16 * 0, 330 + 16 * 8, 230 + 16 * 8, fill="#ffffff")
            window_background.create_text(393, 284, text="🙂", fill="#2d4d63", font='sans 120 bold')

            window_background.create_rectangle(500, 200, 690, 390, fill="#2d4d63")
            window_background.create_oval(530 + 16 * 0, 230 + 16 * 0, 530 + 16 * 8, 230 + 16 * 8, fill="#ffffff")
            window_background.create_text(593, 284, text="😡", fill="#2d4d63", font='sans 120 bold')

            easy_button = Button(window, bg=easy_button_color, fg=easy_button_font_color, width=easy_button_width,
                                 height=easy_button_height, text=easy_button_text, font='sans 16 bold',
                                 activebackground=easy_button_active_color,
                                 activeforeground=easy_button_font_active_color,
                                 command=self.play_easy)
            normal_button = Button(window, bg=normal_button_color, fg=normal_button_font_color,
                                   width=normal_button_width, height=normal_button_height,
                                   text=normal_button_text, font='sans 16 bold',
                                   activebackground=normal_button_active_color,
                                   activeforeground=normal_button_font_active_color,
                                   command=self.play_normal)
            hard_button = Button(window, bg=hard_button_color, fg=hard_button_font_color,
                                 width=hard_button_width, height=hard_button_height,
                                 text=hard_button_text, font='sans 16 bold',
                                 activebackground=hard_button_active_color,
                                 activeforeground=hard_button_font_active_color,
                                 command=self.play_hard)
            leaderboard_button = Button(window, bg=leaderboard_button_color, fg=leaderboard_button_font_color,
                                        width=leaderboard_button_width, height=leaderboard_button_height,
                                        text=leaderboard_button_text, font='sans 16 bold',
                                        activebackground=leaderboard_button_active_color,
                                        activeforeground=leaderboard_button_font_active_color,
                                        command=self.leaderboard)
            select_label = Label(text="Wähle einen Schwierigkeitsgrad", bg=background_color_secondary,
                                 fg="#ffffff", font='sans 24 bold')
            credit_label = Label(text="© Jahresprojekt 2021 - FA11 - Gruppe 3",
                                 bg=background_color_primary, fg="#ffffff", font='sans 16')
            back_button = Button(window, bg=back_button_color, fg=back_button_font_color, width=back_button_width,
                                 height=back_button_height, text=back_button_text, font='sans 16 bold',
                                 activebackground=back_button_active_color,
                                 activeforeground=back_button_font_active_color,
                                 command=lambda: self.change_content_type(window, "game_select"))

            credit_label.place(x=205, y=550)
            window_background.place(x=0, y=0)
            select_label.place(x=140, y=125)
            easy_button.place(x=100, y=400)
            normal_button.place(x=300, y=400)
            hard_button.place(x=500, y=400)
            leaderboard_button.place(x=275, y=450)
            back_button.place(x=643, y=450)
            ###

        if content_type == "game":
            print(content_type)

        if content_type == "leaderboard":
            print(content_type)

    def create_window(self, content_type):
        self.window = Tk()
        self.window.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.window.title(self.WINDOW_TITLE)
        self.window.configure(background=self.WINDOW_COLOR)

        self.create_window_content(self.window, content_type)

        self.window.mainloop()

    def create_blank_window(self):
        window = Tk()
        window.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        window.title(self.WINDOW_TITLE)
        window.configure(background=self.WINDOW_COLOR)

        l = Label(window, text="LEADER BOARD")
        l.config(font=("Courier", 14))

        b = Text(window, height=2, width=10)
        b.grid(row=1, column=1)
        b.insert(END, "-----")
        text = "NAME"
        b = Text(window, height=2, width=10)
        b.grid(row=1, column=2)
        b.insert(END, text)
        text = "SCORE"
        b = Text(window, height=2, width=10)
        b.grid(row=1, column=3)
        b.insert(END, text)
        i = 1
        db = DB()
        rows = []
        if self.game == self.PAWN_CHESS:
            rows = db.get_pawn_chess_best_list()
        if self.game == self.DAME:
            rows = db.get_dame_best_list()
        if self.game == self.TIC_TAC_TAE:
            rows = db.get_tic_tac_toe_best_list()
        print(rows)
        for row in rows:
            b = Text(window, height=5, width=10)
            b.grid(row=i + 1, column=1)
            b.insert(END, "player")
            text = row[1]
            b = Text(window, height=5, width=10)
            b.grid(row=i + 1, column=2)
            b.insert(END, text)
            text = row[7]
            b = Text(window, height=5, width=10)
            b.grid(row=i + 1, column=3)
            b.insert(END, text)
            i = i + 1
        db.close_con()
        window.mainloop()

    def change_content_type(self, window, content_type):
        self.delete_widgets(self.window)
        self.create_window_content(self.window, content_type)

    def delete_widgets(self, container):
        for widget in container.winfo_children():
            widget.destroy()

    def select_difficulty_pawnchess(self):
        self.select_difficulty(self.PAWN_CHESS)

    def select_difficulty_tictactoe(self):
        self.select_difficulty(self.TIC_TAC_TAE)

    def select_difficulty_dame(self):
        self.select_difficulty(self.DAME)

    def select_difficulty(self, game):
        self.game = game
        self.change_content_type(self.window, "game_settings")


Window("login")
