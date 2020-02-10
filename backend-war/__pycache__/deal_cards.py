import shuffle


def deal_cards(player_count, cards_in_hand, deck):
    if player_count * cards_in_hand > len(deck):
        return "error--number of cards requested is too high"
    else:
        deck = shuffle.shuffle(deck)
        player_hands = {}
        for x in list(range(player_count)):
            player_hands["player" + str(x)] = []
        for card in list(range(cards_in_hand)):
            for x in player_hands:
                player_hands[x] = player_hands[x] + deck[0]
                deck = deck[1:]
        return ((player_hands), (deck))
