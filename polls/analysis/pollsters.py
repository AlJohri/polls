from ..models import hp_pollsters, rcp_pollsters
from pprint import pprint as pp
import unicodecsv as csv
from ..scrapers.hp import group_pollsters_by_combinations

with open("../data/hp_pollsters_2014.csv", "w") as f:
	writer = csv.writer(f)
	query_2014 = {"questions.name": {"$regex": "^2014.*"}}
	pollsters = group_pollsters_by_combinations(query_2014)
	for pollster_name, combinations in pollsters.iteritems():
		writer.writerow([pollster_name, hp_pollsters.find_one(pollster_name).get('ftename')])

with open("../data/hp_pollsters_2012.csv", "w") as f:
	writer = csv.writer(f)
	query_2014 = {"questions.name": {"$regex": "^2012.*"}}
	pollsters = group_pollsters_by_combinations(query_2014)
	for pollster_name, combinations in pollsters.iteritems():
		writer.writerow([pollster_name, hp_pollsters.find_one(pollster_name).get('ftename')])

with open("../data/rcp_pollsters.csv", "w") as f:
	writer = csv.writer(f)
	writer.writerows(sorted([[pollster['_id'], pollster.get('ftename')] for pollster in rcp_pollsters.find()]))

with open("../data/hp_mapping.csv", "w") as f:
	writer = csv.writer(f)
	writer.writerows(sorted([[pollster['_id'], pollster.get('ftename')] for pollster in hp_pollsters.find({"ftename": {"$exists": True}})]))

with open("../data/rcp_mapping.csv", "w") as f:
	writer = csv.writer(f)
	writer.writerows(sorted([[pollster['_id'], pollster.get('ftename')] for pollster in rcp_pollsters.find({"ftename": {"$exists": True}})]))


# ruby code
# # Remove partisan and sponsor from name.
# has_partisan = (pollster =~ /(.*)\s\(([D,R])(?:-)?(.*)\)/i)
# if has_partisan
#   huffpost_pollster_name = $1
# end

# # If HuffpostName exists, then return pollster associated with it
# possible_pollsters = []
# huffpost_names = PollsterName.where { (name == huffpost_pollster_name) & (type == 'HuffpostName') }
# return huffpost_names.take.pollster if huffpost_names.one?

# # Otherwise find a list of possible pollsters
# possible_pollsters += Pollster.search(huffpost_pollster_name)
# possible_pollsters += huffpost_pollster_name.split('/').flat_map { |name_part| Pollster.search(name_part) }
# possible_pollsters = possible_pollsters.uniq.compact

# # If methdology is online or phone, check for child pollsters
# if method == 'Internet'
#   sub_pollsters = pollster.children.to_a
#   sub_pollsters.keep_if { |x| x.type == 'OnlineOnlyPollster' }
#   fail 'Too many matching OnlineOnlyPollsters' if sub_pollsters.length > 1
#   pollster = sub_pollsters.first if sub_pollsters.one?
# elsif method == 'Live Phone'
#   sub_pollsters = pollster.children.to_a
#   sub_pollsters.keep_if { |x| x.type == 'TelephoneOnlyPollster' }
#   fail 'Too many matching OnlineOnlyPollsters' if sub_pollsters.length > 1
#   pollster = sub_pollsters.first if sub_pollsters.one?
# end

