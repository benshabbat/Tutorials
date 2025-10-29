from submarines.game import init_game , shoot, is_won, is_lost, shots_left
from submarines.io import parse_coords


def play(size: int = 6, n_ships: int = 6, max_shots: int = 10, *, one_based: bool = True) ->None:
    game = init_game(size, n_ships, max_shots)
    print("Game initialized!")
    
    while shots_left(game) > 0:
        raw = input("Enter coordinates to shoot (e.g., '3,4'): ")
        coords = parse_coords(raw, one_based=one_based)
        if coords is None:
            print("Invalid input. Please enter coordinates in the format 'x,y'.")
            continue
        x, y = coords
        success, message = shoot(game, x, y)
        print(message)
        
        if is_won(game):
            print("Congratulations! You've sunk all the ships!")
            break
        elif is_lost(game):
            print("Game over! You've used all your shots.")
            break
        else:
            print(f"Shots left: {shots_left(game)}")
            
            
            
if __name__ == "__main__":
    play()            