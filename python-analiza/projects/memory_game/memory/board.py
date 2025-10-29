import random

def create_board(size: int, symbols: list[str], *, rng: random.Random | None = None) -> dict:
    if rng is None:
        rng = random.Random()
    board = {}
    for i in range(size):
        for j in range(size):
            board[(i, j)] = rng.choice(symbols)
    return board



board = create_board(4, ['A', 'B', 'C', 'D'], rng=random.Random(42))
