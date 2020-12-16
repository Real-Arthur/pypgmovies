from flask import Flask, request, jsonify, json
from peewee import *
from marshmallow import Schema, fields
import database

app = Flask(__name__)
mysql_db = MySQLDatabase('cast_watch', user='root', password='Woxnsk19', host='localhost', port=3306)
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
@app.route('/library/<userId>')
def get_library(userId):
    return database.get_library(userId)

# Add movie to user's collection
@app.route('/library/<userId>')
def add_library(userId):
    return database.add_library


# run server
if __name__ == '__main__':
    app.run(debug=True)
