class Cricketer:
    def __init__(self, name, team):
        self.name = name
        self.team = team

    def play_role(self):
        return "Plays cricket for the team"

class Captain(Cricketer):
    def __init__(self, name, team, trophies):
        super().__init__(name, team)
        self.trophies = trophies

    def play_role(self):
        return f"Leads {self.team} and has won {self.trophies} trophies"

class Bowler(Cricketer):
    def play_role(self):
        return "Specializes in taking wickets"

rohit = Captain("Rohit Sharma", "India", 6)
bumrah = Bowler("Jasprit Bumrah", "India")

players = [rohit, bumrah]

for player in players:
    print(f"{player.name}: {player.play_role()}")