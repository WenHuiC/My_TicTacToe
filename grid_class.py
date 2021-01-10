"""  
copyright © 2020 wen hui
@file My_TicTacToe
@brief  This class generates the grid of the game. At the same time, 
        it provides the functions of tracking the grid status, including
        the judgment of game win or loss, players' playing record, etc.
@author Wen Hui Chen
@date 2020/01/09 
"""

import pygame
from settings import *
from cell_class import *

class Grid:
    def __init__(self, game):
        self.game = game
        self.pos = (GRID_POS[0],GRID_POS[1])
        self.cells = []
        self.make_grid()
        self.winner = None
        self.won = False

    def make_grid(self):
        for y in range(3):
            for x in range(3):
                self.cells.append(Cell(self,x,y)) # append cell objects to cells array

    def update(self):
        if not self.won:
            self.check_for_winner()
        if self.won:
            pass
        else:    
            for cell in self.cells:
                cell.update()

    def draw(self):
        for cell in self.cells:
            cell.draw()

    def check_for_winner(self):
        # check horizontal neighbor
        if self.cells[0].owner == self.cells[1].owner and self.cells[0].owner == self.cells[2].owner and self.cells[0].owner is not None:
            self.winner = self.cells[0].owner
            self.won = True
        elif self.cells[3].owner == self.cells[4].owner and self.cells[3].owner == self.cells[5].owner and self.cells[3].owner is not None:
            self.winner = self.cells[3].owner
            self.won = True
        elif self.cells[6].owner == self.cells[7].owner and self.cells[6].owner == self.cells[8].owner and self.cells[6].owner is not None:
            self.winner = self.cells[6].owner
            self.won = True
        # check vertical neighbor
        elif self.cells[0].owner == self.cells[3].owner and self.cells[0].owner == self.cells[6].owner and self.cells[0].owner is not None:
            self.winner = self.cells[0].owner
            self.won = True
        elif self.cells[1].owner == self.cells[4].owner and self.cells[1].owner == self.cells[7].owner and self.cells[1].owner is not None:
            self.winner = self.cells[1].owner
            self.won = True
        elif self.cells[2].owner == self.cells[5].owner and self.cells[2].owner == self.cells[8].owner and self.cells[2].owner is not None:
            self.winner = self.cells[2].owner
            self.won = True
        # check diagonal neighbor
        elif self.cells[0].owner == self.cells[4].owner and self.cells[0].owner == self.cells[8].owner and self.cells[0].owner is not None:
            self.winner = self.cells[0].owner
            self.won = True
        elif self.cells[2].owner == self.cells[4].owner and self.cells[2].owner == self.cells[6].owner and self.cells[2].owner is not None:
            self.winner = self.cells[2].owner
            self.won = True
        else:
            pass

    # return True while all cell.owner is not None
    def game_draw(self):
        count = 0
        for cell in self.cells:
            if cell.owner is not None:
                count += 1
        if count == 9 and not self.won:
            return True
        return False
        

        


