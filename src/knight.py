from piece import Piece
from colorama import Fore
class Knight(Piece):
    def __init__(self, position, team):
        if team == 0:
            super().__init__("knight", "n", Fore.RED + "\u265E", position, team)
        else:
            super().__init__("knight", "n", Fore.BLUE + "\u265E", position, team)