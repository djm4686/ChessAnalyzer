

class Piece(object):

    def __init__(self, piece_id, position, owner, type):
        self.piece_id = piece_id
        self.position = position
        self.owner = owner
        self.piece_type = type

    def get_threat(self):
        pass



