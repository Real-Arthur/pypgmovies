from flask import Flask, request, jsonify, json
from peewee import *
from marshmallow import Schema, fields
import database

mysql_db = MySQLDatabase('cast_watch', user='root', password='Woxnsk19', host='localhost', port=3306)
mysql_db.connect()


class BaseModel(Model):
    class Meta:
        database = mysql_db
        

class Movie(BaseModel):
    id = IntegerField(primary_key=True)
    title = CharField(max_length=300, unique=True)
    overview = CharField(max_length=2000)
    release_date = CharField(max_length=12)
    poster_path = CharField(max_length=60)


# User class
class User(BaseModel):
    id = AutoField(primary_key=True)
    username = CharField(max_length=80, unique=True)
    password = CharField(max_length=1000)


# User_Movie class
class User_Movie(BaseModel):
    id = IntegerField(primary_key=True)
    user_id = ForeignKeyField(User)
    movie_id = ForeignKeyField(Movie)


# Movie Schema
class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    overview = fields.Str()
    release_date = fields.Str()
    poster_path = fields.Str()


def index():
    print(request.json['name'])
    return 'Good to go!'

# Get all movies from database
def get_movies():
    query = Movie.select().order_by(Movie.title).dicts()
    return jsonify({'movies':list(query)})

# Get all movies in user's collection by user Id from User_Movie table
def get_library(userId):
    query = Movie.select().join(User_Movie).distinct().where(User_Movie.user_id == userId).order_by(User_Movie.id).dicts()
    return jsonify({'library':list(query)})

# Add movie to user's collection
def add_library(userId):
    Movie.create(id=263115, title='Logan', overview="In the near future, a weary Logan cares for an ailing Professor X in a hideout on the Mexican border. But Logan's attempts to hide from the world and his legacy are upended when a young mutant arrives, pursued by dark forces.", release_date='2017-02-28', poster_path='/fnbjcRDYn6YviCcePDnGdyAkYsB.jpg')
    User_Movie.create(user_id=userId, movie_id=263115)
    return '200'