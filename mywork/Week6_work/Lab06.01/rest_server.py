from flask import Flask, url_for, request, redirect, abort, jsonify
app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/books', methods=['GET'])
def get_books():
    return "getting all books"

@app.route("/books/<int:id>", methods=['GET'])
def get_book_byid(id):
    return f"fing by id {id}" 

@app.route('/books', methods=['POST'])
def create_book():
    #Read json from the body of the request
    jsonstring = request.json  
    return f"creating a book with title: {jsonstring}"   

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    jsonstring = request.json      
    return f"updating a book {id} {jsonstring}"   

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    return f"deleting a book {id}"
 

if __name__ == '__main__':
    app.run(debug=True)  