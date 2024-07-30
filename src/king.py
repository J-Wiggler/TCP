from piece import Piece
from colorama import Fore
from board import Board
class King(Piece):
    def __init__(self, position, team):
        if team == 0:
            super().__init__("king", "k", Fore.RED + "\u265A", position, team)
        else:
            super().__init__("king", "k", Fore.BLUE + "\u265A", position, team)

    def compute_move(self, positions: list[list[int]], board: Board):
        # the initial position
        pos0 = positions[0]
        # the requested position to move
        pos1 = positions[1]
        # empty the possible moves list
        self.pos_moves = []

        # 8 possible move directions
        moves = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        for move in moves:
            if (pos0[0] + move[0]) in range(0, 8) and (pos0[1] + move[1]):
                piece = board.board[pos0[0] + move[0]][pos0[1] + move[1]]
                if piece == None or piece.team != self.team:
                    self.pos_moves.append([pos0[0] + move[0], pos0[1] + move[1]])
        
        for move in self.pos_moves:
            if move[0] == pos1[0] and move[1] == pos1[1]:
                return True
        return False