#Netnews list
Netnews_list= []

#scraping
import requests
import csv
r=requests.get("https://www.asahi.com/news/")

encoding=r.encoding
if encoding.lower() == 'iso-8859-1':
    r.encoding = 'utf-8'

from bs4 import BeautifulSoup
soup=BeautifulSoup(r.text, 'html.parser')

tag=soup.find('ul', class_="List")

if tag is not None:
    for row in tag.find_all('li'):
        columns=row.find('a')
        if columns:
            target_data=columns.text
            print(target_data)
            Netnews_list.append(target_data)
else:
    print("none")