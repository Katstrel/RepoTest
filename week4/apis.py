#Rebecca
#book.py

from flask import Flask, request, jsonify, abort

app = Flask(__name__)
books = []


# Create a new Book
@app.route('/books', methods=['POST'])
def createBook():
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON body required."}), 400

    # Required fields
    required_fields = ['id', 'title', 'author', 'publisher']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing one or more required fields: id, title, author, publisher."}), 400

    # Check for duplicate book ids
    if any(book['id'] == data['id'] for book in books):
        return jsonify({"error": "Book id already exists."}), 400

    books.append(data)
    return jsonify(data), 201


# Retrieve all Books
@app.route('/books', methods=['GET'])
def getBooks():
    return jsonify(books), 200


# Retrieve a specific Book by id
@app.route('/books/<bookID>', methods=['GET'])
def getBook(bookID):
    for book in books:
        if book['id'] == bookID:
            return jsonify(book), 200
    return jsonify({"error": "Book not found."}), 404


# Update a Book by id
@app.route('/books/<bookID>', methods=['PUT'])
def updateBook(bookID):
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON body required."}), 400

    for book in books:
        if book['id'] == bookID:
            # Update the provided fields
            book['title'] = data.get('title', book['title'])
            book['author'] = data.get('author', book['author'])
            book['publisher'] = data.get('publisher', book['publisher'])
            return jsonify(book), 200

    return jsonify({"error": "Book not found."}), 404


# Delete a Book by id
@app.route('/books/<bookID>', methods=['DELETE'])
def deleteBook(bookID):
    for index, book in enumerate(books):
        if book['id'] == bookID:
            removedBook = books.pop(index)
            return jsonify({
                "message": "Book deleted.",
                "book": removedBook
            }), 200

    return jsonify({"error": "Book not found."}), 404


if __name__ == '__main__':
    app.run(debug=True)