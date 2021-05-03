from copy import deepcopy
from random import choice
from tkinter import *
from tkinter import messagebox


class Bauernschach():
    def __init__(self, can, B_W, B_S, rand, difficulty):
        self.difficulty = difficulty
        self.EASY = "easy"
        self.NORMAL = "normal"
        self.HARD = "hard"
        self.game_state = None
        self.GAME_OVER = "GAME OVER"
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
        self.difficulty = self.NORMAL
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

        for square in self.highlighted_square:
            # print("square : ", square)
            col = square[0]
            line = square[1]
            if (col + line) % 2 == 0:
                c = 'grey'
            else:
                c = 'white'
            self.draw_rectangle(col, line, c, 0)
            if self.is_position_free_from_KI_pawns(col, line) == FALSE:
                t = self.BOARD_WIDTH / 5
                self.draw_rectangle(col, line, 'yellow', t)
        self.highlighted_square = []

    def selected_square_bauernschach(self, x, y):
        col = int(x / self.BOARD_WIDTH)
        line = int(y / self.BOARD_WIDTH)
        self.removeSelectionFromOthers_bauernschach()
        self.last_selected = [col, line]
        print("selected square ", self.last_selected)
        self.highlighted_square = []

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
        self.draw_rectangle(old_x, old_y, 'yellow', t)

        new_x = self.played_move_KI[1][0]
        new_y = self.played_move_KI[1][1]
        if (new_x + new_y) % 2 == 0:
            c_rectangle = 'grey'
        else:
            c_rectangle = 'white'
        # remove the old oval from the last position
        self.draw_rectangle(new_x, new_y, c_rectangle, 0)
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
        self.draw_rectangle(new_x, new_y, c_rectangle, 0)
        self.player_pawns_position[old_x] = [old_x, old_y]

    def play_move_bauernschach(self, event):
        if self.game_state != self.GAME_OVER:
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

            print("played move player : ", self.played_move_player)
            # remove the highlight from the possible square
            self.removeSelectionFromOthers_bauernschach()
            self.draw_rectangle(col, line, c_oval, 0)
            # draw a new oval in the played square
            t = self.BOARD_WIDTH / 5
            obj1 = self.can.create_oval(col * self.BOARD_WIDTH + t + self.rand, line * self.BOARD_WIDTH + t + self.rand,
                                        (col + 1) * self.BOARD_WIDTH - t + self.rand,
                                        (line + 1) * self.BOARD_WIDTH - t + self.rand, fill='red')
            self.can.tag_bind(obj1, "<Button-1>", self.show_possible_moves_bauernschach)
            # remove the old oval from the last position

            self.draw_rectangle(self.played_move_player[0][0], self.played_move_player[0][1], c_rectangle, 0)
            for x in self.KI_pawns_position:
                if x == self.played_move_player[1]:
                    self.KI_pawns_position.remove(self.played_move_player[1])
            print("new KI position ", self.KI_pawns_position)
            # initialise the last selected Square
            self.last_selected = [-1, -1]
            line = line + 1
            # modify the player's pawn position
            self.player_pawns_position.remove(self.played_move_player[0])
            self.player_pawns_position.append(self.played_move_player[1])
            count = 0
            for x in self.player_pawns_position:
                if x == self.played_move_player[0]:
                    self.player_pawns_position[count] = self.played_move_player[0]
                    break
                count = count + 1
            if line - 1 == 0:
                print("**************** YOU WIN ***********************")
                self.game_state = self.GAME_OVER
                messagebox.showinfo("Basic Example", "YOU WIN")
            else:
                self.best_move_bauernschach()

    def is_position_free_from_KI_pawns(self, a, b):
        for x in self.KI_pawns_position:
            if x[0] == a and x[1] == b:
                return FALSE
        return TRUE

    def is_position_free_from_player_pawns(self, a, b, player_pawns_position):
        for x in player_pawns_position:
            if x[0] == a and x[1] == b:
                return FALSE
        return TRUE

    def is_position_free_bauernschach(self, a, b, KI_pawns_position, player_pawns_position):
        all_pawns = KI_pawns_position + player_pawns_position
        for z in all_pawns:
            if z[0] == a and z[1] == b:
                return FALSE
        return TRUE

    def player_possible_move_bauernschach(self, KI_pawns_position, player_pawns_position):
        player_possible_moves_bauernschach = []
        for pos in player_pawns_position:
            col = pos[0]
            line = pos[1]
            if self.is_position_free_bauernschach(col, line - 1, KI_pawns_position, player_pawns_position) == TRUE:
                player_possible_moves_bauernschach.append([col, line, col, line - 1])
            if self.is_position_free_from_KI_pawns(col + 1, line - 1) == FALSE:
                player_possible_moves_bauernschach.append([col, line, col + 1, line - 1])
            if self.is_position_free_from_KI_pawns(col - 1, line - 1) == FALSE:
                player_possible_moves_bauernschach.append([col, line, col - 1, line - 1])
        return player_possible_moves_bauernschach

    def play_possible_move_player_bauernschach(self, KI_pawns_position, player_pawns_position):
        all_moves = []
        for x in self.player_possible_move_bauernschach(KI_pawns_position, player_pawns_position):
            cur_position = [x[0], x[1]]
            new_move = [x[2], x[3]]
            player_position = deepcopy(player_pawns_position)
            player_position.remove(cur_position)
            player_position.append(new_move)
            all_moves.append(player_position)
        return all_moves

    ##  return all possible moves [0]and[1] are the current position [2]and[3] the possible move
    def KI_possible_move_bauernschach(self, KI_pawns_position, player_pawns_position):
        KI_possible_moves_bauernschach = []
        for pos in KI_pawns_position:
            col = pos[0]
            line = pos[1]
            if self.is_position_free_bauernschach(col, line + 1, KI_pawns_position, player_pawns_position) == TRUE:
                KI_possible_moves_bauernschach.append([col, line, col, line + 1])
            if self.is_position_free_from_player_pawns(col + 1, line + 1, player_pawns_position) == FALSE:
                KI_possible_moves_bauernschach.append([col, line, col + 1, line + 1])
            if self.is_position_free_from_player_pawns(col - 1, line + 1, player_pawns_position) == FALSE:
                KI_possible_moves_bauernschach.append([col, line, col - 1, line + 1])
        # print("KI POSSIBLE MOVES ", KI_possible_moves_bauernschach)
        return KI_possible_moves_bauernschach

    def play_possible_move_KI_bauernschach(self, KI_pawns_position, player_pawns_position):
        all_moves = []

        for x in self.KI_possible_move_bauernschach(KI_pawns_position, player_pawns_position):
            KI_position = deepcopy(KI_pawns_position)
            cur_position = [x[0], x[1]]
            new_move = [x[2], x[3]]
            KI_position.remove(cur_position)
            KI_position.append(new_move)
            # print("KI pawns 1 ", KI_position)
            all_moves.append(KI_position)
        return all_moves

    def KI_move_bauernschach(self, difficulty):
        self.best_move_bauernschach(difficulty)

    def evaluate(self, KI_pawns_position, player_pawns_position):
        return len(KI_pawns_position) - len(player_pawns_position)

    def minimax(self, KI_positions, player_positions, depth, state, max_player):
        if depth == 0 or state == self.GAME_OVER:
            return self.evaluate(KI_positions, player_positions), KI_positions, player_positions, state
        if max_player:
            max_eval = -1000
            best_move = None
            ## all possible moves [0]and[1] are the current position [2]and[3] the possible move
            for move_KI in self.play_possible_move_KI_bauernschach(KI_positions, player_positions):
                eval = self.minimax(move_KI, player_positions, depth - 1, state,
                                    FALSE)[0]  ## how do i know the state here???
                max_eval = max(max_eval, eval)
                if max_eval == eval:
                    best_move = move_KI
            return max_eval, best_move
        else:
            min_eval = 1000
            best_move = None
            ## all possible moves [0]and[1] are the current position [2]and[3] the possible move
            for move_player in self.play_possible_move_player_bauernschach(KI_positions, player_positions):
                eval = self.minimax(KI_positions, move_player, depth - 1, state,
                                    TRUE)[0]  ## how do i know the state here???
                min_eval = min(min_eval, eval)
                if min_eval == eval:
                    best_move = move_player
            return min_eval, best_move

    def best_move_bauernschach(self):
        # TODO MiniMax
        KI_positions = deepcopy(self.KI_pawns_position)
        player_positions = deepcopy(self.player_pawns_position)
        state = deepcopy(self.game_state)
        if self.difficulty == self.HARD:
            depth = 6
        elif self.difficulty == self.NORMAL:
            depth = 4
        elif self.difficulty == self.EASY:
            depth = 2
        max_player = TRUE

        KI_possible_moves_bauernschach = self.minimax(KI_positions, player_positions, depth, state, max_player)[1]
        copy_ki_pawns_position = deepcopy(self.KI_pawns_position)
        if KI_possible_moves_bauernschach != []:
            for x in self.KI_pawns_position:
                for y in KI_possible_moves_bauernschach:
                    if x == y:
                        KI_possible_moves_bauernschach.remove(y)
                        copy_ki_pawns_position.remove(x)
                        break

            next_x = KI_possible_moves_bauernschach[0][0]
            next_y = KI_possible_moves_bauernschach[0][1]
            cur_x = copy_ki_pawns_position[0][0]
            cur_y = copy_ki_pawns_position[0][1]
            # move = choice(KI_possible_moves_bauernschach)
            self.play_KI_move_bauernschach(cur_x, cur_y, next_x, next_y)
        else:
            print("********************* YOU LOSE (no possible moves) *************************")
            self.game_state = self.GAME_OVER
            messagebox.showinfo("Basic Example", "YOU LOSE")

    def draw_rectangle(self, col, line, color, t):
        self.can.create_rectangle(col * self.BOARD_WIDTH + t + self.rand, line * self.BOARD_WIDTH + t + self.rand,
                                  (col + 1) * self.BOARD_WIDTH - t + self.rand,
                                  (line + 1) * self.BOARD_WIDTH - t + self.rand, fill=color)

    def play_KI_move_bauernschach(self, cur_x, cur_y, next_x, next_y):
        col = next_x
        line = next_y
        self.last_selected[0] = cur_x
        self.last_selected[1] = cur_y
        self.played_move_KI = [[self.last_selected[0], self.last_selected[1]], [col, line]]
        # print("KI last played move : ", self.played_move_KI)
        if (self.last_selected[0] + self.last_selected[1]) % 2 == 0:
            c_rectangle = 'grey'
        else:
            c_rectangle = 'white'

        if (col + line) % 2 == 0:
            c_oval = 'grey'
        else:
            c_oval = 'white'

        self.draw_rectangle(col, line, c_oval, 0)
        # draw a new oval in the played square
        t = self.BOARD_WIDTH / 5
        self.draw_rectangle(col, line, 'yellow', t)
        # remove the old oval from the last position
        self.draw_rectangle(cur_x, cur_y, c_rectangle, self.rand)

        # initialise the last selected Square
        self.last_selected = [-1, -1]
        ########################################################
        if self.played_move_KI[0][0] != self.played_move_KI[1][0]:
            count = 0
            # print("player_pawns_position: ", self.player_pawns_position,
            #      " played move KI ",
            #      self.played_move_KI[1])
            for x in self.player_pawns_position:
                if x == self.played_move_KI[1]:
                    self.player_pawns_position.remove(self.played_move_KI[1])
        count = 0
        # print("player_pawns_position: ", self.player_pawns_position)
        # modify the KI's pawn position
        self.KI_pawns_position.remove(self.played_move_KI[0])
        self.KI_pawns_position.append(self.played_move_KI[1])

        print("KI PAWNS POSITION", self.KI_pawns_position)
        if len(self.KI_pawns_position) == 0:
            print("draw!!!!")
            self.game_state = self.GAME_OVER
            messagebox.showinfo("Basic Example", "YOU WIN")
        if self.KI_possible_move_bauernschach(self.KI_pawns_position, self.player_pawns_position) == []:
            print("draw!!!!")
            self.game_state = self.GAME_OVER
            messagebox.showinfo("Basic Example", "DRAW")
        elif self.played_move_KI[1][1] == self.BOARD_SIZE - 1:
            print("******************* YOU LOSE *****************************")
            self.game_state = self.GAME_OVER
            messagebox.showinfo("Basic Example", "YOU LOSE")
        print("*************************************************************")
