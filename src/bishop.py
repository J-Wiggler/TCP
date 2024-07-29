from piece import Piece
from colorama import Fore
class Bishop(Piece):
    def __init__(self, position, team):
        if team == 0:
            super().__init__("bishop", "b", Fore.RED + "\u265D", position, team)
        else:
            super().__init__("bishop", "b", Fore.BLUE + "\u265D", position, team)