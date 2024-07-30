class Piece:
    name: str
    id: str
    icon: str
    position: list
    team: int = 0
    pos_moves= []
    def __init__(self, name, id, icon, position, team):
        self.name = name
        self.id = id
        self.icon = icon
        self.position = position
        self.team = team
    
    