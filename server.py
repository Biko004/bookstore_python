import json
from random import randint
from flask import Flask, request
from flask_cors import CORS, cross_origin



books =[
    {
        'name': 'The Hunger Games',
        'id': 1,
        'author': 'Suzanne Collins',
        'year': 2019
    },
    {
        'name': 'Harry Potter and the Order of the Phoenix',
        'id': 2,
        'author': ' J.K. Rowling',
        'year': 2019
    },
    {
        'name': 'To Kill a Mockingbird',
        'id': 3,
        'author': 'Harper Lee',
        'year': 2019
    },
    {
        'name': 'Pride and Prejudice',
        'id': 4,
        'author': 'Jane Austen',
        'year': 2019
    }
]

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/hello/<name>")
def hello_handler(name):
    return "hello " + name

@app.route("/")
def homepage():
    return app.send_static_file('index.html')


@app.route("/books")
@cross_origin()
def get_books():
    return json.dumps(books)

@app.route('/get_book')
@cross_origin()
def get_single_book():
    book_id = int(request.args.get('id'))
    for item in books:
        if item['id'] == book_id:
            my_item = item
            break
    else:
        my_item = 'no item'
    return json.dumps(my_item)


@app.route("/add_book", methods=['POST'])
@cross_origin()
def add_book():
    book=request.get_json()
    books.append(book)
    print(books)
    return json.dumps(books)

@app.route('/static/<path:path>')
def static_root(path):
    return app.send_static_file(path)


@app.route('/static/js/<path:path>')
def javascripts(path):
    return app.send_static_file('js/' + path)


@app.route('/static/css/<path:path>')
def stylesheets(path):
    return app.send_static_file('css/' + path)


@app.route('/static/images/<path:path>')
def images(path):
    return app.send_static_file('images/' + path)


@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


if __name__ == "__main__":
    app.run(host="localhost", port=7002, debug=True)
