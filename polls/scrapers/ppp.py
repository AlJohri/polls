import re, requests, lxml.html, datetime
import dateutil.parser

class PPPCurrent(object):

	@staticmethod
	def download():
		url_current = "http://www.publicpolicypolling.com/main/polls/"
		url_2015 = "http://www.publicpolicypolling.com/main/2015-archive.html"
		url_2014 = "http://www.publicpolicypolling.com/main/2014-archive.html"
		url_2013 = "http://www.publicpolicypolling.com/main/2013-archive.html"
		url_2012 = "http://www.publicpolicypolling.com/main/2012-archive.html"
		url_2011 = "http://www.publicpolicypolling.com/main/2011-archive.html"
		url_2010 = "http://www.publicpolicypolling.com/main/2010-archive.html"
		url_2009 = "http://www.publicpolicypolling.com/main/2009-archive.html"
		url_2008 = "http://www.publicpolicypolling.com/main/2008-archive.html"
		url_2007 = "http://www.publicpolicypolling.com/main/2007-archive.html"
		url_2006 = "http://www.publicpolicypolling.com/main/2006-archive.html"

		page = 1
		cont = True
		while cont:
			response = requests.get(url_current + "/page/%d" % page)
			doc = lxml.html.fromstring(response.content)
			last_date = None
			for blog in doc.cssselect("div[id^=entry-]"):
				prev = blog.getprevious()
				if "\n" in prev.text: date = last_date
				else: date = dateutil.parser.parse(prev.text).date()
				last_date = date

				if date >= datetime.datetime.today().date() - datetime.timedelta(1):
					title = blog.cssselect("h3.entry-header > a")[0].text
					link = blog.cssselect("h3.entry-header > a")[0].get('href')
					pdf = filter(lambda x: "pdf" in x.get('href'),lxml.html.fromstring(requests.get(link).content).xpath('.//a[contains(text(),"here")]'))[0].get('href')
					print date, title, pdf
				else:
					cont = False
					break
			page += 1


class PPPFuture(object):
	url = ""

if __name__ == '__main__':
	PPPCurrent.download()