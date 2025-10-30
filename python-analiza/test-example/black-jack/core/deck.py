import random

def build_standard_deck() -> list[dict]:

    suites = ['H', 'D', 'C', 'S']
    ranks = [
        '2', '3', '4', '5', '6', '7', '8', '9', '10',
        'J', 'Q', 'K', 'A'
    ]

    deck = [{'rank': rank, 'suite': suite} for suite in suites for rank in ranks]
    return deck


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    deck_size = len(deck)
    for _ in range(swaps):       
        i = random.randint(0, deck_size - 1)
        suite_at_i = deck[i]["suite"]
        valid_j = False
        j = -1
        while not valid_j:
            j = random.randint(0, deck_size - 1)
            if i == j:
                continue
            if suite_at_i == 'H':
                if j % 5 == 0:
                    valid_j = True
            elif suite_at_i == 'C':
                if j % 3 == 0:
                    valid_j = True
            elif suite_at_i == 'D':
                if j % 2 == 0:
                    valid_j = True
            elif suite_at_i == 'S':
                if j % 7 == 0:
                    valid_j = True
        
        deck[i], deck[j] = deck[j], deck[i]
    
    return deck
