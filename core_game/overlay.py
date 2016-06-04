import board
import pygame


class OverlaySquare(board.Square):

    def __init__(self, position, size, color, coords):
        board.Square.__init__(self, position, size, color, coords)
        self.surface = pygame.Surface((size, size))
        self.original_color = self.color

        self.redraw()

    def redraw(self):
        pygame.draw.rect(self.surface, self.color, pygame.Rect((0, 0), (self.size, self.size)))
        pygame.draw.rect(self.surface, (0, 0, 0), pygame.Rect((0, 0), (self.size, self.size)), 1)

    def clear_color(self):
        self.color = 255,255,255
        self.surface.set_alpha(0)


    def add_green(self, amount):
        self.color = self.color[0] - amount, self.color[1], self.color[2] - amount

    def add_red(self, amount):
        self.color = self.color[0], self.color[1] - amount, self.color[2] - amount

    def add_blue(self, amount):
        self.color = self.color[0]- amount, self.color[1] - amount, self.color[2]

    def draw(self, surface):
        surface.blit(self.surface, self.rect)


class Overlay(board.Board):

    def __init__(self, size_px):
        board.Board.__init__(self, size_px, square_type=OverlaySquare)
        self.clear_squares()
        for x in range(2):
            self.ally_threat((0,0))


    def ally_threat(self, position, strength=50):
        sq = self.squares[position[0]][position[1]]
        sq.add_green(strength)
        sq.redraw()
        sq.surface.set_alpha(255)

    def enemy_threat(self, position):
        sq = self.squares[position[0]][position[1]]
        sq.add_red(20)
        sq.redraw()
        sq.surface.set_alpha(255)

    def clear_squares(self):
        for row in self.squares:
            for sq in row:
                sq.clear_color()
                sq.redraw()













