#####################################################################
# author:  Satyendra Raj Singh   
# date:     2/15/2024  
# description: CardGame
#####################################################################

# import the shuffle and seed functions from the random library.
import random
import os
# set the seed
random.seed(9876543210)

# define the possible suits that the cards can have using a list.
POSSIBLESUITS = ["clubs", "diamonds", "hearts", "spades"]

class Card:
    POSSIBLESUITS = ["clubs", "diamonds", "hearts", "spades"]

    def __init__(self,number=2,suit='clubs'):
        self._number = number
        self._suit = suit
    
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self,value):
        if 2 <= value <= 10:
            self._number = value
        else: 
            self._number = 2

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self,value):
        if value in self.POSSIBLESUITS:
            self._suit = value
        else:
            self._suit = "clubs"

    def __str__(self):
        return f"{self._number} of {self.suit}"

    def __gt__(self,value):
        return self._number > value.number

    def __lt__(self,value):
        return self._number < value.number

    def __eq__(self,value):
        return self._number == value.number

class PictureCard(Card):
    def __init__(self, number, suit):
        super().__init__(number, suit)
        self._imagefile = self.create_image_file_name(number, suit)
        
    @property
    def imagefile(self):
        return self._imagefile

    @imagefile.setter
    def imagefile(self, imagefile):
        directory = "images" 
        full_path = os.path.join(directory, imagefile)
        if os.path.exists(full_path):
            self._imagefile = full_path
        else:
            print("Invalid file name. Setting imagefile to default.png")
            self._imagefile = os.path.join(directory, "default.png")
            
    def create_image_file_name(self, number, suit):
        return f"{number}_of_{suit}.png"

class Deck:
    def __init__(self):
        self._cards = [PictureCard(number, suit) for number in range(2,11) for suit in Card.POSSIBLESUITS]

    @property
    def cards (self):
        return self._cards
    
    @cards.setter
    def cards(self, newcards):
        self._cards = newcards

    def shuffle(self):
        random.shuffle(self._cards)
    
    def size(self):
        return len(self._cards)

    def draw(self):
        if self.size()>0:
            return self._cards.pop(0)
        else:
            return 0

    def __str__(self):
        if self.size() ==  0:
            return "[--empty--]"
        else:
            return "["+", ".join([str(card) for card in self._cards]) + ", " + "]"


class Game:
    def __init__(self):
        self._deck = Deck()
        self._deck.shuffle()
        self._deck.shuffle()

    @property
    def deck(self):
        return self._deck

    @deck.setter
    def deck(self , value):
        self._deck = value 


    def start(self):
        print(f"------------------------------------------------------------------")
        print("Welcome to the Basic Game!")
        print(f"You and this program will take turns picking cards.")
        print(f"The one with the highest value card wins")
        print(f"------------------------------------------------------------------")
        ready = input("Are you ready to start the Card Game? (y/n): ")
        if ready.lower() == 'y':
            self.play()
        else:
            self.end()

    def end(self):
        # print("Game over", self._deck)
        print(self._deck)

    def play(self):
        
        while self._deck.size() >=  2:
            playercard = self._deck.draw()
            computercard = self._deck.draw()

            print(f"You picked {playercard}, and I picked {computercard}")

            if playercard > computercard:
                print("I WIN")
            elif playercard < computercard:
                print("YOU WIN")
            else:
                print("It's a tie")

            # self._deck.shuffle()
            # print("Deck size after rounds:", self.deck.size()
            playagain = input("Would you like to play again? (y/n): ").lower()
            if playagain != "y":
                self.end()
                break
        if self._deck.size() < 2:
                print("Not enough cards to play.")
                print("Sorry to see you go.")
                print("------------Remaining Cards--------------")
                self.end()   
         
            
    



        

