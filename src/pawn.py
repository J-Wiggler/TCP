from piece import Piece
from colorama import Fore
class Pawn(Piece):
    def __init__(self, position, team):
        if team == 0:
            super().__init__("pawn", "p", Fore.RED + "\u265F", position, team)
        else:
            super().__init__("pawn", "p", Fore.BLUE + "\u265F", position, team)
