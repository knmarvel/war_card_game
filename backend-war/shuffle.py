import random
import json


with open("carddeck.json") as carddeckjson:
    carddeck = json.load(carddeckjson)


def shuffle():
    shuffled_cards = []
    used_ids = []
    while len(shuffled_cards) < 52:
        card_id = random.randint(0, 51)
        if card_id not in used_ids:
            used_ids.append(card_id)
            card = "card" + str(card_id)
            shuffled_cards.append([carddeck[card]])
    return shuffled_cards
