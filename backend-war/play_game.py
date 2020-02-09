import deal_cards


def play_war():
    player_cards = deal_cards.deal_cards(2, 2)
    p_deck = player_cards["player0"]
    o_deck = player_cards["player1"]
    round_number = 0
    end_of_game = False
    while end_of_game is False:
        while round_number < 1000:
            cards_in_play = [p_deck[0]] + [o_deck[0]]
            p_deck = p_deck[1:]
            o_deck = o_deck[1:]
            if cards_in_play[0]["value"] == cards_in_play[1]["value"]:
                print("WAR")

            if cards_in_play[0]["value"] > cards_in_play[1]["value"]:
                p_deck = p_deck + cards_in_play


print(play_war())
