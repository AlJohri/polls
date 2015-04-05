from ..models import fte_pollsters

if fte_pollsters.count() == 0:
	import csv
	# source: https://raw.githubusercontent.com/fivethirtyeight/data/master/pollster-ratings/pollster-ratings.tsv
	with open("../data/pollster-ratings.tsv") as f:
		reader = csv.DictReader(f, delimiter='\t')
		for pollster in reader:
			pollster['_id'] = pollster.pop('ID')
			pollster['name'] = pollster.pop('Pollster')
			print pollster
			fte_pollsters.insert(pollster)

for pollster in fte_pollsters.find():
	print pollster['_id'], pollster['name']