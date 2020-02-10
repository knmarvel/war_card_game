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
In the backend-war directory, you can find the following files:

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




This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts--FRONT END

Kano's note: the front end of this project is just a practice for myself to deploy both at the same time. 
In the project directory, you can run:

### `npm start`

Runs the app in the development mode.<br />
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br />
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.<br />
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.<br />
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.<br />
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (Webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: https://facebook.github.io/create-react-app/docs/code-splitting

### Analyzing the Bundle Size

This section has moved here: https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size

### Making a Progressive Web App

This section has moved here: https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app

### Advanced Configuration

This section has moved here: https://facebook.github.io/create-react-app/docs/advanced-configuration

### Deployment

This section has moved here: https://facebook.github.io/create-react-app/docs/deployment

### `npm run build` fails to minify

This section has moved here: https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify
