from piece import Piece
from colorama import Fore
class Queen(Piece):
    def __init__(self, position, team):
        if team == 0:
            super().__init__("queen", "q", Fore.RED + "\u265B", position, team)
        else:
            super().__init__("queen", "q", Fore.BLUE + "\u265B", position, team)