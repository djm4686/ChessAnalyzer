import pygame
import board
import overlay
from locals import *


class ChessGameManager(object):

    def __init__(self, width, height):
        self.game_board = board.Board(height)
        self.overlay = overlay.Overlay(height)
        self.turn = WHITE
        self.selected_piece = None

    def select_piece(self, piece):
        if piece.owner == self.turn:
            self.selected_piece = piece

    def update(self):
        pass

    def draw(self, surface):
        self.game_board.draw(surface)
        self.overlay.draw(surface)
