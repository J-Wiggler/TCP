from piece import Piece
from colorama import Fore
class Rook(Piece):
    def __init__(self, position, team):
        if team == 0:
            super().__init__("rook", "r", Fore.RED + "\u265C", position, team)
        else:
            super().__init__("rook", "r", Fore.BLUE + "\u265C", position, team)