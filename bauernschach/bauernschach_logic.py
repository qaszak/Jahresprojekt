from random import choice
from tkinter import *


class Bauernschach():
    def __init__(self, can, B_W, B_S, rand):
        # the highlighted square
        self.highlighted_square = []
        # the last played move player
        self.played_move_player = [[-1, -1], [-1, -1]]
        # the last played move KI
        self.played_move_KI = [[-1, -1], [-1, -1]]
        # last selected pawn
        self.last_selected = [-1, -1]

        # last possible moves
        self.last_possible_moves = [[-1, -1]]

        self.can = can
        self.BOARD_WIDTH = B_W
        self.BOARD_SIZE = B_S
        self.rand = rand
        self.spiel = "bauernschach"
        self.last_selected = [0, 0]
        size = 6
        # player and ki pawns position [column , line]
        # player_pawns_position = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5]]
        # KI_pawns_position = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]
        self.player_pawns_position = []
        self.KI_pawns_position = []
        for i in range(size):
            self.player_pawns_position.append([i, size - 1])
            self.KI_pawns_position.append([i, 0])
        print("bauernschach init")

    # draw the pawns on the KI side
    def fill_board_KI_pawns(self):
        ite, self.x3, self.x4, self.y3, self.y4 = 0, self.BOARD_WIDTH / 5, self.BOARD_WIDTH / 5, self.BOARD_WIDTH - \
                                                  self.BOARD_WIDTH / 5, self.BOARD_WIDTH - self.BOARD_WIDTH / 5
        while ite < self.BOARD_SIZE:
            self.can.create_rectangle(self.x3 + self.rand, self.x4 + self.rand, self.y3 + self.rand,
                                      self.y4 + self.rand, fill='yellow')
            ite, self.x3, self.x4, self.y3, self.y4 = ite + 1, self.x3 + self.BOARD_WIDTH, self.x4, self.y3 + \
                                                      self.BOARD_WIDTH, self.y4

        # draw the pawns on the player side

    def fill_board_player_pawns(self):
        ite, self.x3, self.x4, self.y3, self.y4 = 0, self.BOARD_WIDTH / 5 + self.rand, self.BOARD_WIDTH * (
                self.BOARD_SIZE - 1) + self.BOARD_WIDTH / 5 + self.rand, \
                                                  self.BOARD_WIDTH - self.BOARD_WIDTH / 5 + self.rand, \
                                                  self.BOARD_WIDTH * self.BOARD_SIZE - self.BOARD_WIDTH / 5 + self.rand

        while ite < self.BOARD_SIZE:
            obj1 = self.can.create_oval(self.x3, self.x4, self.y3, self.y4, fill='red')
            if self.spiel == "bauernschach":
                self.can.tag_bind(obj1, "<Button-1>", self.show_possible_moves_bauernschach)
            ite, self.x3, self.x4, self.y3, self.y4 = ite + 1, self.x3 + self.BOARD_WIDTH, self.x4, self.y3 + \
                                                      self.BOARD_WIDTH, self.y4

        # fill the board with both KI and player pawns

    def fill_board_pawns(self):
        print("draw pawns")
        self.fill_board_player_pawns()
        self.fill_board_KI_pawns()

    ###################################################################################################################
    ################################ FILL THE BOARD WITH PAWNS ########################################################
    ###################################################################################################################
    # draw the pawns on the KI side
    def fill_board_KI_pawns(self):
        ite, self.x3, self.x4, self.y3, self.y4 = 0, self.BOARD_WIDTH / 5, self.BOARD_WIDTH / 5, self.BOARD_WIDTH - \
                                                  self.BOARD_WIDTH / 5, self.BOARD_WIDTH - self.BOARD_WIDTH / 5
        while ite < self.BOARD_SIZE:
            self.can.create_rectangle(self.x3 + self.rand, self.x4 + self.rand, self.y3 + self.rand,
                                      self.y4 + self.rand, fill='yellow')
            ite, self.x3, self.x4, self.y3, self.y4 = ite + 1, self.x3 + self.BOARD_WIDTH, self.x4, self.y3 + \
                                                      self.BOARD_WIDTH, self.y4

    # draw the pawns on the player side

    def fill_board_player_pawns(self):
        ite, self.x3, self.x4, self.y3, self.y4 = 0, self.BOARD_WIDTH / 5 + self.rand, self.BOARD_WIDTH * (
                self.BOARD_SIZE - 1) + self.BOARD_WIDTH / 5 + self.rand, \
                                                  self.BOARD_WIDTH - self.BOARD_WIDTH / 5 + self.rand, \
                                                  self.BOARD_WIDTH * self.BOARD_SIZE - self.BOARD_WIDTH / 5 + self.rand

        while ite < self.BOARD_SIZE:
            obj1 = self.can.create_oval(self.x3, self.x4, self.y3, self.y4, fill='red')
            if self.spiel == "bauernschach":
                self.can.tag_bind(obj1, "<Button-1>", self.show_possible_moves_bauernschach)
            ite, self.x3, self.x4, self.y3, self.y4 = ite + 1, self.x3 + self.BOARD_WIDTH, self.x4, self.y3 + \
                                                      self.BOARD_WIDTH, self.y4

    # fill the board with both KI and player pawns

    def fill_board_pawns(self):
        self.fill_board_player_pawns()
        self.fill_board_KI_pawns()

    ###################################################################################################################
    ################################   BAUERNSCHACH METHODES   ########################################################
    ###################################################################################################################
    def removeSelectionFromOthers_bauernschach(self):
        i = self.last_selected[0]
        j = self.last_selected[1]
        if i == -1: return
        # print("col line in remove  ", i, j)
        self.can.create_rectangle(i * self.BOARD_WIDTH + self.rand, j * self.BOARD_WIDTH + self.rand,
                                  (i + 1) * self.BOARD_WIDTH + self.rand,
                                  (j + 1) * self.BOARD_WIDTH + self.rand, outline='black')
        col = self.last_possible_moves[0][0]
        line = self.last_possible_moves[0][1]

        if (col + line) % 2 == 0:
            c = 'grey'
        else:
            c = 'white'
        # print("last possible moves col   line  ", col, line, c)
        # print("highlited squares in removeSelection : ", self.highlighted_square)
        for square in self.highlighted_square:
            # print("square : ", square)
            col = square[0]
            line = square[1]
            if (col + line) % 2 == 0:
                c = 'grey'
            else:
                c = 'white'
            self.can.create_rectangle(col * self.BOARD_WIDTH + self.rand, line * self.BOARD_WIDTH + self.rand,
                                      (col + 1) * self.BOARD_WIDTH + self.rand,
                                      (line + 1) * self.BOARD_WIDTH + self.rand, fill=c)
            if self.is_position_free_from_KI_pawns(col, line) == FALSE:
                t = self.BOARD_WIDTH / 5
                self.can.create_rectangle(col * self.BOARD_WIDTH + t + self.rand,
                                          line * self.BOARD_WIDTH + t + self.rand,
                                          (col + 1) * self.BOARD_WIDTH - t + self.rand,
                                          (line + 1) * self.BOARD_WIDTH - t + self.rand, fill='yellow')
        self.highlighted_square = []

    def selected_square_bauernschach(self, x, y):
        col = int(x / self.BOARD_WIDTH)
        line = int(y / self.BOARD_WIDTH)
        self.removeSelectionFromOthers_bauernschach()
        self.last_selected = [col, line]
        print("selected square ", self.last_selected)
        self.highlighted_square = []

        # print("selected square ", col, line)
        self.can.create_rectangle(col * self.BOARD_WIDTH + self.rand, line * self.BOARD_WIDTH + self.rand,
                                  (col + 1) * self.BOARD_WIDTH + self.rand,
                                  (line + 1) * self.BOARD_WIDTH + self.rand,
                                  outline='red')
        self.possible_moves_bauernschach()
        print("highlited square in selected square ", self.highlighted_square)
        print("**********************************************************************")

    def possible_moves_bauernschach(self):
        col = self.last_selected[0]
        line = self.last_selected[1] - 1
        self.last_possible_moves = [[col, line]]

        # print("last possible moves 1 col   line  ", col, line)
        if self.is_position_free_from_KI_pawns(col, line) == TRUE:
            print(col, line, " is a possible move")
            self.highlighted_square.append([col, line])
            obj1 = self.can.create_rectangle(col * self.BOARD_WIDTH + self.rand, line * self.BOARD_WIDTH + self.rand,
                                             (col + 1) * self.BOARD_WIDTH + self.rand,
                                             (line + 1) * self.BOARD_WIDTH + self.rand, fill='#99ff99',
                                             stipple='gray50')
            self.can.tag_bind(obj1, "<Button-1>", self.play_move_bauernschach)

        if self.is_position_free_from_KI_pawns(col + 1, line) == FALSE:
            print(col + 1, line, " is a possible move")
            self.highlighted_square.append([col + 1, line])
            obj3 = self.can.create_rectangle((col + 1) * self.BOARD_WIDTH + self.rand,
                                             line * self.BOARD_WIDTH + self.rand,
                                             (col + 1 + 1) * self.BOARD_WIDTH + self.rand,
                                             (line + 1) * self.BOARD_WIDTH + self.rand, fill='#99ff99',
                                             stipple='gray50')
            self.can.tag_bind(obj3, "<Button-1>", self.play_move_bauernschach)

        if self.is_position_free_from_KI_pawns(col - 1, line) == FALSE:
            print(col - 1, line, " is a possible move")
            self.highlighted_square.append([col - 1, line])
            obj4 = self.can.create_rectangle((col - 1) * self.BOARD_WIDTH + self.rand,
                                             line * self.BOARD_WIDTH + self.rand,
                                             col * self.BOARD_WIDTH + self.rand,
                                             (line + 1) * self.BOARD_WIDTH + self.rand, fill='#99ff99',
                                             stipple='gray50')
            self.can.tag_bind(obj4, "<Button-1>", self.play_move_bauernschach)
        print("highlighted square in possible moves: ", self.highlighted_square)

    def show_possible_moves_bauernschach(self, event):
        self.selected_square_bauernschach(event.x, event.y)

    def back(self):
        print("back")
        Bauernschach.back_player(self)
        Bauernschach.back_KI(self)

    def back_KI(self):
        old_x = self.played_move_KI[0][0]
        old_y = self.played_move_KI[0][1]
        # draw oval in the old position
        t = self.BOARD_WIDTH / 5
        self.can.create_rectangle(old_x * self.BOARD_WIDTH + t + self.rand,
                                  old_y * self.BOARD_WIDTH + t + self.rand,
                                  (old_x + 1) * self.BOARD_WIDTH - t + self.rand,
                                  (old_y + 1) * self.BOARD_WIDTH - t + self.rand, fill='yellow')

        new_x = self.played_move_KI[1][0]
        new_y = self.played_move_KI[1][1]
        if (new_x + new_y) % 2 == 0:
            c_rectangle = 'grey'
        else:
            c_rectangle = 'white'
        # remove the old oval from the last position
        self.can.create_rectangle(new_x * self.BOARD_WIDTH + self.rand, new_y * self.BOARD_WIDTH + self.rand,
                                  (new_x + 1) * self.BOARD_WIDTH + self.rand,
                                  (new_y + 1) * self.BOARD_WIDTH + self.rand, fill=c_rectangle)
        self.KI_pawns_position[old_x] = [old_x, old_y]

    def back_player(self):
        old_x = self.played_move_player[0][0]
        old_y = self.played_move_player[0][1]
        # draw oval in the old position
        t = self.BOARD_WIDTH / 5
        obj1 = self.can.create_oval(old_x * self.BOARD_WIDTH + t + self.rand, old_y * self.BOARD_WIDTH + t + self.rand,
                                    (old_x + 1) * self.BOARD_WIDTH - t + self.rand,
                                    (old_y + 1) * self.BOARD_WIDTH - t + self.rand, fill='red')
        self.can.tag_bind(obj1, "<Button-1>", self.show_possible_moves_bauernschach)

        new_x = self.played_move_player[1][0]
        new_y = self.played_move_player[1][1]
        if (new_x + new_y) % 2 == 0:
            c_rectangle = 'grey'
        else:
            c_rectangle = 'white'
        # remove the old oval from the last position
        self.can.create_rectangle(new_x * self.BOARD_WIDTH + self.rand, new_y * self.BOARD_WIDTH + self.rand,
                                  (new_x + 1) * self.BOARD_WIDTH + self.rand,
                                  (new_y + 1) * self.BOARD_WIDTH + self.rand, fill=c_rectangle)
        self.player_pawns_position[old_x] = [old_x, old_y]

    def play_move_bauernschach(self, event):
        col = int(event.x / self.BOARD_WIDTH)
        line = int(event.y / self.BOARD_WIDTH)
        # store the played move  [0] ::> old position [1] ::> new position
        self.played_move_player = [[self.last_selected[0], self.last_selected[1]], [col, line]]
        if (self.last_selected[0] + self.last_selected[1]) % 2 == 0:
            c_rectangle = 'grey'
        else:
            c_rectangle = 'white'

        if (col + line) % 2 == 0:
            c_oval = 'grey'
        else:
            c_oval = 'white'

        # print("the played move col   line  ", col, line)
        print("played move player : ", self.played_move_player)
        # remove the highlight from the possible square
        self.removeSelectionFromOthers_bauernschach()
        self.can.create_rectangle(col * self.BOARD_WIDTH + self.rand,
                                  line * self.BOARD_WIDTH + self.rand,
                                  (col + 1) * self.BOARD_WIDTH + self.rand,
                                  (line + 1) * self.BOARD_WIDTH + self.rand, fill=c_oval)
        # print("rectangle position color: ", col, line, c_oval)

        # draw a new oval in the played square
        t = self.BOARD_WIDTH / 5
        obj1 = self.can.create_oval(col * self.BOARD_WIDTH + t + self.rand, line * self.BOARD_WIDTH + t + self.rand,
                                    (col + 1) * self.BOARD_WIDTH - t + self.rand,
                                    (line + 1) * self.BOARD_WIDTH - t + self.rand, fill='red')
        self.can.tag_bind(obj1, "<Button-1>", self.show_possible_moves_bauernschach)
        # remove the old oval from the last position

        self.can.create_rectangle(self.played_move_player[0][0] * self.BOARD_WIDTH + self.rand,
                                  self.played_move_player[0][1] * self.BOARD_WIDTH + self.rand,
                                  (self.played_move_player[0][0] + 1) * self.BOARD_WIDTH + self.rand,
                                  (self.played_move_player[0][1] + 1) * self.BOARD_WIDTH + self.rand, fill=c_rectangle)
        # print("rectangle position color: ", self.played_move_player[0][0], self.played_move_player[0][1], c_rectangle)
        # print("KI PAWNS POSITION ", self.KI_pawns_position)
        if self.is_position_free_from_KI_pawns(col, line) == FALSE:
            self.KI_pawns_position[col] = ([col, -10])

        # initialise the last selected Square
        self.last_selected = [-1, -1]
        line = line + 1
        # modify the player's pawn position

        self.player_pawns_position[self.played_move_player[0][0]] = [self.played_move_player[1][0],
                                                                     self.played_move_player[1][1]]
        # TODO modify the position of KI_pawns and player_pawns
        count = 0
        for x in self.player_pawns_position:
            if x == self.played_move_player[0]:
                self.player_pawns_position[count] = self.played_move_player[0]
                break
            count = count + 1

        print("PLAYER PAWNS POSITION ", self.player_pawns_position)
        if line - 1 == 0:
            print("**************** YOU WIN ***********************")
        else:
            self.best_move_bauernschach()

    def is_position_free_from_KI_pawns(self, a, b):
        for x in self.KI_pawns_position:
            if x[0] == a and x[1] == b:
                return FALSE
        return TRUE

    def is_position_free_from_player_pawns(self, a, b):
        for x in self.player_pawns_position:
            if x[0] == a and x[1] == b:
                return FALSE
        return TRUE

    def is_position_free_bauernschach(self, a, b):
        all_pawns = self.KI_pawns_position + self.player_pawns_position
        for x in all_pawns:
            if x[0] == a and x[1] == b:
                return FALSE
        return TRUE

    ##  return all possible moves [0]and[1] are the current position [2]and[3] the possible move
    def KI_possible_move_bauernschach(self):
        KI_possible_moves_bauernschach = []
        for pos in self.KI_pawns_position:
            col = pos[0]
            line = pos[1]
            if line != -10:
                if self.is_position_free_bauernschach(col, line + 1) == TRUE:
                    KI_possible_moves_bauernschach.append([col, line, col, line + 1])
                ### TODO check the position of the player's pawns
                if self.is_position_free_from_player_pawns(col + 1, line + 1) == FALSE:
                    print("KI position is free : ", col + 1, line + 1)
                    KI_possible_moves_bauernschach.append([col, line, col + 1, line + 1])
                if self.is_position_free_from_player_pawns(col - 1, line + 1) == FALSE:
                    print("KI position is free : ", col - 1, line + 1)
                    KI_possible_moves_bauernschach.append([col, line, col - 1, line + 1])
        # print("possible move are : ", KI_possible_moves_bauernschach)
        return KI_possible_moves_bauernschach

    def KI_move_bauernschach(self, difficulty):
        self.KI_pawns_position
        self.best_move_bauernschach(difficulty)

    def best_move_bauernschach(self):
        # TODO MiniMax
        KI_possible_moves_bauernschach = self.KI_possible_move_bauernschach()
        if KI_possible_moves_bauernschach != []:
            move = choice(KI_possible_moves_bauernschach)
            cur_x = move[0]
            cur_y = move[1]
            next_x = move[2]
            next_y = move[3]
            self.play_KI_move_bauernschach(cur_x, cur_y, next_x, next_y)
        else:
            print("********************* YOU LOSE (no possible moves) *************************")

    def play_KI_move_bauernschach(self, cur_x, cur_y, next_x, next_y):
        col = next_x
        line = next_y
        self.last_selected[0] = cur_x
        self.last_selected[1] = cur_y
        # store the played move  [0] ::> old position [1] ::> new position
        # self.played_move = [[self.last_selected[0], self.last_selected[1]], [col, line]]
        self.played_move_KI = [[self.last_selected[0], self.last_selected[1]], [col, line]]
        print("KI last played move : ", self.played_move_KI)
        if (self.last_selected[0] + self.last_selected[1]) % 2 == 0:
            c_rectangle = 'grey'
        else:
            c_rectangle = 'white'

        if (col + line) % 2 == 0:
            c_oval = 'grey'
        else:
            c_oval = 'white'

        # print("the played move col   line  ", col, line)
        # remove the highlight from the possible square
        self.can.create_rectangle(col * self.BOARD_WIDTH + self.rand, line * self.BOARD_WIDTH + self.rand,
                                  (col + 1) * self.BOARD_WIDTH + self.rand,
                                  (line + 1) * self.BOARD_WIDTH + self.rand, fill=c_oval)
        # print("draw rectangle [new position] col line: ", col, line, c_oval)
        # draw a new oval in the played square
        t = self.BOARD_WIDTH / 5
        self.can.create_rectangle(col * self.BOARD_WIDTH + t + self.rand, line * self.BOARD_WIDTH + t + self.rand,
                                  (col + 1) * self.BOARD_WIDTH - t + self.rand,
                                  (line + 1) * self.BOARD_WIDTH - t + self.rand, fill='yellow')

        # remove the old oval from the last position

        self.can.create_rectangle(cur_x * self.BOARD_WIDTH + self.rand, cur_y * self.BOARD_WIDTH + self.rand,
                                  (cur_x + 1) * self.BOARD_WIDTH + self.rand,
                                  (cur_y + 1) * self.BOARD_WIDTH + self.rand, fill=c_rectangle)
        # print("draw rectangle col line: ", col, line, c_rectangle)

        # initialise the last selected Square
        self.last_selected = [-1, -1]
        ########################################################
        if self.played_move_KI[0][0] != self.played_move_KI[1][0]:
            count = 0
            print("player_pawns_position: ", self.player_pawns_position,
                  " played move KI ",
                  self.played_move_KI[1])
            for position in self.player_pawns_position:
                if position == self.played_move_KI[1]:
                    print("player_pawns_position: ", self.player_pawns_position,
                          " played move KI ",
                          self.played_move_KI[1], "position ", position, "count ", count)
                    self.player_pawns_position[count] = [-10, -10]
                count = count + 1
        count = 0
        print("player_pawns_position: ", self.player_pawns_position)
        # modify the player's pawn position
        for position in self.player_pawns_position:
            if position == self.played_move_KI[0]:
                print("position in KI_pawns_position: ", position, self.KI_pawns_position, " played move KI ",
                      self.played_move_KI)
                self.KI_pawns_position[count] = self.played_move_KI[1]
                count = count + 1

        ########################################################
        if cur_x != col:
            print(cur_x, col, line)
            self.KI_pawns_position[cur_x] = [col, line]
        else:
            # modify the player's pawn position
            self.KI_pawns_position[col] = [col, line]
        ##############################################################

        print("KI PAWNS POSITION", self.KI_pawns_position)
        if self.KI_possible_move_bauernschach() == []:
            print("draw!!!!")
        elif self.played_move_KI[1][1] == self.BOARD_SIZE - 1:
            print("******************* YOU LOSE *****************************")
        print("*************************************************************")
