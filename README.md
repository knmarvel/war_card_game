![Kano's logo](https://knmarvel.github.io/kanoaslogo.png)


# War! The Classic Card Game
War setup:
    -Objective: don't run out of cards
    -requires:
        2 players
        standard deck of 52 cards, prepared as:
            -shuffled into random order
            -every other card from the top of the deck dealt to each player so each player has a stack of 26 cards
    -game play:
        First player flips their top card.
        Second player flips their top card.
        Whichever player has the higher card value wins the round.
        If the players' cards both have the same value, war is declared.
            First player flips their top three cards.
            Second player flips their top three cards. 
            Whichever player has the higher card value on the third card wins the round.
            If the players' third cards both have the same value, the process is repeated until a round winner is found
        At the end of the round, the winner shuffles all cards played during the round into their deck. 
    -winning:
        A player wins if the other player has no cards in their hand.
        If both players run out of cards on the same round (can only happen during a war), it's a tie game.
        

        

## Available Scripts--BACK END

### 'python play_war.py'
This file includes a function, play_war(), that takes no parameters. It iterates a 52 standard card deck through a game of War (rules above). Each round, the cards played are printed and the winner of the round is printed. The program ends when a player wins the game or when the number of rounds played reaches 10,000 as the game could conceivably be infinite. 

## Helper files--BACK END


### carddeck.py
This file includes the variable standard_card_deck, a list of dictionaries that represents a standard deck of 52 cards. Nothing will be returned fro

### shuffle.py
This file includes a function, shuffle(), that takes one parameter (a list that includes the cards to shuffle) and returns that list of cards arranged randomly.

### dealcards.py
This program includes a function, deal_cards(), that takes three parameters:
    -the number of players
    -the number of cards per player
    -the deck to deal
It calls the shuffle function on the deck, and returns a dictionary with players/leftover decks as the keys and the cards in their hands as dictionaries inside an array. If the number of cards required for the deal is greater than the number of cards in the deck, returns an error. 
