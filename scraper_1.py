from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import requests

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(url)

soup = bs(page.text , 'html.parser')

stars_table = soup.find_all('table' , {'class' , 'wikitable sortable'})

total_table = len(stars_table)

#print(total_table)

#print(stars_table[2])

scraped_data = []

table_rows = stars_table[2].find_all('tr')
#print(table_rows)

for tr in table_rows:
    td = tr.find_all('td')
    #print(td)
    row = [i.text.rstrip()for i in td]
    print(row)
    scraped_data.append(row)

star_name = []
distance = []
mass = []
radius = []

#print(scraped_data)

for i in range(1 , len(scraped_data)):
    star_name.append(scraped_data[i][0])
    distance.append(scraped_data[i][5])
    mass.append(scraped_data[i][7])
    radius.append(scraped_data[i][8])

headers = ['star name' , 'distance' , 'mass' , 'radius']

tf_2 = pd.DataFrame(list(zip(star_name , distance , mass , radius)) , columns = ['star name' , 'distance' , 'mass' , 'radius'])

tf_2.to_csv('dwarf_stars.csv' , index = True , index_label = 'id')