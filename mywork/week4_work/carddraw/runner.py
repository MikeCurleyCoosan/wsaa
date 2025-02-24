from shuffle import Shuffle
from deal import Deal
from analyse import Analyse

#Create an instance of the Shuffle class
shuffle = Shuffle()

#Shuffle the deck of cards
deck_id = shuffle.shuffleDeck()

#Create an instance of the Deal class
deal = Deal()

#Deal a hand of cards from the deck of cards with the given deck id
hand = deal.dealHand(deck_id)

#Analyse the hand of cards for pairs, three of a kind, four of a kind and a full house
#First create an instance of the Analyse class
analyse = Analyse()
#Then analyse the hand of cards
result = analyse.analyseHand(hand)

for item in result:
    print(item)
