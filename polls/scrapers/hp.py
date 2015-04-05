from polls.models import hp_polls, hp_survey_houses, hp_sponsors, hp_pollsters, fte_pollsters, hp_questions
from polls.models import firebase
from collections import defaultdict
import re, requests, csv, datetime
from pprint import pprint as pp

import dateutil.parser

# last page as of March 27, 8PM CST
# http://elections.huffingtonpost.com/pollster/api/polls?page=2121
# http://elections.huffingtonpost.com/pollster/api/polls?page=1617&showall=true
# http://elections.huffingtonpost.com/pollster/api/polls?page=1587&showall=false

class HPCurrent(object):
	@staticmethod
	def download():

		firebase.delete('/hp', None)

		page = 0
		cont = True
		while cont:
			url = "http://elections.huffingtonpost.com/pollster/api/polls?page=%d" % page
			for poll in requests.get(url).json():
				date = dateutil.parser.parse(poll['last_updated']).date()
				if date >= datetime.datetime.today().date() - datetime.timedelta(2):
					print date, poll['pollster']
					for i, question in enumerate(poll['questions']):
						question['id'] = str(poll['id']) + "-" + str(i)
						for j, subpopulation in enumerate(question['subpopulations']):
							subpopulation['id'] = str(question['id']) + "-" + str(j)
							subpopulation['name'] = question['name']
							subpopulation['poll_id'] = poll['id']
							subpopulation['pollster'] = poll['pollster']
							subpopulation['start_date'] = poll['start_date']
							subpopulation['end_date'] = poll['end_date']
							subpopulation['last_updated'] = poll['last_updated']
							result = firebase.post(url='/hp', data=subpopulation, headers={'print': 'pretty'})
				else:
					cont = False
					break
			page += 1

def url(poll): return u'http://elections.huffingtonpost.com/pollster/polls/-%s' % poll['_id']

def isvoting(x):
	if "Approval" in x: return False
	if "Favorable" in x: return False
	if "Satisfaction" in x: return False
	if "US Economy" in x: return False
	if "Wrong Track" in x: return False
	if "Favor/Oppose" in x: return False
	if "Party ID" in x: return False
	if "Party Identification" in x: return False
	if "14-IA-01-DemPR" in x or "10-AR-Sen-RepPR" in x or "08-VA-Pres-GE-MvO" in x: return False
	return True

def extract_survey_houses():
	for poll in huffpollster.find():
		for survey_house in poll['survey_houses']:
			survey_house['_id'] = survey_house.pop('name')

			# edgecase, changed partisanship?
			if survey_house['_id'] == "JMC Enterprises" and survey_house['party'] == "N/A": continue
			if not hp_survey_houses.find_one(survey_house):
				print survey_house
				hp_survey_houses.insert(survey_house)

def extract_sponsors():
	for poll in huffpollster.find():
		for sponsor in poll['sponsors']:
			sponsor['_id'] = sponsor.pop('name')

			if not hp_sponsors.find_one(sponsor):
				print sponsor
				hp_sponsors.insert(sponsor)

def group_pollsters_by_combinations(query=None):
	pollsters = defaultdict(list)
	for poll in hp_polls.find(query):
		combination = {"survey_houses": poll['survey_houses'], "sponsors": poll['sponsors']}

		pollster = poll['pollster']
		m = re.match(r"(.*)\s\(([D,R])(?:-)?(.*)\)", pollster, re.I)
		if m: pollster = m.group(1)

		if combination not in pollsters[pollster]: pollsters[pollster].append(combination)

	return pollsters

def extract_pollsters():
	pollsters = group_pollsters_by_combinations()
	for pollster_name, combinations in pollsters.iteritems():
		pollster = {"_id": pollster_name, "combinations": combinations}
		print pollster['_id'], len(combinations)
		hp_pollsters.insert(pollster)

def extract_questions():
	for poll in hp_polls.find():
		for i, question in enumerate(poll['questions']):
			question['_id'] = "%s-%s" % (poll['_id'], i)
			question['pollster'] = poll['pollster']
			question['start_date'] = poll['start_date']
			question['end_date'] = poll['end_date']

			start = datetime.datetime.strptime(question['start_date'], "%Y-%m-%d").strftime("%m/%d").lstrip("0").replace("-0", "-")
			end = datetime.datetime.strptime(question['end_date'], "%Y-%m-%d").strftime("%m/%d").lstrip("0").replace("-0", "-")
			question['date'] = "%s - %s" % (start, end)

			hp_questions.insert(question)

if __name__ == '__main__':

	if hp_polls.count() == 0:
		page = 0
		while True:
			params.update({"page": page})
			polls = requests.get("http://elections.huffingtonpost.com/pollster/api/polls", params=params).json()
			if len(polls) == 0: continue
			for poll in polls:

				for question in poll['questions']:
					if isvoting(question['name']):
						question['cycle'] = re.search(r"^(\d{4}).*$", question['name'], re.I).groups()[0]
						question['cycle'] = int(question['cycle'])
						question['question_type'] = "voting"

				poll['_id'] = poll.pop('id')
				poll['pollster'] = poll['pollster'].strip()
				print poll['_id'], poll['source']
				# record information about param used to save it??
				hp_polls.save(poll)
			page += 1

	# hp_questions.drop()

	if hp_questions.count() == 0:
		extract_questions()

	if hp_survey_houses.count() == 0:
		extract_survey_houses()

	if hp_sponsors.count() == 0:
		extract_sponsors()

	# hp_pollsters.drop()

	if hp_pollsters.count() == 0:
		extract_pollsters()

	if hp_pollsters.find({"ftename": {"$exists": True}}).count() == 0:
		with open("data/hp_mapping.csv") as f:
			reader = csv.reader(f)
			for row in reader:
				pollster = hp_pollsters.find_one(row[0])
				if pollster:
					print row[0], "| saved"
					pollster['ftename'] = row[1]
					hp_pollsters.save(pollster)
				else:
					print row[0], "| not found"

		for hp_pollster in hp_pollsters.find():
			fte_pollster = fte_pollsters.find_one({"name": hp_pollster['_id']})
			if fte_pollster and not hp_pollster.get('ftename'):
				hp_pollster['ftename'] = fte_pollster['name']
				print hp_pollster['_id'], "| saved"
				hp_pollsters.save(hp_pollster)

	HPCurrent.download()

# http://elections.huffingtonpost.com/pollster/2012-iowa-gop-primary.json
# http://elections.huffingtonpost.com/pollster/search.json
# http://elections.huffingtonpost.com/pollster/polls/398