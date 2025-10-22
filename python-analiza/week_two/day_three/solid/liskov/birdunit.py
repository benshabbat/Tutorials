class BirdUnit:
    def fly(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Drone(BirdUnit):
    def fly(self):
        return "Flying with propellers!"
    
class TankUnit(BirdUnit):
    def fly(self):
        raise Exception("TankUnit cannot fly!")
    
    
    
dron = Drone()
print(dron.fly())  # Output: Flying with propellers!
tank = TankUnit()
print(tank.fly())  # This will raise an Exception: TankUnit cannot fly!     



## refcatonclass BirdUnit:

class Flyunit:
    def fly(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class GroundUnit:
    def drive(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    
class Drone(Flyunit):
    def fly(self):
        return "Flying with propellers!"

class TankUnit(GroundUnit):
    def drive(self):
        return "Driving on tracks!"