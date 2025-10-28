import random
from submarines.placement import place_random_ships

def init_game(size: int, n_ships: int, max_shots: int, *, rng: random.Random | None =
              None) -> dict:
    if rng is None:
        rng = random.Random()
    ships = [[0 for _ in range(size)] for _ in range(size)]
    shots = [[False for _ in range(size)] for _ in range(size)]
    place_random_ships(ships, n_ships)
    return {
        "size": size,
        "ships": ships,
        "shots": shots,
        "n_ships": n_ships,
        "max_shots": max_shots,
        "shots_used": 0,
    }


def shoot(state: dict, x: int, y: int) -> tuple[bool, str]:
    size = state["size"]
    ships = state["ships"]
    shots = state["shots"]
    max_shots = state["max_shots"]
    shots_used = state["shots_used"]

    if not (0 <= x < size and 0 <= y < size):
        return False, "Shot out of bounds!"

    if shots[x][y]:
        return False, "Position already shot at!"

    if shots_used >= max_shots:
        return False, "No shots remaining!"

    shots[x][y] = True
    state["shots_used"] += 1

    if ships[x][y] == 1:
        return True, "Hit!"
    else:
        return False, "Miss!"
    
    
def is_won(state: dict) -> bool:
    ships = state["ships"]
    shots = state["shots"]
    for i in range(len(ships)):
        for j in range(len(ships[i])):
            if ships[i][j] == 1 and not shots[i][j]:
                return False
    return True    

def is_lost(state: dict) -> bool:
    return state["shots_used"] >= state["max_shots"] and not is_won(state)