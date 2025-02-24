class Shuffle:

    def __init__(self):
        pass

    #Function to shuffle the deck of cards
    def shuffleDeck(self):
        #Import the required modules
        import requests
        #Set the url of the API
        url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

        #Send a get request to the API
        response = requests.get(url)

        #Check if the response code is not 200 and print an error message if it is not
        #Otherwise return the deck id
        try:
            response.status_code = 200
            print("Successfully connected to the API.\n")
            data = response.json()
            deck_id = data['deck_id']
            print("Deck ID: ", deck_id)
            return deck_id
        except:
            print("Error: API response code: ", response.status_code)
