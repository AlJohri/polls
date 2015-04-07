import requests, lxml.html

years = range(2005l,2015+1)
months = range(1,12+1)

for year in years:
	for month in months:
		response = requests.get("http://www.surveyusa.com/PollHistory.aspx?d=%d,%d" % (year, month))
		doc = lxml.html.fromstring(response.content)
		for a in doc.cssselect("a[id^=ctl][id$=_HyperlinkPollNumber]"):
			poll_index = a.get('id').replace("_HyperlinkPollNumber", "")
			poll_id = a.text_content().replace("Poll #", "")
			poll_key = a.get('href').replace("http://www.surveyusa.com/client/PollReport.aspx?g=", "")

			date = doc.cssselect("#%s_HyperLinkDate" % poll_index)[0].text_content()
			client = doc.cssselect("#%s_HyperlinkClient" % poll_index)[0].text_content()
			geo = doc.cssselect("#%s_HyperlinkGeo" % poll_index)[0].text_content()
			questions = doc.cssselect("a[id^=%s_ctl][id$=_HyperLinkQText]" % poll_index)

			print year, month, date, poll_id, poll_key, client, geo, len(questions)

			for question in questions:
				print "\t", question.text_content()


# poll_id = "45925278-98fe-4060-b496-b4dfbaf01f7c"
# "http://www.surveyusa.com/client/PollReport_main.aspx?g=%s" % poll_id