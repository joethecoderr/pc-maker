
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
  driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
  driver.get(link)
  wait = WebDriverWait(driver,10)
  raw_names=[]
  for i in range(20):
      print(f"Scraping {driver.current_url} ..."  )
      headers = {'Content-Type': 'text/html',}
      response = requests.get(driver.current_url, headers=headers)
      raw_html = response.text
      html = etree.HTML(raw_html)
    #Get description
      xpath_for_names = "//div[@class='games-list']/div[@class='item']/div[2]/a/text()"
      Game_names = html.xpath(xpath_for_names)
      raw_names= raw_names +  [game_name.replace(" System Requirements", "") for game_name in Game_names]
      elem = driver.find_element_by_class_name("next").click()
  return raw_names
