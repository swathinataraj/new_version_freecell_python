import random
from Card import Card


class Deck:
    def __init__(self, value_start, value_end, number_of_suits, new_suit = None):
        #initializing values required by Deck class
        self.new_deck = []
        self.start = value_start
        self.end = value_end
        self.n = number_of_suits
        # Note that because rank is 0-indexed but when displaying, it should be 1-indexed, it is necessary
        # to add one. Thus, 12 actually represents King (not Queen) and 0 represents Ace.
        # suits are H - Heart , S - Spade, D - Diamond, C - Clubs

        self.suitname = ["H", "S", "D", "C"]
        if self.n <= 4:
            # random.sample takes list and number of items to randomly choose from as agruments
            self.suits = random.sample(self.suitname,self.n)
        else:
            self.suitname.extend(new_suit)
            self.suits = random.sample(self.suitname, self.n)
        #creating Card class instance will help us get the card in rank:suit format
        #Then appending the card to new_deck class to have required number of cards with chosen number of suits
        for j in range(self.start,self.end + 1):
            for symbol in self.suits:
                self.new_deck.append(str(Card(j,symbol)))


    def __str__(self):
        #To display all the cards inside the generated deck
        new_str = ""
        for item in self.new_deck:
            new_str += str(item) + "   "
        return new_str

    # shuffle works using no extra code to shuffle the deck
    def shuffle_deck(self):
        random.shuffle(self.new_deck)
        return str(self.new_deck)

    # adding card to the deck
    def add_card(self, card):
        # check if card doesnt already exist in the deck
        if card not in self.new_deck:
            # append the card to deck if doesn't already exist'
            self.new_deck.append(card)
        else:
            print("cannot add the card. It already exists")
        print(self.new_deck)

    #drawing the card at the top of the deck and returning the card
    def draw_card(self):
        length = len(self.new_deck)
        get_card = ""
        if length != 0:
            get_card = self.new_deck[-1]
            #making sure we delete the top card from deck after drawing it
            del self.new_deck[-1]
        return get_card

def main():
    #instantiating object for Deck class
    additional_suits = []
    num = int(input("Enter the number of suits: "))
    if num <= 4:
        deck_obj = Deck(1,13,num)
    else:
        new_suit = raw_input("Enter a symbol for new suit: ")
        for i in range(num + 1):
            additional_suits.append(new_suit)
        deck_obj = Deck(1,13,num,additional_suits)
    print deck_obj
    deck_obj.shuffle_deck()

if __name__ == "__main__":
    main()


