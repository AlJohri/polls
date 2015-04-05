from ..models import hp_polls

from collections import defaultdict
from urlparse import urlparse

from ..scrapers.hp import url

def group_sources_by_domain():
	sources = defaultdict(list)

	for poll in hp_polls.find():
		if poll['source']:
			source = urlparse(poll['source']).netloc
			source = source or "error"
			sources[source].append(poll['source'])

	for source, urls in sources.iteritems():
		print source, len(urls)
		print "\t" + urls[0]

	return sources

select_pollsters = [
	# "gallup",
	# "rasmussenreports",
	# "suffolk",
	# "cnn",
	# "ogdenfry",
	# "publicpolicypolling",
	"marist",
	# "ipsos-na",
]

for poll in hp_polls.find():
	for pollster in select_pollsters:
		if (pollster in (poll.get('source') or "")):
			print poll['source']
	# if poll['source'] and ".pdf" in poll['source']:
		# print url(poll), poll['source']