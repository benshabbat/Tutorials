import random
from .monster import Monster

GOBLIN= {"name": "Goblin", "hp":20 , "speed" : random.randint(5,10),"power":random.randint(5,10),"armor_rating":1}

class Goblin(Monster):
    def __init__(self):
        super().__init__(GOBLIN["name"],GOBLIN["hp"],"goblin",GOBLIN["speed"],GOBLIN["power"],GOBLIN["armor_rating"])

    # def speak(self):
    #     print(f"{self.name} the {self.type} Goblin says: Grrr!")

    # def attack(self, target):
    #     self.power *= 0.5 if self.weapon == "knife" else 1 if self.weapon == "sword" else 1.5 if self.weapon == "axe" else 1
    #     target.hp -= self.power
    #     if target.hp < 0:
    #         target.hp = 0
    #     self.speak()
    #     print(f"{self.name} attacks {target.name} for {self.power} damage!")
    #     print(f"{target.name} has {target.hp} HP left.")
    

    # def run_away(self):
    #     self.speak()
    #     print(f"{self.name} the {self.type} Goblin runs away!")