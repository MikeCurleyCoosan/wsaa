import requests
import csv
from xml.dom.minidom import parseString

deck = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

response = requests.get(deck)

data = response.json()

deck_id = data['deck_id']

print(deck_id)

shuffle = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"

response = requests.get(shuffle)

data1 = response.json()

#Card 1
card1 = data1['cards'][0]['code']
value1 = data1['cards'][0]['value']
suit1 = data1['cards'][0]['suit']
image1 = data1['cards'][0]['images']['png']

print(f"The first card is {value1} of {suit1}")
print(image1)

#Card 1
card2 = data1['cards'][1]['code']
value2 = data1['cards'][1]['value']
suit2 = data1['cards'][1]['suit']

print(f"The second card is {value2} of {suit2}")

