import shuffle


def deal_cards(player_count, cards_in_hand):
    if player_count * cards_in_hand > 52:
        return "error--number of cards requested is too high"
    else:
        shuffled_cards = shuffle.shuffle()
        player_hands = {}
        top_of_deck = 0
        for x in list(range(player_count)):
            player_hands["player" + str(x)] = []
        for card in list(range(cards_in_hand)):
            for x in player_hands:
                player_hands[x] = player_hands[x] + shuffled_cards[top_of_deck]
                top_of_deck += 1
        return player_hands
