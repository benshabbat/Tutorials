class Soldier:
    def __init__(self, name, rank, weapon):
        self.name = name
        self.rank = rank
        self.weapon = weapon

    def __str__(self):
        return f"{self.rank} {self.name} armed with a {self.weapon}"
    
    def report(self):
        return f"Soldier Report: {self.rank} {self.name}, Weapon: {self.weapon}"