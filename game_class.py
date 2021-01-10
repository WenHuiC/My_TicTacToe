"""  
copyright © 2020 wen hui
@file My_TicTacToe
@brief  This class contained the main execution process of the Tic Tac Toe game, 
        including the update of the status and the revealization of the screen.
        By changing the state, the application can be switched between intro state and playing state.
@author Wen Hui Chen
@date 2020/01/09 
"""

import pygame
from settings import *
import grid_class
import button_class

class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('My TicTacToe')
        self.grid = grid_class.Grid(self)
        self.active_player = 1
        self.state = 'intro'
        self.intro_buttons = []
        self.playing_buttons = []
        self.make_buttons()

        self.title_font = pygame.font.SysFont("arial", TITLE_TEXT_SIZE)
        self.title_text = self.title_font.render('Tic Tac Toe', True, TITLE_TEXT_COLOR)
        self.copyright_font = pygame.font.SysFont("arial", COPYRIGHT_TEXT_SIZE)
        self.copyright_text = self.copyright_font.render('----- copyright © 2020 wen hui -----', True, COPYRIGHT_TEXT_COLOR)
        self.sys_font = pygame.font.SysFont("arial", SYS_TEXT_SIZE)

    def run(self):
        print('---------------------')
        print('      START GAME    ')
        print('---------------------')
        while self.running:
            self.get_events()
            self.update()
            self.draw()
        pygame.quit()
        
    def get_events(self):
        if self.state == 'playing':
            self.playing_events()
        elif self.state == 'intro':
            self.intro_events()

    def update(self):
        if self.state == 'playing':
            self.playing_update()
        elif self.state == 'intro':
            self.intro_update()

    def draw(self):
        self.screen.fill(BG_COLOUR)
        pygame.draw.rect(self.screen,FRAME_COLOR,[(SCREEN_WIDTH-THIN_FRAME_WIDTH)//2,(SCREEN_HEIGHT-THIN_FRAME_HEIGHT)//2,THIN_FRAME_WIDTH,THIN_FRAME_HEIGHT],2)
        pygame.draw.rect(self.screen,FRAME_COLOR,[(SCREEN_WIDTH-THICK_FRAME_WIDTH)//2,(SCREEN_HEIGHT-THICK_FRAME_HEIGHT)//2,THICK_FRAME_WIDTH,THICK_FRAME_HEIGHT],6)

        if self.state == 'playing':
            self.playing_draw()
        elif self.state == 'intro':
            self.intro_draw()
        pygame.display.update()

    def make_buttons(self):
        btn_start_game = button_class.Button(self,(SCREEN_WIDTH-180)//2,210,180,50,BTN_BG_COLOR,BTN_HOVER_COLOR,text = 'Start New Game',function = self.from_intro_to_play)
        self.intro_buttons.append(btn_start_game)
        btn_clear_board = button_class.Button(self,GRID_POS[0],(GRID_POS[1]+CELL_SIZE*3+25),120,40,BTN_BG_COLOR,BTN_HOVER_COLOR,text = 'Clear Board', function = self.clear_board_for_new_game)
        self.playing_buttons.append(btn_clear_board)
        btn_home = button_class.Button(self,(GRID_POS[0]+CELL_SIZE*3-100),(GRID_POS[1]+CELL_SIZE*3+25),100,40,BTN_BG_COLOR,BTN_HOVER_COLOR, text ='Home',function = self.from_play_to_intro)
        self.playing_buttons.append(btn_home)


# ----- intro state ----
    def intro_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for btn in self.intro_buttons:
                    btn.click()

    def intro_update(self):
        for button in self.intro_buttons:
            button.update()

    def intro_draw(self):
        # display title on intro page
        self.screen.blit(self.title_text, ((SCREEN_WIDTH - self.title_text.get_width())//2,120))
        self.screen.blit(self.copyright_text, ((SCREEN_WIDTH - self.copyright_text.get_width())//2,520))
        for button in self.intro_buttons:
            button.draw()

# ----- playing state -----
    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.click_on_grid(mouse_pos):
                    # get selected grid position
                    mouse_grid_pos = self.get_grid_pos(mouse_pos)
                    for cell in self.grid.cells:
                        if cell.pos[0] == mouse_grid_pos[0] and cell.pos[1] == mouse_grid_pos[1] and cell.owner is None:
                            cell.click()
                            self.change_active_player()
                for btn in self.playing_buttons:
                    btn.click()

    def playing_update(self):
        self.grid.update()
        for button in self.playing_buttons:
            button.update()
    
    def playing_draw(self):
        self.screen.blit(self.title_text, ((SCREEN_WIDTH - self.title_text.get_width())//2,50)) # display game title
        self.grid.draw()

        # sys text - display active player and winner info
        if self.grid.game_draw():
            player_text = "Game ended in a draw"
        elif not self.grid.won:
            player_text = "Player " + str(self.active_player) + "'s turn to play"
        else:
            player_text = "Player " + str(self.grid.winner) + " has won the game !!!"
        self.sys_text = self.sys_font.render(player_text, True, SYS_TEXT_COLOR)
        self.screen.blit(self.sys_text, ((SCREEN_WIDTH - self.sys_text.get_width())//2, 120))

        for button in self.playing_buttons:
            button.draw()

# ----- other functions -----

    # make sure mouse click on grid
    def click_on_grid(self, mouse_pos):
        if mouse_pos[0] > GRID_POS[0] and mouse_pos[0] < GRID_POS[0] + (CELL_SIZE * 3):
            if mouse_pos[1] > GRID_POS[1] and mouse_pos[1] < GRID_POS[1] + (CELL_SIZE *3):
                return True
        return False

    def change_active_player(self):
        if self.active_player == 1:
            self.active_player = 2
        else:
            self.active_player = 1

    # get selected grid's cell position
    def get_grid_pos(self, pos):
        grid_x = (pos[0] - GRID_POS[0])//CELL_SIZE
        grid_y = (pos[1] - GRID_POS[1])//CELL_SIZE
        return [grid_x, grid_y]

# ----- button funtion -----

    def from_intro_to_play(self):
        self.state = 'playing'

    def from_play_to_intro(self):
        # back to intro page + clear board for new game
        self.state = 'intro'
        self.grid = grid_class.Grid(self)
        self.active_player = 1

    def clear_board_for_new_game(self):
        # create new board
        self.grid = grid_class.Grid(self)
        # init active player to player 1
        self.active_player = 1


