# Work on the player class give them the ability to have a hand and to deal the 
# cards into that hand 

from random import shuffle

class Card:
    def __init__(self, rank, suit): 
        self.rank = rank
        self.suit = suit 
    
    def __str__(self):
        return str(self.rank) + " of " + self.suit

class Deck:
    deck = []
    def __init__(self):
    
        suits = "Hearts", "Diamonds", "Clubs", "Spades"
        ranks = 2,3,4,5,6,7,8,9,10,"J","Q","K","A"
        for suit in suits:
            for rank in ranks:
                card= Card(rank,suit)
                self.deck.append(card)
    # need to be able to deal cards
    def deal_card(self):
        dealt_card = self.deck.pop()
        return dealt_card # return gives back the value to whomever called it.  

    # needs to be able to shuffle
    def shuffle(self):
        shuffle(self.deck)
    # display the deck
    def display(self):
        for card in self.deck:
            print(card)

class Player:
    def __init__(self, name, isdealer):
        self.name = name
        self.hand = []
        self.isdealer = isdealer  
# Work on the player class give them the ability to have a hand and to deal the 
# cards into that hand 

def main(): # main can be called blackjack or gameplay
    
    # Welcome the player and explain the rules
    print("""Welcome to Blackjack! Here are the Rules
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (H)it to take another card.
      (S)tand to stop taking cards.
      The dealer stops hitting at 17""")

    # Run a game of blackjack
    # create a deck of cards outside of the main. 
    deck = Deck()
    deck.shuffle()
    deck.display()

    # Make player 1 and the dealer

#    while True:

        # return cards to the deck
        # Shuffle the deck of cards close to the start to start a new game. 
        # Deal 2 cards to the players

        # Loop: display hands and scores 
        # Ask them to hit or stand. 
        # Determine Winner





    
# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()

