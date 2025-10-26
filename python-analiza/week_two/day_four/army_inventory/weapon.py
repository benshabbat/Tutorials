class Weapon:
    total_weapons = 0
    def __init__(self, name, ammo):
        self.name = name
        self.ammo = ammo
        Weapon.total_weapons += 1

    def attack(self):
        return f"{self.name} attacks with {self.ammo} ammo!"

    @classmethod
    def get_total_weapons(cls):
        return cls.total_weapons
    
    
sword = Weapon("Sword", 0)
bow = Weapon("Bow", 30)
print(sword.attack())  # Output: Sword attacks with 0 ammo!
print(bow.attack())    # Output: Bow attacks with 30 ammo!
print(Weapon.get_total_weapons())  # Output: 2