from piece import Piece
from colorama import Fore
from board import Board
class Rook(Piece):
    def __init__(self, position, team):
        if team == 0:
            super().__init__("rook", "r", Fore.RED + "\u265C", position, team)
        else:
            super().__init__("rook", "r", Fore.BLUE + "\u265C", position, team)
    
    def compute_move(self, positions: list[list[int]], board: Board):
        # first check possible moves
        # the team alignment is checked in the calling function

        # the initial position
        pos0 = positions[0]
        # the requested position to move
        pos1 = positions[1]
        self.pos_moves = []

        ud_var = 0
        if self.team == 0:
            ud_var = -1
        else:
            ud_var = 1

        # check up down direction
        # ensure all coordinates match
        offset = 1
        while (pos0[0] - offset) in range(0, 8):
            piece = board.board[pos0[0] - offset][pos0[1]]
            if piece == None:
                self.pos_moves.append([pos0[0] - offset, pos0[1]])
            elif piece.team != self.team:
                self.pos_moves.append([pos0[0] - offset, pos0[1]])
                break
            else:
                break
            offset += 1
        offset = 1
        while (pos0[0] + offset) in range(0, 8):
            piece = board.board[pos0[0] + offset][pos0[1]]
            if piece == None:
                self.pos_moves.append([pos0[0] + offset, pos0[1]])
            elif piece.team != self.team:
                self.pos_moves.append([pos0[0] + offset, pos0[1]])
                break
            else:
                break
            offset += 1
        
        # check left right direction
        offset = 1
        while (pos0[1] - offset) in range(0, 8):
            piece = board.board[pos0[0]][pos0[1] - offset]
            if piece == None:
                self.pos_moves.append([pos0[0], pos0[1] - offset])
            elif piece.team != self.team:
                self.pos_moves.append([pos0[0], pos0[1] - offset])
                break
            else:
                break
            offset += 1
        offset = 1
        while (pos0[1] + offset) in range(0, 8):
            piece = board.board[pos0[0]][pos0[1] + offset]
            if piece == None:
                self.pos_moves.append([pos0[0], pos0[1] + offset])
            elif piece.team != self.team:
                self.pos_moves.append([pos0[0], pos0[1] + offset])
                break
            else:
                break
            offset += 1

        # check validity of requested position
        for move in self.pos_moves:
            if move[0] == pos1[0] and move[1] == pos1[1]:
                return True
        return False