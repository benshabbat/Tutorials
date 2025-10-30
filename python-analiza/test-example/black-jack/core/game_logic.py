from core.player_io import ask_player_action


def calculate_hand_value(hand: list[dict]) -> int:
    value = 0
    aces = 0
    for card in hand:
        rank = card['rank']
        if rank in ['J', 'Q', 'K']:
            value += 10
        elif rank == 'A':
            aces += 1
            value += 11  # Initially count Ace as 11
        else:
            value += int(rank)

        while value > 21 and aces:
            value -= 10  # Convert an Ace from 11 to 1
            aces -= 1
    return value

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player['hand'] = [deck.pop(), deck.pop()]
    dealer['hand'] = [deck.pop(), deck.pop()]

    print(f"Cards left in deck: {len(deck)}")
    print(f"Player's hand: {player['hand']}, value: {calculate_hand_value(player['hand'])}")
    print(f"Dealer's hand: {dealer['hand']}, value: {calculate_hand_value(dealer['hand'])}")
    
def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while calculate_hand_value(dealer['hand']) < 17:
        dealer['hand'].append(deck.pop())
        print(f"Dealer hits: {dealer['hand']}, value: {calculate_hand_value(dealer['hand'])}")
        if calculate_hand_value(dealer['hand']) > 21:
            print("Dealer busts!")
            return False
    print("Dealer stands.")
    return True

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck,player,dealer)
    val_player = calculate_hand_value(player['hand'])
    while val_player<=21:
        req = ask_player_action()
        if req == "H":
            card = deck.pop()
            print(card)
            player['hand'].append(card)
            val_player = calculate_hand_value(player['hand'])
            print(f"your val {val_player} ")
            if val_player >21:
                print(f"player lost {val_player} above 21")
                break
                       
        if req == "S" and dealer_play(deck,dealer):
            print(f"player pressed S for stands his value of cards {val_player} ")
            val_dealer =calculate_hand_value(dealer["hand"])
            if val_dealer> val_player:
                print(f"dealer won the value of his card {val_dealer} > {val_player} : value of card to player")
            elif val_dealer < val_player:
                print(f"player won the value of his card {val_player} > {val_dealer} : value of card to player") 
            else:
                print("TIE")    
            break    