from board import Board
from test_piece import TestPiece
from colorama import Fore
from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
# define user interaction with the game

# setup the initial pieces and draw the board
def initialize_board(red: list, blue: list, board: Board):
    # print initialization message and turn
    print("\nBEGIN")
    print("<<TURN 0::BLUE TO MOVE>>\n")

    # initialize the pawns
    for i in range(8):
        p0 = Pawn([1, i], 0)
        p1 = Pawn([6, i], 1)
        red.append(p0)
        blue.append(p1)
        board.add_piece(p0)
        board.add_piece(p1)
    # initialize the rest of the pieces
    #########
    # ROOKS
    #########
    p = Rook(position=[0, 0], team=0)
    red.append(p)
    board.add_piece(p)

    p = Rook(position=[0, 7], team=0)
    red.append(p)
    board.add_piece(p)

    p = Rook(position=[7, 0], team=1)
    blue.append(p)
    board.add_piece(p)

    p = Rook(position=[7, 7], team=1)
    blue.append(p)
    board.add_piece(p)

    ##########
    # KNIGHTS
    ##########
    p = Knight(position=[0, 1], team=0)
    red.append(p)
    board.add_piece(p)

    p = Knight(position=[0, 6], team=0)
    red.append(p)
    board.add_piece(p)

    p = Knight(position=[7, 1], team=1)
    blue.append(p)
    board.add_piece(p)

    p = Knight(position=[7, 6], team=1)
    blue.append(p)
    board.add_piece(p)

    ##########
    # BISHOPS
    ##########
    p = Bishop(position=[0, 2], team=0)
    red.append(p)
    board.add_piece(p)

    p = Bishop(position=[0, 5], team=0)
    red.append(p)
    board.add_piece(p)

    p = Bishop(position=[7, 2], team=1)
    blue.append(p)
    board.add_piece(p)

    p = Bishop(position=[7, 5], team=1)
    blue.append(p)
    board.add_piece(p)

    #########
    # QUEENS
    #########
    p = Queen(position=[0, 3], team=0)
    red.append(p)
    board.add_piece(p)

    p = Queen(position=[7, 3], team=1)
    blue.append(p)
    board.add_piece(p)

    #########
    # KINGS
    #########
    p = King(position=[0, 4], team=0)
    red.append(p)
    board.add_piece(p)

    p = King(position=[7, 4], team=1)
    blue.append(p)
    board.add_piece(p)

    # draw the board
    board.draw_board()

def main():
    # turn counter
    turn = 0
    # lists to contain each player's pieces
    red = []
    blue = []

    # initialize the main board
    m_board = Board()

    # game start, menu of sorts
    print("WELCOME TO CHESST")

    while True:
        cmd = input("START(s) | QUIT(q) >> ")
        if cmd.upper() == "S":
            initialize_board(red=red, blue=blue, board=m_board)
            break
        elif cmd.upper() == "Q":
            print("Farewell")
            exit(0)
        else:
            print("Bad input. Try again.")

if __name__ == "__main__":
    main()