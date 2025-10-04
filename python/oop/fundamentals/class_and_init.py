class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return print(f"{self.name} says woof!")

dog1 = Dog("Buddy", "Golden Retriever")
dog1.bark()
print(dog1.name)
print(dog1.breed)

dog2 = Dog("Max", "Beagle")
dog2.bark()
print(dog2.name)
print(dog2.breed)