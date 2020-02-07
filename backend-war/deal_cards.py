import shuffle
import top_card


def deal_cards(player_count, cards_in_hand):
    shuffled_cards = shuffle.shuffle()
    player_hands = []
    for x in range[:player_count]:
        player_hands.append("player" + str(x))
    for card in cards_in_hand:
        for x in player_hands:
            
