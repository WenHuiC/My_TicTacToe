"""  
copyright © 2020 wen hui
@file My_TicTacToe
@brief  Display naughts and cross.
        Record the owner of each cell.
@author Wen Hui Chen
@date 2020/01/09 
"""

import pygame
from settings import *

class Cell:
    def __init__(self,grid, pos_x, pos_y):
        self.grid = grid
        self.pos = (pos_x, pos_y)
        self.size = CELL_SIZE
        self.revealed = False
        self.owner = None

    def update(self):
        pass

    def draw(self):
        if not self.revealed:
            pygame.draw.rect(self.grid.game.screen,CELL_BG_COLOR,[self.grid.pos[0] + (self.pos[0]*self.size),self.grid.pos[1] + (self.pos[1]*self.size),self.size,self.size],2)
        else:
            if self.owner == 1:
                # display naught for player 1
                pygame.draw.circle(self.grid.game.screen,SHAPE_COLOR,[self.grid.pos[0] + (self.pos[0]*self.size + self.size//2),self.grid.pos[1] + (self.pos[1]*self.size + self.size//2)],30,6)
            else:
                # display cross for player 2
                cross_L1_P1 = (self.grid.pos[0] + self.pos[0]*self.size + 20, self.grid.pos[1] + self.pos[1]*self.size + 20)
                cross_L1_P2 = (self.grid.pos[0] + (self.pos[0]+1)*self.size - 20, self.grid.pos[1] + (self.pos[1]+1)*self.size - 20)
                cross_L2_P1 = (self.grid.pos[0] + (self.pos[0]+1)*self.size - 20, self.grid.pos[1] + self.pos[1]*self.size + 20)
                cross_L2_P2 = (self.grid.pos[0] + self.pos[0]*self.size + 20, self.grid.pos[1] + (self.pos[1]+1)*self.size - 20)
                pygame.draw.line(self.grid.game.screen,SHAPE_COLOR,cross_L1_P1,cross_L1_P2,10)
                pygame.draw.line(self.grid.game.screen,SHAPE_COLOR,cross_L2_P1,cross_L2_P2,10)
                
            pygame.draw.rect(self.grid.game.screen,CELL_BG_COLOR,[self.grid.pos[0] + (self.pos[0]*self.size),self.grid.pos[1] + (self.pos[1]*self.size),self.size,self.size],2)

    def click(self):
        if not self.grid.won:
            if not self.revealed:
                # record owner to cell
                self.owner = self.grid.game.active_player
                self.revealed = True
        else:
            pass
