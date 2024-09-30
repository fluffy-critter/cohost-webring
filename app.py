""" Flask-based webring system """

import feedparser
import flask
import requests
from flask_caching import Cache

app = flask.Flask(__name__)
cache = Cache(app, config={
    'CACHE_TYPE': 'memcached',
    'CACHE_DEFAULT_TIMEOUT': 60,
    'CACHE_KEY_PREFIX': 'cwr.beesbuzz.biz',
})

