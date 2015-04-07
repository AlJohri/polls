from polls.models import firebase

import re, requests, lxml.html, datetime
import dateutil.parser

class QuinnipiacCurrent(object):

	@staticmethod
	def download():

		result = firebase.put(url='/status', name="quinnipiac", data="loading", headers={'print': 'pretty'})

		firebase.delete('/quinnipiac', None)

		url = "http://www.quinnipiac.edu/news-and-events/quinnipiac-university-poll/search-releases/search-results/?What=&Submit=Submit&strArea=%3B&strSubject=&strTime=28&strAddr="
		response = requests.get(url)
		doc = lxml.html.fromstring(response.content)
		for row in doc.cssselect("#skipToContent > div > article > table > tr > td[valign=top]"):
			date = dateutil.parser.parse(row.cssselect("b")[0].text).date()
			text = [x for x in row.itertext()][1].replace("\t-", "").replace("\r\n", " ").replace("  ", " ").strip()
			link = row.cssselect("a")[0].get('href')

			release_id = re.search(r".*ReleaseID=(\d+).*", link).groups()[0]
			states, text = re.search(r"^\((.*)\)\s-\s(.*)", text).groups()
			states = states.split(", ")

			poll = {"id": release_id, "date": date, "states": states, "text": text}

			if date >= datetime.datetime.today().date() - datetime.timedelta(1):
				result = firebase.post(url='/quinnipiac', data=poll, headers={'print': 'pretty'})
				print release_id, " | ", date, "|", states, "|", text
			else:
				break

		result = firebase.put(url='/status', name="quinnipiac", data="complete", headers={'print': 'pretty'})

class QuinnipiacFuture(object):
	url = ""

if __name__ == '__main__':
	QuinnipiacCurrent.download()