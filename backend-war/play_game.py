import deal_cards


def play_war():
    player_cards = deal_cards.deal_cards(2, 26)
    p_deck = player_cards["player0"]
    o_deck = player_cards["player1"]
    round_number = 0
    while round_number < 1000:
        played_cards = []
        print("You have " + str(len(p_deck)) + " cards remaining.")
        print("You play the " + p_deck[0]["name"])
        played_cards = [p_deck[0]]
        p_deck = p_deck[1:]
        print("Opponent plays the " + o_deck[0]["name"])
        played_cards = played_cards + [o_deck[0]]
        o_deck = o_deck[1:]
        round_number += 1
        if played_cards[0]["value"] == played_cards[1]["value"]:
            war_state = True
            while war_state is True:
                print("WAR!")
                if len(p_deck) < 3:
                    return ("You ran out of cards! You lose. :( " + str(round_number))
                if len(o_deck) < 3:
                    return ("Your opponent ran out of cards! You win! :) " + str(round_number))
                print("You play the " + p_deck[0]["name"] + ", " + p_deck[1]["name"] + ", and the " + p_deck[2]["name"])
                played_cards = played_cards + p_deck[:3]
                p_deck = p_deck[3:]
                print("Your opponent plays the " + o_deck[0]["name"] + ", " + o_deck[1]["name"] + ", and the " + o_deck[2]["name"])
                played_cards = played_cards + o_deck[:3]
                o_deck = o_deck[3:]
                if played_cards[-1]["value"] != played_cards[-4]["value"]:
                    if played_cards[-1]["value"] > played_cards[-4]["value"]:
                        print("Your opponent captured all " + str(len(played_cards)) + " cards!")
                        o_deck = o_deck + played_cards
                    else:
                        print("You captured all " + str(len(played_cards)) + " cards!")
                        p_deck = p_deck + played_cards
                    war_state = False
        else:
            if played_cards[0]["value"] > played_cards[1]["value"]:
                print("You win this battle.")
                p_deck = p_deck + played_cards
            else:
                print("You have lost this battle.")
                o_deck = o_deck + played_cards
            if len(p_deck) == 52:
                return("Your opponent ran out of cards! You win! :) " + str(round_number))
            if len(o_deck) == 52:
                return("You ran out of cards! You lose :( " + str(round_number))
    return ("sorry, timed out with ", len(p_deck), "remaining")


print(play_war())
