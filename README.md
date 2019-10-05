# new_version_freecell_python
A variation of the Freecell game in pyhton.


About the game:

We have cascades to hold all the cards. Player can move only the top card in each cascade.
The goal is to move cards to the foundations with each foundation designated to one suit out of hearts, clubs, spades and diamonds. It should be arranged in the order A,2,3,4,5,6,7,8,9,10,J ,Q, K.
If the player is successful in moving all the four suits in the above order to the foundations, he wins the game.
Cells are the top left cells which can hold only one card at a time. There are only 4 cells. Player cannot move card to the cells when they are full.
Player cannot choose a card from the middle of the cascade to move.
First, we ask the user to pick a card.
The picked card will be inspected to check if it can be moved. 
If the card can be moved, we ask the player to choose where he wants to move the card to. 
If the player wants to move it to the cascade, he can only move it if the top of the cascade has a card one value higher than the card to be moved and of opposite color (Diamonds and hearts are red and clubs and spades are black)
If the player wants to move the card to the foundation, it can be placed only in the increasing order of the value (one value higher) of the same suit. So, the first card to be moved should be an ace. Whichever foundation is empty, will be assigned to store the card (Ace goes first). 
If the player wants to move to a cell, there are no restrictions on the kind of card he can place in cells except cells shouldn’t be full. 
