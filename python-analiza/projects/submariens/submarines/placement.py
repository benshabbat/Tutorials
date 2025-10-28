import random

def place_random_ships(ships: list[list[int]], n: int) -> None:
    size = len(ships)
    placed_ships = 0
    while placed_ships < n:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        if ships[x][y] == 0:
            ships[x][y] = 1
            placed_ships += 1
            
            