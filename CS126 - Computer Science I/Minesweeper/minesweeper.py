#!/usr/bin/env python

"""

An implementation of the game Minesweeper.

"""

import random


class Space(object):

    def __init__(self, state):
        self._state = str(state)
        self._displayed = '   '

    def flag(self):
        self._displayed = '[F]'

    def clear(self):
        self._displayed = self._state

    def unflag(self):
        self._displayed = '   '

    def display_cell(self):
        return str(self._displayed)

    def state(self):
        return str(self._state)


class Board(object):

    def __init__(self, dimension, difficulty):
        self._lost = False
        self._dimension = dimension
        self._spaces = []
        self._mine_count = 0

        if difficulty == 'hard':
            mines = ['   ', '   ', '   ', '*', '*', '*', '*', '*', '*', '*']
        elif difficulty == 'medium':
            mines = ['   ', '   ', '   ', '   ', '   ', '*', '*', '*', '*',
                     '*']
        elif difficulty == 'easy':
            mines = ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
                     '*', '*']

        for i in range(0, dimension):
            row = []
            for j in range(0, dimension):
                the_cell = random.choice(mines)
                row.append(the_cell)
                if the_cell == '*':
                    self._mine_count += 1
            self._spaces.append(row)
        board = []

        for i in range(0, len(self._spaces)):
            row2 = []
            for j in range(0, len(self._spaces[i])):
                mine_count = 0
                if self._spaces[i][j] == '   ':
                    if j + 1 < dimension:
                        if self._spaces[i][j + 1] == '*':
                            mine_count += 1
                        if i + 1 < dimension:
                            if self._spaces[i + 1][j + 1] == '*':
                                mine_count += 1
                        if i - 1 >= 0:
                            if self._spaces[i - 1][j + 1] == '*':
                                mine_count += 1
                    if j - 1 >= 0:
                        if self._spaces[i][j - 1] == '*':
                            mine_count += 1
                        if i + 1 < dimension:
                            if self._spaces[i + 1][j - 1] == '*':
                                mine_count += 1
                        if i - 1 >= 0:
                            if self._spaces[i - 1][j - 1] == '*':
                                mine_count += 1
                    if i + 1 < dimension:
                        if self._spaces[i + 1][j] == '*':
                            mine_count += 1
                    if i - 1 >= 0:
                        if self._spaces[i - 1][j] == '*':
                            mine_count += 1
                    if mine_count == 0:
                        mine_count = ' '
                    row2.append(mine_count)
                else:
                    row2.append(self._spaces[i][j])
            board.append(row2)
        self._spaces = []

        for j in board:
            row3 = []
            for i in j:
                row3.append(Space('[' + str(i) + ']'))
            self._spaces.append(row3)

    def display(self):
        ruler = ' '
        border = '+'

        for i in range(0, len(self._spaces[0])):
            if i < 10:
                ruler += ' ' + str(i) + '  '
            else:
                ruler += ' ' + str(i) + ' '
            border += '---+'
        print(ruler)
        print(border)
        i = 0

        for row in self._spaces:
            s = '|'
            for cell in row:
                s += cell.display_cell() + '|'
            s += ' ' + str(i)
            i += 1
            print(s)
            print(border)
        print('The current number of mines is ' + str(self._mine_count))

    def play(self, play, x, y):
        if play == 'unflag':
            if self._spaces[y][x].display_cell() == '[F]':
                self._spaces[y][x].unflag()
        elif play == 'flag':
            if self._spaces[y][x].display_cell() == '   ':
                self._spaces[y][x].flag()
                self._mine_count -= 1
        elif play == 'clear':
            if self._spaces[y][x].display_cell() == '   ':
                self._spaces[y][x].clear()
                if self._spaces[y][x].display_cell() == '[*]':
                    self._lost = True
                elif self._spaces[y][x].display_cell() == '[ ]':
                    for i in range(0, len(self._spaces)):
                        for j in range(0, len(self._spaces[i])):
                            if self._spaces[i][j].display_cell() == '[ ]':
                                if j + 1 < self._dimension:
                                    self._spaces[i][j + 1].clear()
                                    if i + 1 < self._dimension:
                                        self._spaces[i + 1][j + 1].clear()
                                    if i - 1 >= 0:
                                        self._spaces[i - 1][j + 1].clear()
                                if j - 1 >= 0:
                                    self._spaces[i][j - 1].clear()
                                    if i + 1 < self._dimension:
                                        self._spaces[i + 1][j - 1].clear()
                                    if i - 1 >= 0:
                                        self._spaces[i - 1][j - 1].clear()
                                if i + 1 < self._dimension:
                                    self._spaces[i + 1][j].clear()
                                if i - 1 >= 0:
                                    self._spaces[i - 1][j].clear()

                    for i in range(len(self._spaces) - 1, -1, -1):
                        for j in range(len(self._spaces[i]) - 1, -1, -1):
                            if self._spaces[i][j].display_cell() == '[ ]':
                                if j + 1 < self._dimension:
                                    self._spaces[i][j + 1].clear()
                                    if i + 1 < self._dimension:
                                        self._spaces[i + 1][j + 1].clear()
                                    if i - 1 >= 0:
                                        self._spaces[i - 1][j + 1].clear()
                                if j - 1 >= 0:
                                    self._spaces[i][j - 1].clear()
                                    if i + 1 < self._dimension:
                                        self._spaces[i + 1][j - 1].clear()
                                    if i - 1 >= 0:
                                        self._spaces[i - 1][j - 1].clear()
                                if i + 1 < self._dimension:
                                    self._spaces[i + 1][j].clear()
                                if i - 1 >= 0:
                                    self._spaces[i - 1][j].clear()

                    for i in range(0, len(self._spaces)):
                        for j in range(0, len(self._spaces[i])):
                            if self._spaces[i][j].display_cell() == '[ ]':
                                if j + 1 < self._dimension:
                                    self._spaces[i][j + 1].clear()
                                    if i + 1 < self._dimension:
                                        self._spaces[i + 1][j + 1].clear()
                                    if i - 1 >= 0:
                                        self._spaces[i - 1][j + 1].clear()
                                if j - 1 >= 0:
                                    self._spaces[i][j - 1].clear()
                                    if i + 1 < self._dimension:
                                        self._spaces[i + 1][j - 1].clear()
                                    if i - 1 >= 0:
                                        self._spaces[i - 1][j - 1].clear()
                                if i + 1 < self._dimension:
                                    self._spaces[i + 1][j].clear()
                                if i - 1 >= 0:
                                    self._spaces[i - 1][j].clear()

                    for i in range(len(self._spaces) - 1, -1, -1):
                        for j in range(len(self._spaces[i]) - 1, -1, -1):
                            if self._spaces[i][j].display_cell() == '[ ]':
                                if j + 1 < self._dimension:
                                    self._spaces[i][j + 1].clear()
                                    if i + 1 < self._dimension:
                                        self._spaces[i + 1][j + 1].clear()
                                    if i - 1 >= 0:
                                        self._spaces[i - 1][j + 1].clear()
                                if j - 1 >= 0:
                                    self._spaces[i][j - 1].clear()
                                    if i + 1 < self._dimension:
                                        self._spaces[i + 1][j - 1].clear()
                                    if i - 1 >= 0:
                                        self._spaces[i - 1][j - 1].clear()
                                if i + 1 < self._dimension:
                                    self._spaces[i + 1][j].clear()
                                if i - 1 >= 0:
                                    self._spaces[i - 1][j].clear()

                    for i in range(0, len(self._spaces)):
                        for j in range(0, len(self._spaces[i])):
                            if self._spaces[i][j].display_cell() == '[ ]':
                                if j + 1 < self._dimension:
                                    self._spaces[i][j + 1].clear()
                                    if i + 1 < self._dimension:
                                        self._spaces[i + 1][j + 1].clear()
                                    if i - 1 >= 0:
                                        self._spaces[i - 1][j + 1].clear()
                                if j - 1 >= 0:
                                    self._spaces[i][j - 1].clear()
                                    if i + 1 < self._dimension:
                                        self._spaces[i + 1][j - 1].clear()
                                    if i - 1 >= 0:
                                        self._spaces[i - 1][j - 1].clear()
                                if i + 1 < self._dimension:
                                    self._spaces[i + 1][j].clear()
                                if i - 1 >= 0:
                                    self._spaces[i - 1][j].clear()

                    for i in range(len(self._spaces) - 1, -1, -1):
                        for j in range(len(self._spaces[i]) - 1, -1, -1):
                            if self._spaces[i][j].display_cell() == '[ ]':
                                if j + 1 < self._dimension:
                                    self._spaces[i][j + 1].clear()
                                    if i + 1 < self._dimension:
                                        self._spaces[i + 1][j + 1].clear()
                                    if i - 1 >= 0:
                                        self._spaces[i - 1][j + 1].clear()
                                if j - 1 >= 0:
                                    self._spaces[i][j - 1].clear()
                                    if i + 1 < self._dimension:
                                        self._spaces[i + 1][j - 1].clear()
                                    if i - 1 >= 0:
                                        self._spaces[i - 1][j - 1].clear()
                                if i + 1 < self._dimension:
                                    self._spaces[i + 1][j].clear()
                                if i - 1 >= 0:
                                    self._spaces[i - 1][j].clear()

    def countinue_play(self):
        return not self._lost

    def you_won(self):
        count = 0

        for i in range(0, len(self._spaces)):
            for j in range(0, len(self._spaces[i])):
                if self._spaces[i][j].display_cell() == \
                    self._spaces[i][j].state() or \
                    (self._spaces[i][j].display_cell() ==
                     '[F]' and self._spaces[i][j].state() == '[*]') or \
                        self._spaces[i][j].state() == '[*]':
                    count += 1
        if count == self._dimension ** 2:
            return True
        return False

    def loss_display(self):
        for i in range(0, self._dimension):
            for j in range(0, self._dimension):
                self._spaces[i][j].clear()
        ruler = ' '
        border = '+'
        for i in range(0, len(self._spaces[0])):
            if i < 10:
                ruler += '  ' + str(i) + ' '
            else:
                ruler += ' ' + str(i)
            border += '---+'

        print(ruler)
        print(border)
        i = 0
        for row in self._spaces:
            s = '|'
            for cell in row:
                s += cell.display_cell() + '|'
            s += ' ' + str(i)
            i += 1
            print(s)
            print(border)


print('Welcome to Pysweeper!')
print('Available commands: clear, flag, unflag')
print('Example command: clear, 0, 0')
continue_playing = input()
while continue_playing == '':
    print('Please enter the size of the board you wish to play on.')
    size = input()
    size = int(size)
    print('Please enter a difficulty: (Easy, Medium, Hard)')
    difficulty = input()
    a = Board(size, difficulty)
    while a.countinue_play():
        a.display()
        print()
        print('What move would you like to play? ')
        move = input()
        move = move.split(',')
        move[1] = int(move[1])
        move[2] = int(move[2])
        a.play(move[0], move[1], move[2])
        if a.you_won():
            break
    if not a.countinue_play():
        print('You stepped on a mine! Better luck next time!')
        a.loss_display()
    elif a.you_won():
        print('You have secured the minefield! Congratulations!')
        a.display()
    print('Would you like to play again?')
    continue_playing = input()
