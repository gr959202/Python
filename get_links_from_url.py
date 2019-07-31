from selenium import webdriver
import time
import re
import urllib2
from bs4 import BeautifulSoup
import os
import sys
import json
import requests

def get_soup(url):
    #urls = {}
    urls =[] 
    driver = webdriver.Safari(executable_path = '/usr/bin/safaridriver')
    driver.get(url)
    r = requests.get(url, timeout=10)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    anchors = soup.findAll('a')
    for a in anchors:
	if a.has_key('href'):
		partial_url = a.get('href')
		if partial_url.startswith('http://'):
			full_url = partial_url
		elif partial_url.startswith('https://'):
			full_url = partial_url
		else:
			full_url = url + partial_url 
			urls.append(full_url)
	else:
		continue
    
    driver.close()
    urls = list(dict.fromkeys(urls))
    return soup,urls

#soup,url_all = get_soup('https://www.indeed.com/jobs?q=supply+chain+intern&l=united+states')
soup,url_all = get_soup('https://www.espncricinfo.com')
tit_url = {}
for s in range(len(url_all)):
	if "story" in url_all[s]:
		print(url_all[s])
	else:
		continue
for s in range(len(url_all)):
	if "story" in url_all[s]:
		urli = urllib2.urlopen(url_all[s])
		html = BeautifulSoup(urli.read(),'html.parser')
		title = html.find('title')
		titlee = title.contents[0]
		if titlee not in tit_url:
			tit_url[titlee] = url_all[s]
		else:
			continue

for keys in tit_url:
	print(keys,tit_url[keys])
