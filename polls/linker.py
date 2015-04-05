import csv, datetime
from models import rcp_questions, hp_questions
from pprint import pprint as pp

with open("data/rcp_questions.csv", "w") as f:
	writer = csv.writer(f)
	for question in rcp_questions.find({"cycle": {"$gt": 2013}}).sort([("cycle", 1), ("date", 1)]):
		writer.writerow([question['pollster'].encode('utf-8'), question['cycle'], question['date'], question['title']])

with open("data/hp_questions.csv", "w") as f:
	writer = csv.writer(f)
	for question in hp_questions.find({"cycle": {"$gt": 2013}}).sort([("cycle", 1), ("date", 1)]):
		writer.writerow([question['pollster'].encode('utf-8'), question['cycle'], question['date'], question['name']])

# import re

# for x in hp_polls.distinct("questions.name"):
# 	if not re.match(r"^\d{4}.*$", x):
# 		print x