from __future__ import division
import pygame


class Board(object):

    def __init__(self, size_px):
        self.squares = []
        self.size = size_px
        size = size_px / 8
        for y in range(8):
            for x in range(8):
                color = (255,235,205) if (x + y) % 2 == 0 else (139,69,19)
                self.squares.append(Square((x * size, y * size), size, color))

    def draw(self, surface):
        for sq in self.squares:
            sq.draw(surface)



class Square(object):

    def __init__(self, position, size, color):
        self.position = position
        self.color = color
        self.rect = pygame.Rect(position, (size, size))

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)