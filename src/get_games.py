
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
  ##print(raw_html)
#Get description
  xpath_for_names = "//div[@id='site_wrap']/article/div/h2/text()"
  Game_names = html.xpath(xpath_for_names)
  #print(Game_names)
  return Game_names

##Get_names('https://www.pcgamesn.com/best-pc-games')
#print(names_)
#print(scrap_page_steam(steam_link))
