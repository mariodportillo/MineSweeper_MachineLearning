import pygame
from settings import *
from sprites import *

#Class here enables the game to boot up and run setting the stage for all the game elements.
class Game:
    #Here we are creating a function that creates the window where the game will be played.
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

    #Here we are creating a function that will have all the game actions
    def new(self):
        self.board = Board()
        self.board.display_board()

    #This function will run when a new game is started. 
    def run(self):
        self.playing = True
        while self.playing: 
            self.clock.tick(FPS)
            self.events()
            self.draw()
        else:
            self.end_screen()
    
    #This function will draw itself and adjsut the screen as needed.
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.board.draw(self.screen)
        pygame.display.flip()

    def check_win(self):
        for row in self.board.board_list:
            for tile in row:
                if tile.type != "x" and not tile.revealed:
                    return False
        return True

    #This function allows for users to exit the program and what the program should do as it closes. 
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                mx //= TILESIZE
                my //= TILESIZE

                if event.button == 1:
                    if not self.board.board_list[mx][mx].flagged:
                        #dig and check if exploded
                        if not self.board.dig(mx, my):
                            #explode
                            for row in self.board.board_list:
                                for tile in row:
                                    if tile.flagged and tile.type != "x":
                                        tile.flagged = False
                                        tile.revealed = True
                                        tile.image = tile_not_mine
                                    elif tile.type == "x":
                                        tile.revealed = True
                            self.palying = False

                if event.button == 3:
                    if not self.board.board_list[mx][my].revealed:
                        self.board.board_list[mx][my].flagged = not self.board.board_list[mx][my].flagged

                if self.check_win():
                    self.win = True
                    self.playing = False
                    for row in self.board.board_list:
                        for tile in row:
                            if not tile.revealed:
                                tile.flagged = True
    def end_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return



    
game = Game()
while True:
    game.new()
    game.run()