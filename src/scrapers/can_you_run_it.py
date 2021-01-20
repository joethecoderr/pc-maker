from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ElementNotVisibleException
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import lxml.html as html
import re


class WebShop():
    def __init__(self, url):
        self.url = url
    
    def get_shop_name(self):
        name = re.search('https?://www.([A-Za-z_0-9.-]+).*', self.url) 
        return name.group(1)
    
    def go_to_webshop(self, driver):        
        driver.get(self.url)

    def get_search_bar_xpath(self):
        if re.search('amazon.com.mx', self.url):
            xpath_search_bar = '/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input'
            return xpath_search_bar
        else:
            return None

    def search_hardware(self, hardware, driver):
        if re.search('amazon.com.mx', self.url):
            try:
                search_bar_elementid = 'twotabsearchtextbox'
                wait = WebDriverWait(driver,40)
                wait.until(EC.visibility_of_element_located((By.ID, 'twotabsearchtextbox')))
                inputText = driver.find_element_by_id(search_bar_elementid)
                inputText.send_keys(hardware)
                inputText.send_keys(u'\ue007')
            except:
                return None
        else:
            pass
    def get_first_three_results(self, driver):
        xpaths = self.get_xpath_for_shop()
        recommendationsList = [] 
        dictTemp = {}
        html_home = driver.page_source
        parsed = html.fromstring(html_home)
        urls = parsed.xpath(xpaths['urls'])
        prices = parsed.xpath(xpaths['prices'])
        short_descr = parsed.xpath(xpaths['short_descr'])
        stars = parsed.xpath(xpaths['stars'])
        num_reviews = parsed.xpath(xpaths['num_reviews'])
        for i in range(3):
            try:
                dictTemp["short_descr"] = short_descr[i]
                dictTemp["url"] = urls[i]
               # dictTemp["price"] = prices[i]
                dictTemp["stars"] = stars[i]
                dictTemp["num_reviews"] = num_reviews[i]
                recommendationsList.append(dictTemp)
                dictTemp = {}
            except:
                pass
        return recommendationsList
    
    def get_xpath_for_shop(self):
        xpath_dict = {}
        if re.search('amazon.com.mx', self.url):
            urls = '//div[@id="search"]/div[@class="s-desktop-width-max s-desktop-content sg-row"]//div[@class="sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20"]//div[@class="a-section a-spacing-medium"]//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"]/a/@href'
            prices = '//div[@id="search"]/div[@class="s-desktop-width-max s-desktop-content sg-row"]//span[@data-component-id="7"]//span[@class="a-price"]/span[@class="a-offscreen"]/text()'
            short_description_article = '//div[@id="search"]/div[@class="s-desktop-width-max s-desktop-content sg-row"]//div[@class="sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20"]//div[@class="a-section a-spacing-medium"]//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"]/a/span/text()'
            stars = '//div[@id="search"]/div[@class="s-desktop-width-max s-desktop-content sg-row"]//div[@class="sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20"]//div[@class="a-section a-spacing-medium"]/div[@class="a-section a-spacing-none a-spacing-top-micro"]/div[@class="a-row a-size-small"]//span[@class="a-declarative"]//span[@class="a-icon-alt"]/text()'
            num_reviews = '//div[@id="search"]//div[@class="s-main-slot s-result-list s-search-results sg-row"]//div[@class="a-section a-spacing-none a-spacing-top-micro"]//a[@class="a-link-normal"]//span[@class="a-size-base"]/text()'
            xpath_dict = {
                'urls' : urls,
                'prices': prices,
                'short_descr': short_description_article,
                'stars': stars,
                'num_reviews': num_reviews
                         }
        else:
            pass
        return xpath_dict
            

def min_rec_systemreq(r):
  list_tokenized_min = []
  list_tokenized_rec = []
  tple = ()
  html_home = r.content.decode('utf-8')
  parsed = html.fromstring(html_home)
  try:
    html_list_min = parsed.xpath('//div[@class="list-line-height"]/ul[1]/li/text()')
    html_list_rec = parsed.xpath('//div[@class="list-line-height"]/ul[2]/li/text()')
    for element in range(len(html_list_min)- 1):
      hw, spec = html_list_min[element].split(':')
      tple = (hw, spec)
      list_tokenized_min.append(tple)
      tple = ()
    for element in range(len(html_list_rec) - 1):
      hw, spec = html_list_rec[element].split(':')
      tple = (hw, spec)
      list_tokenized_rec.append(tple)
      tple = ()
  except:
    return []
  return list_tokenized_min, list_tokenized_rec

def min_rec_systemreq2(driver):
  list_tokenized_min = []
  list_tokenized_rec = []
  tple = ()
#   html_home = r.content.decode('utf-8')
#   parsed = html.fromstring(html_home)
  try:
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="list-line-height"]/ul[1]/li/text()')))
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="list-line-height"]/ul[2]/li/text()')))
    html_list_min = driver.find_element_by_xpath('//div[@class="list-line-height"]/ul[1]/li/text()')
    print(html_list_min)
    html_list_rec == driver.find_element_by_xpath('//div[@class="list-line-height"]/ul[2]/li/text()')
    # html_list_min = parsed.xpath('//div[@class="list-line-height"]/ul[1]/li/text()')
    # html_list_rec = parsed.xpath('//div[@class="list-line-height"]/ul[2]/li/text()')
    for element in range(len(html_list_min)- 1):
      hw, spec = html_list_min[element].split(':')
      tple = (hw, spec)
      list_tokenized_min.append(tple)
      tple = ()
    for element in range(len(html_list_rec) - 1):
      hw, spec = html_list_rec[element].split(':')
      tple = (hw, spec)
      list_tokenized_rec.append(tple)
      tple = ()
  except:
    return []
  return list_tokenized_min, list_tokenized_rec

  

def scrape():
    url = 'https://www.systemrequirementslab.com/cyri'
    driver = webdriver.Chrome('chromedriver.exe')
    wait = WebDriverWait(driver,40)
    driver.get(url)
    inputText = driver.find_element_by_id('index_drop_input')
    inputText.send_keys('Call of duty')
    wait.until(EC.visibility_of_element_located((By.ID, 'tipue_drop_wrapper')))
    #time.sleep(1)
    element = driver.find_element_by_xpath('//div[@id="tipue_drop_wrapper"]/a')
    element.click()
    wait.until(EC.visibility_of_element_located((By.ID, 'cyri-search-button')))
    button = driver.find_element_by_xpath('//div[@id="cyri-search-button"]')
    button.click()
    r = requests.get(driver.current_url, timeout = 10)

    if r.status_code == 200:
        time.sleep(.5)
        minimun, rec = min_rec_systemreq(r)
        url_amazon = 'https://www.amazon.com.mx/'
        webshop = WebShop(url_amazon)
        webshop.go_to_webshop(driver)
        webshop.search_hardware(minimun[1][0] + minimun[1][1], driver)
        amazon_ = webshop.get_first_three_results(driver)
        return amazon_ or [], minimun or [], rec or []
