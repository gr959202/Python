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
            if 'overview' in partial_url and 'referees' not in partial_url:
                url = url.replace('/clubs','')
                full_url = url + partial_url
                urls.append(full_url)
            else:
                continue
        else:
            continue
    driver.close()
    urls = list(dict.fromkeys(urls))
    return soup, urls

soup, url_overview = get_soup('https://www.premierleague.com/clubs')
print(url_overview)

outfile = 'english_pl_squad.xlsx'
with pd.ExcelWriter(outfile, engine='openpyxl',mode='w') as writer:
    for ur in url_overview:
        title = findTitle(ur)
        title = title.split(',')[0]
        players_list = []
        if 'News' in title:
            title = title.replace('News', ' ')
            squad = ur.replace('overview', 'squad')
            page = urllib.request.urlopen(squad)
            soup = BeautifulSoup(page, 'html.parser')
            name = soup.findAll('h4')
            for n in name:
                name = n.text.strip()
                players_list.append(name)
                if 'Club Sites' in players_list:
                    players_list.remove('Club Sites')
                else:
                    continue
            df = pd.DataFrame(players_list, columns=['Players'])
            df.to_excel(writer, sheet_name=title)
            stats_page = ur.replace('overview', 'stats')
            page = urllib.request.urlopen(stats_page)
            soup = BeautifulSoup(page, 'html.parser')
            matches_played = soup.findAll('span', {'class': 'stat'})[0].get_text().split()[2]
            wins = soup.findAll('span', {'class': 'stat'})[1].get_text().split()[1]
            losses = soup.findAll('span', {'class': 'stat'})[2].get_text().split()[1]
            goals = soup.findAll('span', {'class': 'stat'})[3].get_text().split()[1]
            goals_conceded = soup.findAll('span', {'class': 'stat'})[4].get_text().split()[2]
            goals_conceded_per_match = soup.findAll('span', {'class': 'stat'})[24].get_text().split()[4]
            clean_sheets = soup.findAll('span', {'class': 'stat'})[5].get_text().split()[2]
            goals_per_match = soup.findAll('span', {'class': 'stat'})[8].get_text().split()[3]
            shots = soup.findAll('span', {'class': 'stat'})[9].get_text().split()[1]
            shots_on_target = soup.findAll('span', {'class': 'stat'})[10].get_text().split()[3]
            shooting_accuracy = soup.findAll('span', {'class': 'stat'})[11].get_text().split()[3]
            penalties_scored = soup.findAll('span', {'class': 'stat'})[12].get_text().split()[2]
            big_chances_created = soup.findAll('span', {'class': 'stat'})[13].get_text().split()[3]
            hit_woodwork = soup.findAll('span', {'class': 'stat'})[14].get_text().split()[2]
            passes = soup.findAll('span', {'class': 'stat'})[16].get_text().split()[1]
            passes_per_match = soup.findAll('span', {'class': 'stat'})[17].get_text().split()[3]
            passing_accuracy = soup.findAll('span', {'class': 'stat'})[18].get_text().split()[3]
            crosses = soup.findAll('span', {'class': 'stat'})[19].get_text().split()[1]
            cross_accuracy = soup.findAll('span', {'class': 'stat'})[20].get_text().split()[3]
            saves = soup.findAll('span', {'class': 'stat'})[25].get_text().split()[1]
            tackles = soup.findAll('span', {'class': 'stat'})[26].get_text().split()[1]
            tackles_success_percentage = soup.findAll('span', {'class': 'stat'})[27].get_text().split()[3]
            blocked_shots = soup.findAll('span', {'class': 'stat'})[28].get_text().split()[2]
            interceptions = soup.findAll('span', {'class': 'stat'})[29].get_text().split()[1]
            clearances = soup.findAll('span', {'class': 'stat'})[30].get_text().split()[1]
            headed_clearances = soup.findAll('span', {'class': 'stat'})[31].get_text().split()[2]
            aerial_battles_duels_won = soup.findAll('span', {'class': 'stat'})[32].get_text().split()[3]
            errors_leading_to_goals = soup.findAll('span', {'class': 'stat'})[33].get_text().split()[4]
            own_goals = soup.findAll('span', {'class': 'stat'})[34].get_text().split()[2]
            yellow_cards = soup.findAll('span', {'class': 'stat'})[36].get_text().split()[2]
            red_cards = soup.findAll('span', {'class': 'stat'})[37].get_text().split()[2]
            fouls = soup.findAll('span', {'class': 'stat'})[38].get_text().split()[1]
            offsides = soup.findAll('span', {'class': 'stat'})[39].get_text().split()[1]
            stats_list = [matches_played,wins,losses,goals,goals_conceded,goals_conceded_per_match,clean_sheets,goals_per_match,shots,shots_on_target,shooting_accuracy,penalties_scored,big_chances_created,hit_woodwork,passes,passes_per_match,passing_accuracy,crosses,cross_accuracy,saves,tackles,tackles_success_percentage,blocked_shots,interceptions,clearances,headed_clearances,aerial_battles_duels_won,errors_leading_to_goals,own_goals,yellow_cards,red_cards,fouls,offsides]
            columns = ['matches_played','wins','losses','goals','goals_conceded','goals_conceded_per_match','clean_sheets','goals_per_match','shots','shots_on_target','shooting_accuracy','penalties_scored','big_chances_created','hit_woodwork','passes','passes_per_match','passing_accuracy','crosses','cross_accuracy','saves','tackles','tackles_success_percentage','blocked_shots','interceptions','clearances','headed_clearances','aerial_battles_duels_won','errors_leading_to_goals','own_goals','yellow_cards','red_cards','fouls','offsides']
            df2 = pd.DataFrame(stats_list,columns,columns=['Statistics'])
            df2.to_excel(writer,startrow=len(df)+2,sheet_name=title)
