from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ElementNotVisibleException
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import requests
import lxml.html as html
import re
import warnings
warnings.filterwarnings('ignore')


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
    html_list_min = parsed.xpath('//*[@id="srl-main"]/div[2]/div[2]/main/div/div[1]/div/div/div[4]/div[2]/div/ul/li//text()')
    html_list_min_joined = [html_list_min[i] + html_list_min[i+1] for i in range(0, len(html_list_min)-1, 2)]
    print(html_list_min_joined)
    html_list_rec = parsed.xpath('//*[@id="srl-main"]/div[2]/div[2]/main/div/div[1]/div/div/div[4]/div[4]/div/ul/li//text()')
    html_list_rec_joined = [html_list_rec[i] + html_list_rec[i+1] for i in range(0, len(html_list_rec)-1, 2)]
    print(html_list_rec_joined)
    for element in range(len(html_list_min_joined)- 1):
      hw, spec = html_list_min_joined[element].split(':')
      tple = (hw, spec)
      list_tokenized_min.append(tple)
      tple = ()
    for element in range(len(html_list_rec_joined) - 1):
      hw, spec = html_list_rec_joined[element].split(':')
      tple = (hw, spec)
      list_tokenized_rec.append(tple)
      tple = ()
  except:
    return []
  return list_tokenized_min or [], list_tokenized_rec or []


def loop(game):
    try:
        url = 'https://www.systemrequirementslab.com/cyri'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-startup-window')
        driver = webdriver.Chrome('chromedriver.exe', chrome_options=chrome_options)
        wait = WebDriverWait(driver,40)
        driver.get(url)
        tempu = driver.find_element_by_class_name('select2-selection__rendered')
        tempu.click()
        inputText = driver.find_element_by_class_name('select2-search__field')
        inputText.send_keys(game)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'select2-results')))
        element = driver.find_element_by_class_name('select2-results__options')
        element.click()
        current_url = driver.current_url
        wait.until(EC.element_to_be_clickable((By.ID, 'button-cyri-bigblue')))
        button = driver.find_element_by_id('button-cyri-bigblue')
        button.click()
        WebDriverWait(driver, 15).until(EC.url_changes(current_url))
        driver.current_url
        r = requests.get(driver.current_url)
        driver.close()
        return r
    except TimeoutException:
        print('Timeout, will skip to next game')
    else:
        r = requests.get('http://quotes.toscrape.com/')
        r.status_code = 100
        print(r.status_code)
        return r



def scrape(game):

    r = loop(game)
    minimun = []
    rec = []
    amazon_ = []
    if  r.status_code == 200:
        time.sleep(1.5)
        minimun, rec = min_rec_systemreq(r)
        amazon_ = []
        
    return amazon_ , minimun, rec
