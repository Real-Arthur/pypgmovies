import json
import requests
import os
import settings
from flask import Flask, jsonify, request
# from decouple import config

# Searches The Movie Database API for queried actor/actress
def get_person(value):
    url = 'https://api.themoviedb.org/3/search/person'
    params = dict(
        api_key=settings.API_KEY,
        query=value,
        page=1
    )
    resp = requests.get(url=url, params=params)
    data = resp.json()
    return jsonify(data['results'])


def get_title(value):
    url = 'https://api.themoviedb.org/3/search/movie'
    params = dict(
            api_key=settings.API_KEY,
            query=value,
            page=1
        )
    resp = requests.get(url=url, params=params)
    data = resp.json()
    return jsonify(data)
    