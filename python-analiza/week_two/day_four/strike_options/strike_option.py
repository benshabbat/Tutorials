class StrikeOption:
    def __init__(self, name:str,ammo:int):
        self.name = name
        self.ammo = ammo
    def strike(self):
        if self.ammo > 0:
            self.ammo -= 1
            return f"Strike executed with {self.name}. Remaining ammo: {self.ammo}"
        else:
            return f"No ammo left for {self.name}!"
        
        
class Tank(StrikeOption):
    def strike(self):
        return super().strike() + " Tank shell fired!"  
    
class Drone(StrikeOption):
    def strike(self):
        return super().strike() + " Drone missile launched!"    