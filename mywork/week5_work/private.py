#Get information about a privte repository on github
#This is a private repository so you need to authenticate
import requests
import json
from config import config as cfg

filename = "data/aprivateone.json"

url = 'https://api.github.com/repos/MikeCurleyCoosan/aprivateone'

# the more basic way of setting authorization
#headers = {'Authorization': 'token ' + apikey}
#response = requests.get(url, headers= headers)

apikey = cfg["githubkey"]
response = requests.get(url, auth = ('token', apikey))

print (response.status_code)
#print (response.json())

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)
