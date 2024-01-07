from flask import Flask, render_template, request, redirect, url_for
import pymongo
from bson.objectid import ObjectId

# instantiate the app
app = Flask(__name__)

# Connect to MongoDB and define variables for collectionsMongoDB

# set up routes
@app.route('/')
def home():
    return render_template()

@app.route('/read')
def read():
    # retrieve all books from DB

    # Render read page, passing in books
    return render_template()

@app.route('/create')
def create():
    # get all the categories

    # Render create page passing in all categories for dropdown
    return render_template()


@app.route('/create', methods=['POST'])
def create_post():
    # create a JSON structure with the data the user entered
    doc = {

    }
    # insert the new doc

    # redirect to read page
    return redirect()


@app.route('/edit/<mongoid>')
def edit(mongoid):
    # get the doc that corresponds to the user selection

    # get all the categories

    # render edit page, passing in id of book to edit, book doc and all categories for dropdown
    return render_template()


@app.route('/edit/<mongoid>', methods=['POST'])
def edit_post(mongoid):
    # create a JSON structure with the data the user entered
    doc = {

    }
    # update the book with the new data

    # redirect to read page
    return redirect()


@app.route('/delete/<mongoid>')
def delete(mongoid):
    # delete the book that corresponds to the user selection

    # redirect to read page
    return redirect()

@app.errorhandler(Exception)
def handle_error(e):
    # Output any errors - good for debugging.
    return render_template('error.html', error=e) # render the edit template


if __name__ == "__main__":
    app.run(debug = True)
