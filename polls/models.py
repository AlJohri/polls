from firebase import firebase
firebase = firebase.FirebaseApplication('https://aljohri-polls.firebaseio.com', None)

from pprint import pprint as pp
from pymongo import MongoClient
client = MongoClient()
db = client.polls

hp_polls = db.hp_polls
hp_questions = db.hp_questions
hp_survey_houses = db.hp_survey_houses
hp_sponsors = db.hp_sponsors
hp_pollsters = db.hp_pollsters

rcp_modules = db.rcp_modules
rcp_races = db.rcp_races
rcp_questions = db.rcp_questions
rcp_pollsters = db.rcp_pollsters

fte_pollsters = db.fte_pollsters
