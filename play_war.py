import deal_cards
import carddeck


def play_war():
    player_cards = deal_cards.deal_cards(2, 26, carddeck.standard_card_deck)[0]
    p_deck = player_cards["player0"]
    o_deck = player_cards["player1"]
    round_number = 0
    end_message = "time out"
    played_card_log = []
    win_state = False
    while round_number < 10000 and win_state is False:
        cards_in_play = []
        round_number += 1
        print("Round " + str(round_number))
        cards_in_play.append(p_deck[0])
        print("You played " + p_deck[0]["name"])
        cards_in_play.append(o_deck[0])
        print("Opponent played " + o_deck[0]["name"])
        p_deck = p_deck[1:]
        o_deck = o_deck[1:]
        if cards_in_play[0]["value"] == cards_in_play[1]["value"]:
            war_state = True
            while war_state is True:
                print("war!")
                if len(p_deck) < 3 or len(o_deck) < 3:
                    if len(p_deck) < 3 and len(o_deck) < 3:
                        end_message = "Tie game, both players ran out of cards"
                    if len(p_deck) < 3:
                        end_message = "You lose the game, you ran out of cards"
                    if len(o_deck) < 3:
                        end_message = "You win the game, opponent ran out of cards"
                    war_state = False
                    win_state = True
                else:
                    cards_in_play += p_deck[0:3]
                    for x in p_deck[0:3]:
                        print("You played " + x["name"])
                    cards_in_play += o_deck[0:3]
                    for x in o_deck[0:3]:
                        print("Opponent played " + x["name"])
                    p_deck = p_deck[3:]
                    o_deck = o_deck[3:]
                    if cards_in_play[-1]["value"] != cards_in_play[-4]["value"]:
                        if cards_in_play[-1]["value"] > cards_in_play[-4]["value"]:
                            print("Opponent won the war!")
                            o_deck = o_deck + cards_in_play
                        else:
                            print("You won the war!")
                            p_deck = p_deck + cards_in_play
                        war_state = False
        else:
            if cards_in_play[0]["value"] > cards_in_play[1]["value"]:
                p_deck = p_deck + cards_in_play
                print("you won the round!")
            else:
                o_deck = o_deck + cards_in_play
                print("your opponent won the round!")
        if len(p_deck) == 0:
            end_message = "you lost the game :("
            win_state = True
        if len(o_deck) == 0:
            end_message = "you win the game :)"
            win_state = True
        this_rounds_cards = []
        for x in cards_in_play:
            this_rounds_cards.append([x["name"]])
        played_card_log.append(this_rounds_cards)
        p_deck = deal_cards.deal_cards(1, len(p_deck), p_deck)[0]["player0"]
        o_deck = deal_cards.deal_cards(1, len(o_deck), o_deck)[0]["player0"]

    return (end_message)


print(play_war())
