class Dog:
    def __init__(self, name, age, owner):
        self.name = name
        self.age = age
        self.owner = owner

    def bark(self):
        return f"{self.name} says woof!"

    def get_age(self):
        return self.age
    
    


class Owner:
    def __init__(self, name):
        self.name = name
        self.dogs = []

    def add_dog(self, dog):
        self.dogs.append(dog)

    def list_dogs(self):
        for dog in self.dogs:
            print(f"{dog.name}, Age: {dog.age}")

# Create owners
owner1 = Owner("Alice")
owner2 = Owner("Bob")

# Create dogs and assign them to owners
dog1 = Dog("Buddy", 3, owner1)
dog2 = Dog("Max", 5, owner2)
dog3 = Dog("Bella", 2, owner1)

# Add dogs to owners
owner1.add_dog(dog1)
owner1.add_dog(dog3)
owner2.add_dog(dog2)
# List dogs for each owner
print(f"{owner1.name}'s dogs:")
owner1.list_dogs()

print(f"{owner2.name}'s dogs:")
owner2.list_dogs()  

# Demonstrate dog behaviors
print(dog1.bark())
print(f"{dog1.name} is {dog1.get_age()} years old.")
print(dog2.bark())
print(f"{dog2.name} is {dog2.get_age()} years old.")
print(dog3.bark())
print(f"{dog3.name} is {dog3.get_age()} years old.")

print(dog1.owner.name)  # Output: Alice 
print(dog2.owner.name)  # Output: Bob
print(dog3.owner.name)  # Output: Alice        