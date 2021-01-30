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

def get_game_link(game):
    
         
        print(f"Getting page for {game} ..."  )
        
        driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
        driver.get("https://www.pcgamebenchmark.com/")
        assert "PCGameBenchmark" in driver.title #assert is for debugging, if the condition is false, AssertionError is raised. 
        #Here we are using it to confirm that the title has "Steam".
        wait = WebDriverWait(driver,10)
        elem = driver.find_element_by_xpath("//form[(@id = 'search')]/span/input[@name = 'q']")
        elem.clear()
        elem.send_keys(game)
        
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'tt-open')))
        
        elem.send_keys(Keys.ENTER)
        print(driver.current_url)
        
        
        return driver.current_url

def scrap_page(game):
    game_url = get_game_link(game)
    print(f"Scraping {game_url} ..."  )
    headers = {'Content-Type': 'text/html',}
    response = requests.get(game_url, headers=headers)
    raw_html = response.text
    html = etree.HTML(raw_html)
    
    #Get description
    xpath_for_description = "//div[(@id = 'details-meta')]/div[@class = 'description']/p/text()"
    description_txt = html.xpath(xpath_for_description)
    
    #Get Minimum Requirements
    xpath_for_min_req_strongs = "//div[(@class = 'row requirements')]/div[2]/ul/li/strong/text() | //div[(@class = 'requirements')]/ul[2]/li/strong/text()"# with | like an or, we will use either one of the xpath (If we want to add other 'or' python has problems)
    xpath_for_min_req = "//div[(@class = 'row requirements')]/div[2]/ul/li[strong]/text() | //div[(@class = 'requirements')]/ul[2]/li[strong]/text()" #With [] we say to look for those li with strong
    min_req_strongs = html.xpath(xpath_for_min_req_strongs)
    min_req_txt = html.xpath(xpath_for_min_req)
    
    #Get Recommended Requirements
    
    xpath_for_recommended_req_strongs = "//div[(@class = 'row requirements')]/div[1]/ul/li/strong/text() | //div[(@class = 'requirements')]/ul[1]/li/strong/text()"
    xpath_for_recommended_req = "//div[(@class = 'row requirements')]/div[1]/ul/li[strong]/text() | //div[(@class = 'requirements')]/ul[1]/li[strong]/text()"#With [] we say to look for those li with strong
    recommended_req_strongs = html.xpath(xpath_for_recommended_req_strongs)
    recommended_req_txt = html.xpath(xpath_for_recommended_req)
    
    #Merge strongs and text in the same array
    merged_list_min = [(min_req_strongs[i], min_req_txt[i]) for i in range(0, len(min_req_strongs))]
    merged_arr_min =np.array(merged_list_min)
    
    merged_list_rec = [(recommended_req_strongs[i], recommended_req_txt[i]) for i in range(0, len(recommended_req_strongs)) ]
    merged_arr_recommended = np.array(merged_list_rec)
    
    
    return description_txt, merged_arr_min, merged_arr_recommended
  
##pcgamebenchmark_link = get_game_link_pcgbm("cyberpunk 2077")
#print(scrap_from_pcgbm(pcgamebenchmark_link))