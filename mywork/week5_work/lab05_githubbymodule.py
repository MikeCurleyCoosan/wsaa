from github import Github
from config import config as cfg
import requests
import json

apikey = cfg["githubkey"]

g = Github(apikey)

#Get information about a privte repository on github
#This is a private repository so you need to authenticate
repo = g.get_repo("MikeCurleyCoosan/aprivateone")
print(repo.clone_url)

#Get the url of a file in this repoistory called text.txt 
file = repo.get_contents("text.txt")
urlOfFile = file.download_url
print(urlOfFile)

#Use the downloaded url to make a http request to get the contents of the file
response = requests.get(urlOfFile)
contentsOfFile = response.text
print(contentsOfFile)

#Write the contents of the file to a file in the data folder
filename = "data/text.txt"
with open(filename
          , "wt") as fp:
    fp.write(contentsOfFile)

print("Data written to file " + filename)

#Append the text "more stuff (with a newline character)" to the file

newContents = contentsOfFile + "\nmore stuff\n"

print(newContents)

#Update the file in the repository with the new contents

gitHubResponse = repo.update_file("text.txt", "Updated text.txt", newContents, file.sha)

print(gitHubResponse)
