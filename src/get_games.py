
import requests 
from urllib.request import urlopen
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import sys
import numpy as np 


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')



def Get_names(link):
 
  print(f"Scraping {link} ..."  )
  headers = {'Content-Type': 'text/html',}
  response = requests.get(link, headers=headers)
  raw_html = response.text
  html = etree.HTML(raw_html)
  print(html)
#Get description
  xpath_for_names = "//div/table/tbody/tr/td[(@Class = 'details')]/a//h3[0]/text()"
  Game_names = html.xpath(xpath_for_names)



  return Game_names
names_ = Get_names('https://www.metacritic.com/browse/games/score/metascore/all/pc/filtered?view=condensed')
#print(scrap_page_steam(steam_link))
