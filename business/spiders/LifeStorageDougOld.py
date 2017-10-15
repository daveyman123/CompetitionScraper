import scrapy
from scrapy.selector import Selector
from business.items import TesttestItem
import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
import re
import time



class MySpider(scrapy.Spider):
        name = "LifeStorageDoug"

        
	
	allowed_domains = ['https://www.lifestorage.com']
	start_urls = ['https://www.lifestorage.com/storage-units/missouri/saint-louis/63376/460-in-saint-peters/?size=5x5']

	def parse(self, response):
                
                url='https://www.lifestorage.com/storage-units/missouri/saint-louis/63376/460-in-saint-peters/?size=5x5'
                driver = webdriver.Firefox()
                driver.get(url)

		#url2='http://www.a1lockerrental.com/self-storage/mo/st-louis/4427-meramec-bottom-rd-facility/unit-sizes-prices#/units?category=all'
		#driver2 = webdriver.Firefox()
                #driver2.get(url2)
                #html2 = driver.page_source
                #soup2 = BeautifulSoup(html2, 'html.parser')                
                #soup.append(soup2)
                #print soup
		items = []
		inside = "Indoor"
                outside = "Outdoor"
		inside_units = ["5 x 5", "5 x 10"]
		outside_units = ["10' x 15'","5' x 6'", "6' x 12'","10' x 10'","10' x 20'","10' x 25'","10' x 30'", "10' x 16'", "10' x 12'", "10' x 14'", "12' x 12'",]
		
		#print soup.findAll('span',{"class":"sss-unit-size"})
		
                
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                time.sleep(3)
                sizeTagz = soup.findAll('div',{"class":"storesRow"})
		
		
		rateTagz = soup.findAll('div',{"class":"priceBox"})
		
		
                #specialTagz2 = soup.findAll('div',{"class":"srp_label"})
		#specialTagz = soup.findAll('div',{"class":"srp_v-space_10"})
		typesTagz = soup.findAll('ul',{"class":"features"},)
		
		yield {
                'name': "Life Storage"
                       }
		size = []
		for n in range(len(sizeTagz)):
                        #print len(sizeTagz)
                        x = (sizeTagz[n]).get_text()
                        #x = re.sub('[*]', '', x)
                        #x = x.replace(' ', '')
                        #print x
                        #print x
                        print (rateTagz[n]).get_text()
                        
                        if "Outdoor" in (typesTagz[n]).get_text():
                                #print "Outdoor hit"
                                for sizes in outside_units:
                                        if sizes in x:
                                 #               print "right size"
                                                if x not in size:
                                
                                                        size.append(x)
                                #size.append(re.findall(r'\d+',(sizeTagz2[n]).get_text()))
                                  #                      print "logic hit"
                                                        x = re.sub('[*]', '', x)
                                                        x = x.replace(' ', '')
                                                        yield {
                        #soup.findAll('p',{"class":"icon-bg"})
                        #'name': soup.find('strong', {'class':'high'}).text
                       
                
                        "special": "None",
                        "rate": re.findall(r'^\D*(\d+)',(rateTagz[n]).get_text()),
                        'size': re.findall(r'\d+', x),
                        "types": "Outside"
	
		}
                driver.close()
                
