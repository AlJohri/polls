import requests, lxml.html

# http://surveys.ap.org/
# http://ap-gfkpoll.com/poll-archives

response = requests.get("http://surveys.ap.org/")
doc = lxml.html.fromstring(response.content)
for poll in doc.cssselect("li"):
	print poll.text