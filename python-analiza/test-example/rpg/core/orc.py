import random
from .monster import Monster

ORC= {"name": "Orc", "hp":50 ,"speed" : random.randint(0,5),"power":random.randint(10,15),"armor_rating":random.randint(2,8)}
class Orc(Monster):
    def __init__(self):
        super().__init__(ORC["name"],ORC["hp"],"orc",ORC["speed"],ORC["power"],ORC["armor_rating"])


    # def speak(self):
    #     print(f"{self.name} the {self.type} Orc says: Grrr!")

    # def attack(self, target):
    #     self.power *= 1.5 if self.weapon == "axe" else 1 if self.weapon == "sword" else 0.5 if self.weapon == "knife" else 1
    #     target.hp -= self.power
    #     if target.hp < 0:
    #         target.hp = 0
    #     self.speak()
    #     print(f"{self.name} attacks {target.name} for {self.power} damage!")
    #     print(f"{target.name} has {target.hp} HP left.")

    # def run_away(self):
    #     self.speak()
    #     print(f"{self.name} the {self.type} Orc runs away!")