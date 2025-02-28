#Write a program that reads the dataset for the "exchequer account (historical series)" from the CSO, and 
#stores it into a file called "data/cso.json".

#Author: Michael Curley

#Import the requests and json modules
import requests
import json

#Set the urlstart, urlend and dataset variables
urlstart = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlend = "/JSON-stat/2.0/en"
dataset = "FIQ02"

#Send a get request to the url
response = requests.get(urlstart + dataset + urlend)

#Check if the response code is not 200 and print an error message if it is not
#Otherwise write the data to a file in the data folder called cso.json
if response.status_code != 200:

    print("Error: API response code: " + str(response.status_code))
else:
    with open("data/cso.json", "wt") as fp:
        json.dump(response.json(), fp, indent=4)
    print("Data written to file ")

#Tidy up by closing the file
fp.close()