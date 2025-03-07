#The following are the curl commands to test the API
#The API is a simple book API that allows you to create, read, update and delete books
#The API is running on http://127.0.0.1:5000 and is a flask API
#The API has the following endpoints:
#GET /books - Get all books
#GET /books/<int:isbn> - Get a book by ISBN
#POST /books - Create a book
#PUT /books/<int:isbn> - Update a book
#DELETE /books/<int:isbn> - Delete a book


#Get all
curl http://127.0.0.1:5000/books

#Get one
curl http://127.0.0.1:5000/books/1

#Create a book
curl -X POST -d "{\"title\":\"The Hobbit\",\"author\":\"J.R.R. Tolkien\",
\"price\":123, \"isbn\":123456789}" -H "Content-Type: application/json" http://127.0.0.1:5000/books

#Update a book
curl -X PUT -d "{\"title\":\"The Hobbit\",\"author\":\"J.R.R. Tolkien\",
\"price\":123, \"isbn\":123456789}" -H "Content-Type: application/json" http://127.0.0.1:5000/books/1

#Delete a book
curl -X DELETE http://127.0.0.1:5000/books/1

