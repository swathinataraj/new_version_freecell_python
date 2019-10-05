from stack import Stack
from Deck import Deck

#This is the actual game class where all the rules of Freeell are implemented
class NotFreecell:
    def __init__(self, new_deck):
        #gaps variable is just a representation on the screen for cells and foundations
        #foundations are a list of 4 stacks
        #cascades are list of 8 lists
        # cells are list of 4 strings
        self.deck = new_deck
        self.gaps = ['____','____','____','____','[  ]','[  ]','[  ]','[  ]']
        self.foundation_stacks = [Stack(),Stack(),Stack(),Stack()]
        self.cascades = [[], [], [], [], [], [], [], []]
        self.cells = [""] * 4
        #To distribute cards into cascades we draw top card from deck one at a time and place it in 8 cascades one after another
        for i in range(7):
            for j in range(8):
                card_drawn = self.deck.draw_card()
                #make sure card drawn is not empty before appending
                if card_drawn != '':
                    self.cascades[j].append(card_drawn)

    #To display the cells, foundations and cascades in required manner
    def __str__(self):

        another_string = "\n"
        for slot in self.gaps:
            another_string += slot + "   "
        another_string += "\n\n"
        max_length = len(max(self.cascades, key=len))

        for i in range(max_length):
            for item in self.cascades:
                if len(item) >= i + 1:
                    #for neat display of cascades
                    another_string += '{0:>4}'.format(item[i]) + "   "
                else:
                    another_string += "       "
            another_string += "\n"
        # we need to display to the player actual card face(A,J,Q,K) rather than the values (1,11,12,13).. So replace accordingly
        return another_string.replace("13"," K").replace("12"," Q").replace("11"," J").replace(" 1:"," A:")


    #validating the card picked by the user to see if he can move the card or not. Sometimes, when the card is in the middle of a pile,
    #he cannot move it. When the player chooses a card to move, we also inspect if the card is in cell or foundation or cascade which is named
    #origin. When origin = s we are checking if the card is at cascade, similarly origin = c for cells and origin = f for foundation.
    # on successful move, we should delete the card from origin
    def validate_pick_card(self, check_card):
        sorry_string = "Sorry.. Wrong choice.. Choose another card"
        found_at = None
        count = 3
        for i in range(len(self.cascades)):
            for j in range(len(self.cascades[i])):
                cascade_len = len(self.cascades[i])
                if self.cascades[i][j] == check_card:
                    if cascade_len == j + 1:
                        origin = 's'
                        return self.move_to_place(check_card,i,origin)
        while found_at == None:
            for i in range(4):
                if self.cells[i] == check_card:
                    origin = 'c'
                    return self.move_to_place(check_card,i,origin)
                    break

            for stack in self.foundation_stacks:
                count += 1
                if not stack.is_empty():
                    if stack.peek() == check_card:
                        origin = 'f'
                        return self.move_to_place(check_card,count,origin)
                        break
            break

        if found_at == None:
            print sorry_string
            return 'A'


    # If the user choses to move the card to a cascade, we need to check if it can be moved to the chosen cascade. Card can be placed in cascade only
    #on top of opposite colour and with value one lesser than the top card. Eg, 4 of spades and be placed on 5 of hearts. 4 of spades cannot be
    #moved on 5 of clubs(same colour) or 4 of spades cannot be moved on 6 of diamonds(it should be only one lesser than top most card of the cascade
    #When origin = s we are checking if the card is at cascade, similarly origin = c for cells and origin = f for foundation.
    # on successful move, we should delete the card from origin
    def inspect_cascade(self,chosen_card,i,place):
        flag = 0
        while not flag:
            #player chooses which cascade to move to
            move_to = input("Choose a cascade from 1-8: ")
            flag = 1
            move_to -= 1
            len_of_cas = len(self.cascades[move_to]) - 1
            split_rank, split_suite = chosen_card.split(':',1)
            inspect_rank, inspect_suite = self.cascades[move_to][len_of_cas].split(":",1)
            if (inspect_suite in ['H','D'] and split_suite in ['S','C']) or (inspect_suite in ['S','C'] and split_suite in ['H','D']):
                    if int(inspect_rank) == int(split_rank) + 1:
                        self.cascades[move_to].append(chosen_card)
                        if place == 's':
                            del self.cascades[i][-1]
                        elif place == 'c':
                            self.cells[i] = ""
                            self.gaps[i] = "____"

                        else:
                            del self.foundation_stacks[i]
                    else:
                        print("Cannot move!")
            else:
                print("Cannot move!")
        return self.cascades


    #If the player wants to move the card to a foundation, we inspect if it can be moved. The first empty foundation is chosen to place the card.
    #specific foundation is designated to a specific foundation. It should be arranged in the stack from Ace to King order. Cards cannot be moved between
    #foundations. When origin = s we are checking if the card is at cascade, similarly origin = c for cells and origin = f for foundation.
    #on successful move, we should delete the card from origin
    def inspect_foundation(self,chosen_card, pos,o):
        chosen_card_rank, chosen_card_suit = chosen_card.split(':')
        count = 3
        flag = 0
        for stack in self.foundation_stacks:
            count += 1
            if chosen_card_rank == '1':
                if stack.is_empty():
                    stack.push(chosen_card)
                    break
            else:
                if not stack.is_empty():
                    l, r = stack.peek().split(':')
                    if r == chosen_card_suit:
                        if int(chosen_card_rank) == int(l) + 1:
                            stack.push(chosen_card)
                        else:
                            print("Cannot move!")
                    else:
                        print("Cannot move!")
                    break
                else:
                    print("Cannot move!")
                    return True
        if o == 's':
            i = count - 4
            if not self.foundation_stacks[i].is_empty():
                self.gaps[count] = self.foundation_stacks[i].peek()
            else:
                self.gaps[count] = '[  ]'
            del self.cascades[pos][-1]
        elif o == 'c':
            self.cells[pos] = ""
            self.gaps[pos] = "____"
            self.gaps[count] = chosen_card
            self.display_board()
        else:
            print "Cannot move between foundations"
        self.display_board()


    #If the player wants to move to cells, we can move the card unless cells are already full.
    #When origin = s we are checking if the card is at cascade, similarly origin = c for cells and origin = f for foundation.
    def inspect_cell(self,chosen_card, pos,o ):
        for place in range(len(self.cells)):
            self.flag = 0
            if self.cells[place] == "":
                self.flag = 1
                self.cells.append(chosen_card)
                if o == 's':
                    del self.cascades[pos][-1]
                elif o == 'c':
                    self.cells[pos] = ""
                    self.gaps[pos] = '____'
                    self.display_board()
                elif o == 'f':
                    i = pos - 4
                    if not self.foundation_stacks[i].is_empty():
                        self.gaps[pos] = self.foundation_stacks[i].peek()
                    else:
                        self.gaps[pos] = "[  ]"
                    self.display_board()
                else:
                    print("wrong!")
                self.cells[place] = chosen_card
                self.gaps[place] = chosen_card
                self.display_board()
                break
        if self.flag == 0:
            print("\nCells are full!!!")
            return False


    #This is a display function. We replace the values back to the actually card face. We inspect gaps to see if all the place holders for foundation stacks
    #have Kings(value 13). So when count of kings equals 4, player has won the game.
    def display_board(self):

        display_string = "\n"
        for s in range(len(self.gaps)):
            display_string += self.gaps[s] + "   "
        display_string += "\n\n"
        max_length = len(max(self.cascades, key=len))

        for i in range(max_length):
            for item in self.cascades:
                if len(item) >= i + 1:
                    display_string += '{0:>4}'.format(item[i]) + "   "
                else:
                    display_string += "       "
            display_string += "\n"
        print display_string.replace("13"," K").replace("12"," Q").replace("11"," J").replace(" 1:"," A:")
        count = 0
        for i in range(4,8):
            if self.gaps[i] != [  ]:
                l,r = self.gaps[i].split(':')
                if l == str(13):
                    count += 1
            if count == 4:
                print ("Congratulations! You have won the game")
            else:
                return False

        return False


    #We let the player choose a place to move the card to.
    def move_to_place(self,pass_card,posi,orig):
        wrong = True
        while wrong:
            move_to = raw_input("Move to ? \n Choose: c -- cascade\n \t f -- faoundation \n \t cell -- cell\n")
            if move_to == "c":
                self.inspect_cascade(pass_card,posi,orig)
                wrong = self.display_board()
            elif move_to == "f":
                wrong = self.inspect_foundation(pass_card, posi, orig)
            elif move_to == "cell":
                wrong = self.inspect_cell(pass_card, posi, orig)
            else:
                print("Invalid choice")
                wrong = True
        return "S"


def main():
    #Initializing object for NotFreecell. Quit option is given for the player
        deck_begin = Deck(1,13,4)
        deck_begin.shuffle_deck()
        free_cell = NotFreecell(deck_begin)
        print(free_cell)
        exit_var = ''
        while exit_var != "X":
            pick_card = raw_input("Pick a card to move or enter X to quit game: ").upper().strip().replace("K","13").replace("Q","12").replace("J","11").replace("A","1")
            if pick_card != "X":
                exit_var = free_cell.validate_pick_card(pick_card)
            else:
                exit_var = "X"



if __name__ == "__main__":
    main()