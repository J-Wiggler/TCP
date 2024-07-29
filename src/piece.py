class Piece:
    name: str
    id: str
    icon: str
    position: list
    team: int
    def __init__(self, name, id, icon, position, team):
        self.name = name
        self.id = id
        self.icon = icon
        self.position = position
        team = team