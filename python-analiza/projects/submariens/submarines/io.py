from .board import render_public, count_remaining_ships, print_matrix ,render_reveal

def parse_coords(raw: str, *, one_based: bool = True) -> tuple[int, int] | None:
    input_parts = raw.split(",")
    if len(input_parts) != 2:
        return None

    x_str, y_str = input_parts
    try:
        x = int(x_str.strip())
        y = int(y_str.strip())
    except ValueError:
        return None

    if one_based:
        x -= 1
        y -= 1

    return x, y


def print_status(state: dict) -> None:

    ships = state["ships"]
    shots = state["shots"]
    n_ships = state["n_ships"]
    max_shots = state["max_shots"]
    shots_used = state["shots_used"]

    print("Current Board:")
    print_matrix(ships)
    print("\nPublic View:")
    print(render_public(ships, shots))
    remaining_ships = count_remaining_ships(ships, shots)
    shots_left = max_shots - shots_used
    print(f"Remaining Ships: {remaining_ships} / {n_ships}")
    print(f"Shots Left: {shots_left} / {max_shots}")
    
    
def print_end(state: dict, won: bool) -> None:
    ships = state["ships"]
    shots = state["shots"]
    print("\nFinal Board Reveal:")
    print(render_reveal(ships, shots))
    if won:
        print("Congratulations! You've sunk all the ships!")
    else:    
        print("Game Over! You've used all your shots.")