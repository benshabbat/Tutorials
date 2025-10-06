# Cross-Module Imports
#  Create two modules, a.py and b.py. In a.py, define a 
#  function that calls a function
#  from b.py. Run them together.

from b import say_hello
def greet(name):
    return say_hello(name)

print(greet("Alice"))

if __name__ == "__main__":
    print(greet("Alice"))
    print(greet("Bob"))
    print(greet("Charlie"))