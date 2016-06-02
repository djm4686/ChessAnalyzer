import pygame
import core_game.chess_game_manager
from pygame.locals import *

WIDTH = 1024
HEIGHT = 768

class GameController(object):

    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.game_manager = core_game.chess_game_manager.ChessGameManager(WIDTH, HEIGHT)

    def main(self):
        while True:
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()


    def update(self):
        self.game_manager.update()

    def draw(self):
        self.surface.fill((128, 128, 128))
        self.game_manager.draw(self.surface)
        pygame.display.update()


if __name__ == "__main__":
    g = GameController()
    g.main()