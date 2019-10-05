import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        # For suit ordering: 0=red heart, 1=black clubs, 2=red diamonds, 3=black spades
        self.suit = suit

    def __str__(self):

        #to return card we use the format (rank:suit) For example, 12:H (indicating Queen of Hearts)
        card_string = ""
        card_string += str(self.rank) + ":" +str(self.suit)
        return card_string


test = Card(13,0)
