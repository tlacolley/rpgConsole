#!/usr/bin/env python
# -- coding: UTF-8 --

class Board(object):
    def __init__(self,nb_col, nb_row):
        self.grid = []
        for col in range(nb_col):
            self.grid.append([])
            for row in range(nb_row):
                self.grid[col].append([])


    def move(self, character, x, y):
        if character.x != None or character.y != None:
            self.grid[character.x][character.y].remove(character)
        character.x = x
        character.y = y
        self.grid[x][y].append(character)

    def display(self):
        map = ""
        # print map
        for line in self.grid:
            row = ""
            for cell in line:
                if not cell:
                    row += "-"
                else:
                    row += "X"
            row += "\n"
            map += row
        return map
        # print "lop"
        # print map
        # print "plop"
