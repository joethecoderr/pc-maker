import re
import lxml.html as html
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
        
    def search_hardware(self, hardware):
        if re.search('amazon.com.mx', self.url):
            try:
                search_bar_elementid = 'twotabsearchtextbox'
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

        #r = requests.get(driver.current_url)
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
            