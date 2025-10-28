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


print_matrix(create_matrix(5))
print_matrix(create_bool_matrix(4))


