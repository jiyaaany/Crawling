# -*- coding: utf-8 -*- 

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# class craigslist_crawler(object):
#     def __init__(self,contry,adults,oym,iym):
#         self.contry = contry
#         self.adults = adults
#         self.oym = oym
#         self.iym = iym
#         self.url = f"https://www.skyscanner.co.kr/transport/flights/sela/bki/?adults={adults}&children=0&adultsv2=4&childrenv2=&infants=0&cabinclass=economy&rtn=1&preferdirects=true&outboundaltsenabled=false&inboundaltsenabled=false&oym={oym}&iym={iym}&ref=home&selectedoday=01&selectediday=01"
#         self.driver = webdriver.Chrome("/Users/jiyaaany/Downloads/chromedriver.exe")
#         self.delay = 5

#     def load_page(self):
#         driver = self.driver
#         driver.get(self.url)
#         all_data = driver.find_elements_by_class_name("bpk-calendar-grid__date-32uj7")
#         for data in all_data:
#             print(data.text) 


# # https://www.skyscanner.co.kr/transport/flights/sela/bki/?adults=4&children=0&adultsv2=4&childrenv2=&infants=0&cabinclass=economy&rtn=1&preferdirects=true&outboundaltsenabled=false&inboundaltsenabled=false&oym=2008&iym=2010&ref=home&selectedoday=01&selectediday=01

# contry = 'bki'
# adults = 4
# # 출발 
# oym = 2010
# # 도착
# iym = 2010
# crawler = craigslist_crawler(contry, adults, oym, iym)
# crawler.load_page()

class craigslist_crawler(object):
    def __init__(self, query, max_price):
        self.max_price = max_price
        self.query = query
        self.url = f"http://seoul.craigslist.org/search/sss?query={query}&max_price={max_price}"
        self.driver = webdriver.Chrome("/Users/jiyaaany/Downloads/chromedriver.exe")
        self.delay = 5

    def load_page(self):
        driver = self.driver
        driver.get(self.url)
        all_data = driver.find_elements_by_class_name("result-row")
        for data in all_data:
            print (data.text)

        
query = "iphone"
max_price = "500"
crawler = craigslist_crawler(query, max_price)
crawler.load_page()