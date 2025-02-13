#Program to search for the definition of a word using the dictionaryapi.dev API
#Author: Michael Curley
#API Documentation: https://dictionaryapi.dev/
#Date: 13/02/2025

#Import the required libraries
import requests
import csv
from xml.dom.minidom import parseString

#Set the base url for the API
base_url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'

#Ask the user to enter a word to search for
word = input("Enter a word to search for: ")

#Create the full url
url = base_url + word

#Make a request to the API
response = requests.get(url)

#Check if the request was successful
if response.status_code != 200:
    print(f"An error occurred: {response.status_code}")
    exit()

#Get the data from the response
data = response.json()

#Print the saved definitions of the word
for definition in data:
    print(f"Word: {definition['word']}")
    for meanings in definition['meanings']:
        print(f"Part of Speech: {meanings['partOfSpeech']}")
        for definition in meanings['definitions']:
            print(f"Definition: {definition['definition']}")
            if 'example' in definition:
                print(f"Example: {definition['example']}")
            else:
                print("No example provided")
            print("\n")

