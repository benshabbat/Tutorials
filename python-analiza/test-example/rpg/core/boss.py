from .orc import Orc

class Boss(Orc):
    def __init__(self):
        super().__init__()
        self.name = "Boss Orc"
        self.hp += 5
        self.power += 5
        self.armor_rating += 5
        self.speed += 5
        self.heal_limit = self.hp * 0.2


    def heal(self):
        self.hp += 30
        print(f"{self.name} heals for 30 HP! Current HP: {self.hp}")
            
    def attack(self, target):
        if self.hp <= self.heal_limit:
            self.heal()        
        else:
            super().attack(target)