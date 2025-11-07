import random    


WEAPONS = ["axe", "sword", "knife"]

class Monster:
    def __init__(self, name, hp, type, speed , power , armor_rating , weapon =random.choice(WEAPONS) ):
        self.name = name
        self.hp = hp
        self.type = type
        self.speed = speed
        self.power = power
        self.armor_rating = armor_rating
        self.weapon = weapon
        self.turn = False
        self.roll = 0


    def speak(self):
        if self.type == "goblin":
            print(f"{self.name} the {self.type} Goblin says: Grrr!")
        else:     
            print(f"{self.name} the {self.type} Orc says: Grrr!")

    def attack(self, target):
        self.power *= 0.5 if self.weapon == "knife" else 1 if self.weapon == "sword" else 1.5 if self.weapon == "axe" else 1
        target.hp -= self.power + random.randint(1,6)
        if target.hp < 0:
            target.hp = 0
        self.speak()
        print(f"{self.name} attacks {target.name} for {self.power} damage!")
        print(f"{target.name} has {target.hp} HP left.")
    

    def run_away(self):
        self.speak()
        if self.type == "goblin":
            print(f"{self.name} the {self.type} Goblin runs away!")
        else:
            print(f"{self.name} the {self.type} Orc runs away!")
        return True
                
                