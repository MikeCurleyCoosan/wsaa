import requests
import json
from xml.dom.minidom import parseString
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

#Shuffle a deck of cards by making a request to the deckofcardsapi.com API
shuffle_deck = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

response = requests.get(shuffle_deck)

data = response.json()
#Get the deck_id from the shuffled deck as we will use this deck to draw 5 cards
deck_id = data['deck_id']

#print(deck_id) #Testing purposes

#Draw 5 cards from the deck	and assign the card values to a list
draw_cards = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"

response2 = requests.get(draw_cards)

data1 = response2.json()
#Create a list to store the card values
card_hand = []
#Add the card values to our list
for card in data1['cards']:
    card_hand.append(card['code'])
    card_hand.append(card['value'])
    card_hand.append(card['suit'])
    card_hand.append(card['images']['png'])
    print(f"{card['value']} of {card['suit']}")
    #print the image of the card

#Save a a json file to the data folder
with open('data/card_hand.json', 'w') as f:
    json.dump(data1, f)

#Display the card hand dealt
fig, ax = plt.subplots(1,5, figsize=(12,6))
for i in range(5):
    url = data1['cards'][i]['images']['png']
    img = Image.open(requests.get(url, stream = True).raw)
    ax[i].imshow(img)
    ax[i].axis('off')
plt.show()


#Check for a pair, three of a kind or four of a kind in the card hand
#Create a dictionary to store the card values
card_dict = {}
#Add the card values to the dictionary
for card in data1['cards']:
    if card['value'] in card_dict:
        card_dict[card['value']] += 1
    else:
        card_dict[card['value']] = 1

#Check for a pair, three of a kind or four of a kind in the card hand
for card in card_dict:
    if card_dict[card] == 2:
        print(f"Pair of {card}")
    elif card_dict[card] == 3:
        print(f"Three of a kind {card}")
    elif card_dict[card] == 4:
        print(f"Four of a kind {card}")
