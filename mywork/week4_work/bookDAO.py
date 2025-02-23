import requests

url = "http://andrewbeatty1.pythonanywhere.com/books"

#This function reads all the books from the pythonanywhere site.
#It returns a list of books
#If there is an error it returns a string starting with "Error: "
def readbooks():
    response = requests.get(url)
    #Should check for status code here
    if response.status_code != 200:
        return "Error: API response code: " + str(response.status_code)
    else:
        return response.json()
    
#This function reads a single book from the pythonanywhere site.
#It returns a dictionary with the book details
#If there is an error it returns a string starting with "Error: "
def readbook(bookid):
    geturl = url + "/" + str(bookid)
    response = requests.get(geturl)
    #Should check for status code here
    if response.status_code != 200:
        return "Error: API response code: " + str(response.status_code)
    else:
        return response.json()
    
#This function will create a new book on the pythonanywhere site.
#It takes a dictionary with the book details as an argument.
#It returns a dictionary with the book details
#If there is an error it returns a string starting with "Error: "
def createbook(book):

    response = requests.post(url, json=book)

    #Alternative way to do the same thing as above....
    #headers = {'Content-type': 'application/json'}
    #response = requests.post(url, data=json.dumps(book), headers=headers)


    #Should check for status code here
    if response.status_code != 200:
        return "Error: API response code: " + str(response.status_code)
    else:
        return response.json()

#This function will update a book on the pythonanywhere site.
#It takes a bookid and a dictionary with the book details as an argument.
#It returns a dictionary with the book details
#If there is an error it returns a string starting with "Error: "  
def updatebook(bookid, book):
    updateurl = url + "/" + str(bookid)

    response = requests.put(updateurl, json=book)

    #Alternative way to do the same thing as above....
    #headers = {'Content-type': 'application/json'}
    #response = requests.put(updateurl, data=json.dumps(book), headers=headers)
    
    #Should check for status code here
    if response.status_code != 200:
        return "Error: API response code: " + str(response.status_code)
    else:
        return response.json()
    

def deletebook(bookid):
    deleteurl = url + "/" + str(bookid)
    response = requests.delete(deleteurl)
    #Should check for status code here
    if response.status_code != 200:
        return "Error: API response code: " + str(response.status_code)
    else:
        return response.json()


if __name__ == "__main__":
    #print(readbooks())
    #print(readbook(545))
    #print(readbook(546))
    book = {"title":"The Hobbit", "author":"JRR Tolkien", "price":9.99}
    #print(createbook(book))
    #print(deletebook(546))
    print("done")
