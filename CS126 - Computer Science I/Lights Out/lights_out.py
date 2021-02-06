#!/usr/bin/env python

"""

A simple game of Lights Out.

"""

import random


class Light(object):

    def __init__(self, state):
        self._power = state

    def toggle(self):
        self._power = not(self._power)

    def power(self):
        return self._power


def randbool():
    return random.randint(0, 1) == 1


class Board(object):

    def __init__(self, dimension):
        self._lights = []
        for i in range(0, dimension):
            row = []
            for j in range(0, dimension):
                row.append(Light(randbool()))
            self._lights.append(row)

    def display(self):
        ruler = ' '
        border = '+'
        for i in range(0, len(self._lights[0])):
            ruler += str(i) + ' '
            border += '-+'
        print(ruler)
        print(border)
        i = 0
        for row in self._lights:
            s = '|'
            for light in row:
                if light.power():
                    s += '*|'
                else:
                    s += ' |'
            s += ' ' + str(i)
            i += 1
            print(s)
            print(border)

    def play(self, x, y):
        self._lights[y][x].toggle()
        if x - 1 >= 0:
            self._lights[y][x - 1].toggle()
        if x + 1 < len(self._lights[0]):
            self._lights[y][x + 1].toggle()
        if y - 1 >= 0:
            self._lights[y - 1][x].toggle()
        if y + 1 < len(self._lights):
            self._lights[y + 1][x].toggle()

    def is_power_on(self):
        win = True
        for row in self._lights:
            for light in row:
                if light.power():
                    win = False
        return not win


b = Board(5)
while b.is_power_on():
    b.display()
    print('')
    print('What move would you like to play?')
    move = input()
    move = move.split(',')
    move[0] = int(move[0])
    move[1] = int(move[1])
    b.play(move[0], move[1])

print('You win! The lights are out.')
