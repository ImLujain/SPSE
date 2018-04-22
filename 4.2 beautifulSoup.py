#!/usr/bin/python

from bs4 import BeautifulSoup
import urllib


html = urllib.urlopen('http://www.securitytube.net/video/3000')

bt = BeautifulSoup(html.read(), "lxml") #force it to use lxml parser

print bt.title.string #navigable string, fetching the string in title only without the tags 
#print bt.title will print title tags
allMetaTags = bt.find_all('meta')
alllinks = bt.find_all('a')

print allMetaTags[0]['content']

for i in range(len(alllinks)):
	print alllinks[i]['href']


for link in alllinks:
	print links['href']


#bt.get_text() > print all texts in the file 
