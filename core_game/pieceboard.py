import board


class PieceSquare(board.Square):

    def __init__(self, position, size, color, coordinates):
        board.Square.__init__(self, position, size, color, coordinates)


class PieceBoard(board.Board):

    def __init__(self, size_px):
        board.Board.__init__(self, size_px, square_type=PieceSquare)
