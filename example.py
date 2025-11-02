import random


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
alice = Person("Alice", 30)
hanan = Person("Hanan", 30)
print(alice.greet()) 

# Person(alice)
# alice = Person("Alice", 30)

Person.greet(alice)
Person.greet(hanan)


rng =random
random.randint(3,8)

rng.randint(3,98)