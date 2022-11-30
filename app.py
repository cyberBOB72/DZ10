import requests
from utils import *
from flask import Flask

response = requests.get('https://www.jsonkeeper.com/b/95Z4')
response_json = response.json()

app = Flask(__name__)

@app.route("/")
def page_index():
  return get_all(response_json)


@app.route("/candidates/<int:uid>")
def page_candidates(uid):
  return get_by_pk(uid, response_json)


@app.route("/skills/<uid>")
def page_skills(uid):
  return get_by_skill(uid, response_json)

app.run()
