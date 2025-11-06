import random


PROFESSIONS = ["healing","warrior"]

class Player:
    def __init__(self, name, hp=50,speed = random.randint(5,10),power = random.randint(5,10),armor_rating = random.randint(5,15) ,profession = random.choice(PROFESSIONS)):
        self.name = name
        self.hp = hp + 10 if profession == "healing" else hp
        self.speed = speed
        self.power = power + 2 if profession == "warrior" else power
        self.armor_rating = armor_rating
        self.profession = profession
        self.turn = False
        self.roll = 0
        
        
    def speak(self):
        print(f"{self.name} says: Hello! I am a {self.profession}.")
        
    def attack(self, target):
        target.hp -= self.power
        if target.hp < 0:
            target.hp = 0
        self.speak()
        print(f"{self.name} attacks {target.name} for {self.power} damage!")
        print(f"{target.name} has {target.hp} HP left.")

    def run_away(self):
        self.speak()
        print(f"{self.name} runs away from the battle!")