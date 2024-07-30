from piece import Piece
from colorama import Fore
from board import Board
class Pawn(Piece):
    moved: bool = False
    def __init__(self, position, team):
        if team == 0:
            super().__init__("pawn", "p", Fore.RED + "\u265F", position, team)
        else:
            super().__init__("pawn", "p", Fore.BLUE + "\u265F", position, team)

    def compute_move(self, positions: list[list[int]], board: Board):
        # first check possible moves, no attacks
        # the initial position
        pos0 = positions[0]
        # the requested position to move
        pos1 = positions[1]
        self.pos_moves = []
        # can make this code shorter later, ensure it works now
        if self.team == 0:
            if not self.moved:
                for i in range(1, 3):
                    # check all possible moves
                    # if a move is possible, add it to the list
                    # of possible moves
                    if board.board[pos0[0] - i][pos0[1]] == None:
                        # if the space is empty, allow move
                        self.pos_moves.append([pos0[0] - i, pos0[1]])
                    else:
                        # if a position is blocking other moves, do not
                        # consider those moves
                        break
        else:
            if not self.moved:
                for i in range(1, 3):
                    # check all possible moves
                    # if a move is possible, add it to the list
                    # of possible moves
                    if board.board[pos0[0] + i][pos0[1]] == None:
                        # if the space is empty, allow move
                        self.pos_moves.append([pos0[0] + i, pos0[1]])
                    else:
                        # if a position is blocking other moves, do not
                        # consider those moves
                        break
        # compute attacking positions

        # determine if the requested position is valid
        for move in self.pos_moves:
            if move[0] == pos1[0] and move[1] == pos1[1]:
                return True
        # the requested position is not valid
        return False
