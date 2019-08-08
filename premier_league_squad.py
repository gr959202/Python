from selenium import webdriver
import time
import re
import urllib
from bs4 import BeautifulSoup
import urllib.request
import os
import sys
import json
import requests
import pandas as pd
from openpyxl import load_workbook

def findTitle(url):
    webpage = urllib.request.urlopen(url).read()
    title = str(webpage).split('<title>')[1].split('</title>')[0]
    return title

def get_soup(url):
    urls = []
    driver = webdriver.Safari(executable_path='/usr/bin/safaridriver')
    driver.get(url)
    r = requests.get(url, timeout=10)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    anchors = soup.findAll('a')
    for a in anchors:
        if a.has_attr('href'):
            partial_url = a.get('href')
            if partial_url.startswith('/clubs'):
                full_url = url + partial_url
                urls.append(full_url)
        else:
            continue

    driver.close()
    urls = list(dict.fromkeys(urls))
    return soup, urls


soup, url_overview = get_soup('https://www.premierleague.com')
print(url_overview)

outfile = 'english_pl_squad.xlsx'
with pd.ExcelWriter(outfile, engine='openpyxl') as writer:
    for ur in url_overview:
        title = findTitle(ur)
        title = title.split(",")[0]
        players_list = []
        if 'News' in  title:
            title = title.replace("News"," ")
            squad = ur.replace('overview','squad')
            page = urllib.request.urlopen(squad)
            soup = BeautifulSoup(page, "html.parser" )
            name = soup.findAll('h4')
            for n in name:
                name = n.text.strip()
                players_list.append(name)
                if 'Club Sites' in players_list:
                    players_list.remove('Club Sites')
                else:
                    continue
            df = pd.DataFrame(players_list,columns=["Players"]) 
            #print(df)
            df.to_excel(writer,sheet_name=title)
    writer.save()
