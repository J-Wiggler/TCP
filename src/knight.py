from piece import Piece
from colorama import Fore
from board import Board
class Knight(Piece):
    def __init__(self, position, team):
        if team == 0:
            super().__init__("knight", "n", Fore.RED + "\u265E", position, team)
        else:
            super().__init__("knight", "n", Fore.BLUE + "\u265E", position, team)
    
    def compute_move(self, positions: list[list[int]], board: Board):
        # the initial position
        pos0 = positions[0]
        # the requested position to move
        pos1 = positions[1]
        # empty the possible moves list
        self.pos_moves = []

        # 8 possible knight movement offsets
        moves = [(-2, 1), (-2, -1), (-1, 2), (-1, -2), (2, 1), (2, -1), (1, 2), (1, -2)]
        for move in moves:
            if (pos0[0] + move[0]) in range(0, 8) and (pos0[1] + move[1]) in range(0, 8):
                piece = board.board[pos0[0] + move[0]][pos0[1] + move[1]]
                if piece == None or piece.team != self.team:
                    self.pos_moves.append([pos0[0] + move[0], pos0[1] + move[1]])
        
        for move in self.pos_moves:
            if move[0] == pos1[0] and move[1] == pos1[1]:
                return True
        return False
