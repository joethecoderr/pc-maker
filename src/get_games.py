
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

# def get_game_link(game):


  

#   source_str =  str(driver.page_source)
#    #If not appropiate for all ages
#   #print(source_str)
#   if "View Page" in source_str:
#     print("entered")

#     #Specify the age
#     element = driver.find_element_by_xpath("//select[@name='ageYear']")
#     all_options = element.find_elements_by_tag_name("option")
#     for option in all_options:
#       #print("Value is: %s" % option.get_attribute("value"))
#       if  option.get_attribute("value") == '1900':
#         print("clicked")
#         option.click()
        

#     driver.find_element_by_xpath("//div[(@class = 'main_content_ctn')]/div[@class = 'agegate_text_container btns']/a[1]").click() 
#     wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'game_area_purchase_game')))
   
#   return driver.current_url


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
      ##print(raw_html)
    #Get description
      xpath_for_names = "//div[@class='games-list']/div[@class='item']/div[2]/a/text()"
      Game_names = html.xpath(xpath_for_names)
      #print(Game_names)
      raw_names= raw_names +  [game_name.replace(" System Requirements", "") for game_name in Game_names]
      

    
      elem = driver.find_element_by_class_name("next").click()
 

  
  
 
  
  
  
  return raw_names


# def Get_names(link):
 

  
  
#   print(f"Scraping {link} ..."  )
#   headers = {'Content-Type': 'text/html',}
  
#   response = requests.get(link, headers=headers)
 
#   raw_html = response.text
#   html = etree.HTML(raw_html)
#   ##print(raw_html)
# #Get description
#   xpath_for_names = "//div[@id='site_wrap']/article/div/h2/text()"
#   Game_names = html.xpath(xpath_for_names)
#   #print(Game_names)
#   return Game_names

##Get_names('https://www.pcgamesn.com/best-pc-games')
#print(names_)
#print(scrap_page_steam(steam_link))
