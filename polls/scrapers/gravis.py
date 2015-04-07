import requests, lxml.html

page = 0
cont = True
while cont:
	url = "http://gravismarketing.com/polling-and-market-research/page/%d/" % page
	response = requests.get(url)
	doc = lxml.html.fromstring(response.content)

	print "Page %d" % page

	for article in doc.cssselect("#content article"):
		article_id = article.get('id').replace("post-", "")

		if article_id == "0":
			cont = False
			break

		title = article.cssselect("h1.entry-title")[0].text_content()

		if "Protected" in title: continue

		try:
			time = article.cssselect("footer.entry-meta time.entry-date")[0].get('datetime')
		except:
			time = article.cssselect("footer.entry-meta a")[0].text_content()

		print article_id, time, title

	page += 1