import random
import json


with open("carddeck.json") as carddeckjson:
    carddeck = json.load(carddeckjson)


def shuffle():
    shuffled_cards = []
    for x in range(52):
        card = "card" + str(random.randint(0, 51))
        if card not in shuffled_cards:
            shuffled_cards.append(carddeck[card])
    return shuffled_cards
