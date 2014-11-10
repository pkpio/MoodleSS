#!/usr/bin/env python

# Developer:	Praveen Kumar Pendyala
# Created:	18/11/2014

import urllib

mListUrl = 'http://moodle.net/sites/'
print urllib.urlopen(mListUrl).read()
