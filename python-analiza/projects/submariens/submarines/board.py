def matrix_generator(size: int, fill: int | bool = 0) -> list[list[int | bool]]:
    return [[fill for _ in range(size)] for _ in range(size)]


def create_matrix(size: int, fill: int = 0) -> list[list[int]]:
    return matrix_generator(size, fill)
    # list_matrix = []
    # for _ in range(size):
    #     row = []
    #     for _ in range(size):
    #         row.append(fill)
    #     list_matrix.append(row)

    # return list_matrix


    # return [[fill for _ in range(size)] for _ in range(size)]


def create_bool_matrix(size: int, fill: bool = False) -> list[list[bool]]:
    return matrix_generator(size, fill)
    # list_matrix = []
    # for _ in range(size):
    #     row = []
    #     for _ in range(size):
    #         row.append(fill)
    #     list_matrix.append(row)

    # return list_matrix




def print_matrix(matrix_board: list[list[int]]) -> None:
    for row in matrix_board:
        for value in row:
            print(value, end=" ")
        print()
    # for row in matrix_board:
    #     print(" ".join(str(cell) for cell in row))



def in_bounds(size: int, x: int, y: int) -> bool:
    return 0 <= x < size and 0 <= y < size


def count_remaining_ships(ships: list[list[int]], shots: list[list[bool]]) -> int:
    remaining_ships = 0
    for i in range(len(ships)):
        for j in range(len(ships[i])):
            if ships[i][j] == 1 and not shots[i][j]:
                remaining_ships += 1
    return remaining_ships


def render_public(ships: list[list[int]], shots: list[list[bool]]) -> str:
    size = len(ships)
    board_representation = ""
    for i in range(size):
        for j in range(size):
            if shots[i][j]:
                if ships[i][j] == 1:
                    board_representation += "V"  # Hit
                else:
                    board_representation += "X"  # Miss
            else:
                board_representation += "O"  # Unshot
        board_representation += "\n"
    return board_representation


def render_reveal(ships: list[list[int]], shots: list[list[bool]]) -> str:
    size = len(ships)
    board_representation = ""
    for i in range(size):
        for j in range(size):
            if ships[i][j] == 1:
                board_representation += "1"  # Ship
            elif shots[i][j]:
                board_representation += "X"  # Miss
            else:
                board_representation += "O"  # Empty
        board_representation += "\n"
    return board_representation




