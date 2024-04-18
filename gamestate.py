class GameState():
    def __init__(self, board={'A1':'e', 'D1':'e', 'G1':'e', 'B2':'e', 'D2':'e', 'F2':'e', 'C3':'e', 'D3':'e', 'E3':'e', 'A4':'e', 'B4':'e', 'C4':'e', 'E4':'e', 'F4':'e', 'G4':'e', 'C5':'e', 'D5':'e', 'E5':'e', 'B6':'e', 'D6':'e', 'F6':'e', 'A7':'e', 'D7':'e', 'G7':'e'}, to_move='b', move_type='set', pieces_b=9, pieces_w=9):
        self.board = board
        self.to_move = to_move
        self.move_type = move_type
        self.pieces_b = pieces_b
        self.pieces_w = pieces_w

    def __str__(self) -> str:
        return f"Board: {self.board},\nTo Move: {self.to_move},\nMove Type: {self.move_type},\nBlacks Pieces to place: {self.pieces_b},\nWhites Pieces to place: {self.pieces_w}"