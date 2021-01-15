# -*- coding: utf-8 -*-

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

def get_page_link_from_steam(game):
  print(f"Getting page for {game} ..."  )
  driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
  driver.get("https://store.steampowered.com/")
  assert "Steam" in driver.title #assert is for debugging, if the condition is false, AssertionError is raised. 
  #Here we are using it to confirm that the title has "Steam".
  wait = WebDriverWait(driver,10)
  elem = driver.find_element_by_id("store_nav_search_term")
  elem.clear()
  elem.send_keys(game)
  elem.send_keys(Keys.ENTER)

 # print(driver.page_source)
 
  driver.find_element_by_xpath("//div[(@id = 'search_resultsRows')]/a[1]").click()
  source_str =  str(driver.page_source)
   #If not appropiate for all ages
  #print(source_str)
  if "View Page" in source_str:
    print("entered")

    #Specify the age
    element = driver.find_element_by_xpath("//select[@name='ageYear']")
    all_options = element.find_elements_by_tag_name("option")
    for option in all_options:
      #print("Value is: %s" % option.get_attribute("value"))
      if  option.get_attribute("value") == '1900':
        print("clicked")
        option.click()
        

    driver.find_element_by_xpath("//div[(@class = 'main_content_ctn')]/div[@class = 'agegate_text_container btns']/a[1]").click() 
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'game_area_purchase_game')))
   
  return driver.current_url

def scrap_page_steam(link_path):
  print(f"Scraping {link_path} ..."  )
  headers = {'Content-Type': 'text/html',}
  response = requests.get(link_path, headers=headers)
  raw_html = response.text
  html = etree.HTML(raw_html)

#Get description
  xpath_for_description = "//div[(@id = 'game_area_description')]/text()"
  description_txt = html.xpath(xpath_for_description)

#Get Minimum Requirements
  xpath_for_min_req_strongs = "//div[(@class = 'game_area_sys_req_leftCol')]/ul/ul//strong/text()"
  xpath_for_min_req = "//div[(@class = 'game_area_sys_req_leftCol')]/ul/ul/li[strong]/text()" #With [] we say to look for those li with strong
  min_req_strongs = html.xpath(xpath_for_min_req_strongs)
  min_req_txt = html.xpath(xpath_for_min_req)

#Get Recommended Requirements
  xpath_for_recommended_req_strongs = "//div[(@class='game_area_sys_req_rightCol')]/ul/ul//strong/text()"
  xpath_for_recommended_req = "//div[(@class='game_area_sys_req_rightCol')]/ul/ul/li[strong]/text()" #With [] we say to look for those li with strong
  recommended_req_strongs = html.xpath(xpath_for_recommended_req_strongs)
  recommended_req_txt = html.xpath(xpath_for_recommended_req)

#Merge strongs and text in the same array
  merged_list_min = [(min_req_strongs[i], min_req_txt[i]) for i in range(0, len(min_req_strongs))]
  merged_arr_min =np.array(merged_list_min)

  merged_list_rec = [(recommended_req_strongs[i], recommended_req_txt[i]) for i in range(0, len(recommended_req_strongs)) ]
  merged_arr_recommended = np.array(merged_list_rec)

  return description_txt, merged_arr_min, merged_arr_recommended

#steam_link = get_page_link_from_steam("Cyberpunk")
#print(scrap_page_steam(steam_link))