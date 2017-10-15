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
        name = "PublicStorageDoug"

        
	
	allowed_domains = ['https://www.publicstorage.com']
	start_urls = ['https://www.publicstorage.com/missouri/self-storage-st-charles-mo/63303-self-storage/1007?lat=38.79101&lng=-90.55954&location=saint+charles']

	def parse(self, response):
                
                url='https://www.publicstorage.com/missouri/self-storage-st-charles-mo/63303-self-storage/1007?lat=38.79101&lng=-90.55954&location=saint+charles'
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
		outside_units = ["10' x 15'","5' x 6'","5' x 5'", "10' x 24", "10' x 30'", "6' x 12'","10' x 10'","10' x 20'","10' x 25'","10' x 30'", "10' x 16'", "10' x 12'", "10' x 14'", "12' x 12'",]
		
		#print soup.findAll('span',{"class":"sss-unit-size"})
		
                
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                time.sleep(3)
                sizeTagz = soup.findAll('div',{"class":"srp_label srp_font_14"})
		
		
		rateTagz = soup.findAll('div',{"class":"srp_label alt-price"})
		
                specialTagz2 = soup.findAll('div',{"class":"srp_res_clm srp_clm90"})
		specialTagz = soup.findAll('div',{"class":"srp_v-space_10"})
		typesTagz = soup.findAll('ul',{"class":"srp_list"},)
		
		yield {
                'name': "Public Storage"
                       }
		size = []
		for n in range(len(sizeTagz)):
                        #print len(sizeTagz)
                        print (specialTagz2[n]).get_text()
                        #print (rateTagz[n]).get_text()
                        
                        if "Outside" in (typesTagz[n]).get_text():
                                if (sizeTagz[n]).get_text() in outside_units:
                                        if (sizeTagz[n]).get_text() not in size:
                                
                                                size.append((sizeTagz[n]).get_text())
                                #size.append(re.findall(r'\d+',(sizeTagz2[n]).get_text()))
                                                print "logic hit"
                
                                                yield {
                        #soup.findAll('p',{"class":"icon-bg"})
                        #'name': soup.find('strong', {'class':'high'}).text
                       
                
                        "special": (specialTagz2[n].get_text()).replace('\n', ''),#re.sub(r"(?<=[a-z])\r?\n"," ",(specialTagz2[n]).get_text()),
                        "rate": (rateTagz[n]).get_text(),
                        'size': ((sizeTagz[n]).get_text()),
                        "types": "Outside"
	
		}
                driver.close()
