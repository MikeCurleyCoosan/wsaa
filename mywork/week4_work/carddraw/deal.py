class Deal:

    def __init__(self):
        pass

    #Function to deal a hand of cards from the deck of cards with the given deck id
    def dealHand(self, deck_id):
        #Import the required modules
        import requests
        #Set the url of the API
        url = "https://deckofcardsapi.com/api/deck/" + deck_id + "/draw/?count=5"

        #Send a get request to the API
        response = requests.get(url)

        #Check if the response code is not 200 and print an error message if it is not
        #Otherwise return the cards
        try:
            response.status_code = 200
            print("Successfully connected to the API.\n")
            cards = response.json().get('cards', [])

            #Create a list to store the card values
            card_hand = []
            #Add the card values to our list
            for card in cards:
                card_hand.append(card['code'])
                card_hand.append(card['value'])
                card_hand.append(card['suit'])
                card_hand.append(card['images']['png'])
                print(f"{card['value']} of {card['suit']}")
            return cards
        except:
            print("Error: API response code: ", response.status_code)