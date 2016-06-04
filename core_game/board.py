from __future__ import division
import pygame


class Square(object):

    def __init__(self, position, size, color, coordinates):
        self.position = position
        self.color = color
        self.size = size
        self.rect = pygame.Rect(position, (size, size))
        self.coordinates = coordinates

    def get_position(self):
        return self.position

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def draw_outline(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 1)


class Board(object):

    def __init__(self, size_px, square_type=Square):
        self.squares = []
        self.size = size_px
        size = size_px / 8
        for y in range(8):
            row = []
            for x in range(8):
                color = (255,235,205) if (x + y) % 2 == 0 else (139,69,19)
                row.append(square_type((x * size, y * size), size, color, (y, x)))
            self.squares.append(row)



    def collide_point(self, pt):
        for row in self.squares:
            for sq in row:
                if sq.rect.collidepoint(pt):
                    return sq
        return None

    def draw(self, surface):
        for row in self.squares:
            for sq in row:
                sq.draw(surface)
                sq.draw_outline(surface)



