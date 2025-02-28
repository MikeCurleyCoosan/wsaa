class Analyse:

    def __init__(self):
        pass

    #Function to analyse the hand of cards for pairs, three of a kind, four of a kind and a full house
    #Returns the result of the analysis
    def analyseHand(self, hand):
        #Create a dictionary to store the card values
        card_values = {}
        #Add the card values to our dictionary
        for card in hand:
            card_values[card['value']] = card_values.get(card['value'], 0) + 1


        #Create a list to store the result of the analysis
        result = []
        #Check for pairs, three of a kind, four of a kind and a full house
        for value, count in card_values.items():
            if count == 2:
                result.append(f"Pair of {value}s")
            elif count == 3:
                result.append(f"Three of a kind: {value}s")
            elif count == 4:
                result.append(f"Four of a kind: {value}s")
        #Check for a full house
        if len(result) == 2:
            result.append("Full house")

        #Return the result of the analysis
        return result