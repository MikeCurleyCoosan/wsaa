#assignment04-github.py

#Program to use PyGithub to read a file from a repository, replace all instances of the text "Andrew"
#with my name, commit the changes and push the file back to the repository.

#Author(s): Michael Curley

#Use PyGithub
from github import Github
 
#Use the config file to get the API key for the repo we are working with.....
from data.config import config as cfg

#Use the fine grained token generated in Github, not the password
#Content and commit status has been set to read and write for this token
apikey = cfg["githubkey"]
g = Github(apikey)

#Get the content of the file
repo = g.get_repo("MikeCurleyCoosan/wsaa")
contents = repo.get_contents("assignments/data/assignment04.txt")

#Decode the byte encoded contents.decoded_content..
#...to a string and print it
internal_str = contents.decoded_content
internal_str = internal_str.decode("utf-8")
print("decoded downloaded file content\n", internal_str,sep='')

#Update all instances of "Andrew" in the file content
updated_content = internal_str.replace("Andrew", "Mike Curley")
print("updated file content for upload\n", updated_content,sep='')

#Now push the modified content with appropriate commit message
update_str = "Updated by Assignment 04 program"
response = repo.update_file(contents.path, update_str, updated_content, contents.sha)
print(response)

#Tidy up
g.close()