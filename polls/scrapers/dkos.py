from polls.models import firebase

import re, requests, lxml.html, datetime
import dateutil.parser

class DKOSCurrent(object):
	url_2014 = "https://docs.google.com/spreadsheet/ccc?key=0At9k6QrlThx6dGVMLTFnMEc0d1NfS29KM0piMWVVNFE#gid=0"
	url_2012 = "https://docs.google.com/spreadsheets/d/1MXxdFjBa0lOR8qJ0UFZ0f-Wv8yGDYKiwE8vtb7a3i3Y/edit#gid=0"

	@staticmethod
	def download():
		return {}

if __name__ == '__main__':
	DKOSCurrent.download()