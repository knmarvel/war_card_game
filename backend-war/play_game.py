import deal_cards


def play_war():
    player_cards = deal_cards.deal_cards(2, 26)
    p_deck = player_cards["player0"]
    o_deck = player_cards["player1"]
    round_number = 0
    end_message = "time out"
    played_card_log = []
    win_state = False
    while round_number < 100000000 and win_state is False:
        if round_number % 100 == 0:
            card = p_deck[0]
            p_deck = p_deck[1:]
            p_deck.append(card)
        round_number += 1
        cards_in_play = [p_deck[0]] + [o_deck[0]]
        p_deck = p_deck[1:]
        o_deck = o_deck[1:]
        if cards_in_play[0]["value"] == cards_in_play[1]["value"]:
            war_state = True
            while war_state is True:
                if len(p_deck) < 3 or len(o_deck) < 3:
                    if len(p_deck) < 3 and len(o_deck) < 3:
                        end_message = "Tie game, both players ran out of cards at round " + str(round_number)
                    if len(p_deck) < 3:
                        end_message = "You lose, you ran out of cards"
                    if len(o_deck) < 3:
                        end_message = "You win, opponent ran out of cards"
                    war_state = False
                    win_state = True
                else:
                    cards_in_play += [p_deck[0]] + [p_deck[1]] + [p_deck[2]]
                    cards_in_play += [o_deck[0]] + [o_deck[1]] + [o_deck[2]]
                    p_deck = p_deck[3:]
                    o_deck = o_deck[3:]
                    if cards_in_play[-1]["value"] != cards_in_play[-4]["value"]:
                        if cards_in_play[-1]["value"] > cards_in_play[-4]["value"]:
                            o_deck = o_deck + cards_in_play
                        else:
                            p_deck = p_deck + cards_in_play
                        war_state = False
        else:
            if cards_in_play[0]["value"] > cards_in_play[1]["value"]:
                p_deck = p_deck + cards_in_play
            else:
                o_deck = o_deck + cards_in_play
        if len(p_deck) == 0:
            end_message = "you lose :("
            win_state = True
        if len(o_deck) == 0:
            end_message = "you win :)"
            win_state = True
        this_rounds_cards = []
        for x in cards_in_play:
            this_rounds_cards.append([x["name"]])
        played_card_log.append(this_rounds_cards)
    return (end_message + " at round number " + str(round_number))


print(play_war())
