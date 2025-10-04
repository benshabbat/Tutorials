class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof!"

dog1 = Dog("Buddy", "Golden Retriever")
print(dog1.bark())
print(dog1.name)
print(dog1.breed)

dog2 = Dog("Max", "Beagle")
print(dog2.bark())
print(dog2.name)
print(dog2.breed)