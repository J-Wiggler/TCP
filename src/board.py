# class to define a board object
from piece import Piece
from colorama import Fore
class Board:
    # standard dimensions of a chessboard
    dim = (8, 8)
    # 2d array to hold the board state
    board: list[list[None]]
    # list containing the two tile colors
    tiles = ["\u25A6", "\u25A1"]

    # ensure all positions on the board are unique locations in memory
    def __init__(self) -> None:
        self.board = []
        for row in range(8):
            self.board.append([])
            for col in range(8):
                self.board[row].append(None)
        pass

    # prints the board to stdout
    def draw_board(self):
        print(Fore.WHITE + "  0 1 2 3 4 5 6 7")
        # iterate over all rows
        for row in range(8):
            print(Fore.WHITE + str(row) + " ", end="")
            for col in range(8):
                if self.board[row][col] != None:
                    piece = self.board[row][col]
                    print(piece.icon + " ", end="")
                else:
                    print(Fore.GREEN + self.tiles[(row + col) % 2] + " ", end="")
            print()

    def add_piece(self, new_piece: Piece):
        r = new_piece.position[0]
        c = new_piece.position[1]
        self.board[r][c] = new_piece

    # takes a piece as a parameter and moves it to the specified position
    def move_piece(self, piece: Piece, position: list[int], enemy_pieces: list):
        # remove the piece at the current location on the board
        self.board[piece.position[0]][piece.position[1]] = None
        # get the target position
        # if none, no attack was made
        # if the target has a piece, an attack was made
        # remove the attacked piece
        target = self.board[position[0]][position[1]]
        if target != None and target in enemy_pieces:
            enemy_pieces.pop(enemy_pieces.index(target))
        self.board[position[0]][position[1]] = piece
        piece.position = position

    def print_array(self):
        print(self.board)


