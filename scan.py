#!/usr/bin/env python

# Developer:	Praveen Kumar Pendyala
# Created:	18/11/2014

import bs4
import urllib
from bs4 import BeautifulSoup

html = urllib.urlopen('http://moodle.net/sites/').read()
html = html[html.index("<ul style='list-style:none;list-spacing:10px;'>"):]

soup = BeautifulSoup(html)
for site in soup.find_all('li'):
	name = site.a
	if(name):
		link =  name.get('href')
		if(link):
			print link
