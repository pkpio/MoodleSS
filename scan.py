#!/usr/bin/env python

# Developer:	Praveen Kumar Pendyala
# Created:	18/11/2014

import bs4
import urllib
from bs4 import BeautifulSoup
import simplejson as json

class MoodleSite:
        def __init__(self,name,url):
                self.name = name
                self.url = url
	def to_JSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

html = urllib.urlopen('http://moodle.net/sites/').read()
html = html[html.index("<ul style='list-style:none;list-spacing:10px;'>"):]

soup = BeautifulSoup(html)
f = open('moodles.txt','w')
f.write('[')
for site in soup.find_all('li'):
	name = site.a
	if(name):
		link =  name.get('href')
		if(link):
			site = MoodleSite(name.contents[0], link)
			f.write(site.to_JSON() + ',')

f.write(']')
f = open('moodles.txt', 'r')
print f.read()
