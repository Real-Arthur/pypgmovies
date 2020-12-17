from flask import Flask, request, jsonify, json
from peewee import *
from marshmallow import Schema, fields
import database
import settings
import api

app = Flask(__name__)
mysql_db = MySQLDatabase('cast_watch', user='root', password=settings.DB_PASSWORD, host='localhost', port=3306)
mysql_db.connect()


# test route
@app.route('/')
def index():
    return database.index()

# Get all movies from database
@app.route('/movies')
def get_movies():
    return database.get_movies()

# Get all movies in user's collection by user Id from User_Movie table
@app.route('/library/<userId>', methods=['GET'])
def get_library(userId):
    return database.get_library(userId)

# Add movie to user's collection
@app.route('/library/<userId>', methods=['POST'])
def add_library(userId):
    return database.add_library(userId)

# Searches The Movie Database API for queried actor/actress
# Data provided by api.py get_person
@app.route('/api/person', methods=['GET', 'POST'])
def get_person():
    data = request.get_json()
    print(data)
    results = api.get_person(data['query'])
    # print(results)
    # return results
    return results


@app.route('/api/title', methods=['GET', 'POST'])
def get_title():
    data = request.get_json()
    print(data)
    results = api.get_title(data)
    # print(results)
    # return results
    return results

# run server
if __name__ == '__main__':
    app.run(debug=True)
