import shuffle


shuffled_cards = shuffle.shuffle()


def pick_card(num):
    return shuffled_cards[num]["name"]
