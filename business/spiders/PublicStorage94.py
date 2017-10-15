import scrapy
from scrapy.selector import Selector
from business.items import TesttestItem
import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
import re
import time
from pyvirtualdisplay import Display



class MySpider(scrapy.Spider):
        name = "PublicStorage94"

        
	
	allowed_domains = ['https://www.publicstorage.com']
	start_urls = ['https://www.publicstorage.com/missouri/self-storage-st-charles-mo/63303-self-storage/918?PID=PSLocalSearch&CID=1341&CHID=LL']

	def parse(self, response):
                display = Display(visible=0, size=(800, 600))
                display.start()

                url='https://www.publicstorage.com/missouri/self-storage-st-charles-mo/63303-self-storage/918?PID=PSLocalSearch&CID=1341&CHID=LL'
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
		outside_units = ["5' x 5'","5' x 10'","5' x 15'","8' x 10'","10' x 10'","10' x 20'","10' x 25'","10' x 30'","10' x 24'", "10' x 15'"]
		
		#print soup.findAll('span',{"class":"sss-unit-size"})
		
                
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                time.sleep(3)
                sizeTagz = soup.findAll('div',{"class":"srp_label srp_font_14"})
		
		
		rateTagz = soup.findAll('div',{"class":"srp_label alt-price"})
		
                specialTagz2 = soup.findAll('div',{"class":"srp_res_clm srp_clm90"})
		specialTagz = soup.findAll('div',{"class":"srp_v-space_10"})
		typesTagz = soup.findAll('ul',{"class":"srp_list"},)
		
		yield {'date': datetime.datetime.now().strftime("%m-%d"),
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
                       
                #.replace('\n', '')
                        "special": "Incomplete",#re.sub(r"(?<=[a-z])\r?\n"," ",(specialTagz[n]).get_text()),
                        "rate": (rateTagz[n]).get_text(),
                        'size': ((sizeTagz[n]).get_text()),
                        "types": "Outside"
	
		}
                driver.close()
                
