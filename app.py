from flask import Flask, request, jsonify
from peewee import *

app = Flask(__name__)
mysql_db = MySQLDatabase('cast_watch', user='root', password='Woxnsk19', host='localhost', port=3306)
mysql_db.connect()

class BaseModel(Model):
    class Meta:
        database = mysql_db
        

class Movie(BaseModel):
    id = AutoField(primary_key=True)
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
    id = AutoField(primary_key=True)
    user_id = IntegerField()
    movie_id = IntegerField()


@app.route('/')
def index():
    return 'Good to go!'

@app.route('/movies')
def get_movies():
    query = Movie.select()
    print(query)
    return jsonify([movie.title for movie in query])

# run server
if __name__ == '__main__':
    app.run(debug=True)
