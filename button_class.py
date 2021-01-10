import pygame
from settings import *

class Button:
    def __init__(self, game, pos_x, pos_y, width, height, bg_color = None, hover_color = None, text = None, function = None):
        self.game = game
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.text = text
        self.function = function
        self.hovered = False
        self.font = pygame.font.SysFont("arial", BUTTON_TEXT_SIZE)
        self.btn_text = self.font.render(self.text, True, (250,250,250))
        
    
    def update(self):
        # button changes color while hovered
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] > self.pos_x and mouse_pos[0] < (self.pos_x + self.width):
            if mouse_pos[1] > self.pos_y and mouse_pos[1] < (self.pos_y + self.height):
                self.hovered = True
        else:
            self.hovered = False

    def draw(self):
        if not self.hovered:
            pygame.draw.rect(self.game.screen,self.bg_color,[self.pos_x, self.pos_y, self.width, self.height])
        else:
            pygame.draw.rect(self.game.screen,self.hover_color,[self.pos_x, self.pos_y, self.width, self.height])
        self.game.screen.blit(self.btn_text, (self.pos_x + (self.width - self.btn_text.get_width())//2, self.pos_y + (self.height - self.btn_text.get_height())//2))

    def click(self):
        if self.function is not None and self.hovered:
            self.function()
        else:
            pass