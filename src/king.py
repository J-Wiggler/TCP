from piece import Piece
from colorama import Fore
class King(Piece):
    def __init__(self, position, team):
        if team == 0:
            super().__init__("king", "k", Fore.RED + "\u265A", position, team)
        else:
            super().__init__("king", "k", Fore.BLUE + "\u265A", position, team)
