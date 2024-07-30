from piece import Piece
from colorama import Fore
from board import Board
class Bishop(Piece):
    def __init__(self, position, team):
        if team == 0:
            super().__init__("bishop", "b", Fore.RED + "\u265D", position, team)
        else:
            super().__init__("bishop", "b", Fore.BLUE + "\u265D", position, team)
    
    def compute_move(self, positions: list[list[int]], board: Board):
        # first check possible moves
        # the team alignment is checked in the calling function

        # the initial position
        pos0 = positions[0]
        # the requested position to move
        pos1 = positions[1]
        # empty the possible moves list
        self.pos_moves = []

        ud_var = 0
        if self.team == 0:
            ud_var = -1
        else:
            ud_var = 1
        
        # check first diagonal TL to BR, start from the piece position
        # ensure all coordinates match
        offset = 1
        while (pos0[0] + offset) in range(0,8) and (pos0[1] + offset) in range(0,8):
            piece = board.board[pos0[0] + offset][pos0[1] + offset]
            if piece == None:
                # add the empty space to valid list
                self.pos_moves.append([pos0[0] + offset, pos0[1] + offset])
            elif piece.team != self.team:
                # if enemy piece is found, add to valid list
                # but break
                self.pos_moves.append(piece.position)
                break
            else:
                # break if own piece is blocking a path
                break
            offset += 1
        offset = 1
        while (pos0[0] - offset) in range(0,8) and (pos0[1] - offset) in range(0,8):
            piece = board.board[pos0[0] - offset][pos0[1] - offset]
            if piece == None:
                # add empty space to valid list
                self.pos_moves.append([pos0[0] - offset, pos0[1] - offset])
            elif piece.team != self.team:
                # if enemy piece is found, add to valid list
                # but break
                self.pos_moves.append(piece.position)
                break
            else:
                # break if own piece is blocking a path
                break
            offset += 1

        # check the second diagonal, BL to TR
        offset = 1
        while (pos0[0] - offset) in range(0,8) and (pos0[1] + offset) in range(0,8):
            piece = board.board[pos0[0] - offset][pos0[1] + offset]
            if piece == None:
                # add empty space to valid list
                self.pos_moves.append([pos0[0] - offset, pos0[1] + offset])
            elif piece.team != self.team:
                # if enemy piece is found, add to valid list
                # but break
                self.pos_moves.append(piece.position)
                break
            else:
                # break if own piece is blocking a path
                break
            offset += 1
        offset = 1
        while (pos0[0] + offset) in range(0,8) and (pos0[1] - offset) in range(0,8):
            piece = board.board[pos0[0] + offset][pos0[1] - offset]
            if piece == None:
                # add empty space to valid list
                self.pos_moves.append([pos0[0] + offset, pos0[1] - offset])
            elif piece.team != self.team:
                # if enemy piece is found, add to valid list
                # but break
                self.pos_moves.append(piece.position)
                break
            else:
                # break if own piece is blocking a path
                break
            offset += 1

        # check if the requested position is in the list of valid
        # positions
        for move in self.pos_moves:
            # move is valid
            if move[0] == pos1[0] and move[1] == pos1[1]:
                return True
        # move is invalid
        return False