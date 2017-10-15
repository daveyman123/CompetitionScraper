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
        name = "PublicStorageWeidman"

        
	
	allowed_domains = ['https://www.publicstorage.com']
	start_urls = ['https://www.publicstorage.com/missouri/self-storage-ballwin-mo/63021-self-storage/1071?lat=38.59582&lng=-90.47391&location=Ballwin']

	def parse(self, response):
                display = Display(visible=0, size=(800, 600))
                display.start()

                url='https://www.publicstorage.com/missouri/self-storage-ballwin-mo/63021-self-storage/1071?lat=38.59582&lng=-90.47391&location=Ballwin'
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
		outside_units = ["4' x 6'", "10' x 15'","5' x 6'", "6' x 8'", "6' x 12'","8' x 10'", "10' x 10'","10' x 20'","10' x 25'", "10' x 16'", "10' x 12'", "10' x 14'", "10' x 30'", "10' x 25'"]
		
		#print soup.findAll('span',{"class":"sss-unit-size"})
		
                
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
#                time.sleep(3)
                sizeTagz = soup.findAll('div',{"class":"srp_label srp_font_14"})
		
		
		rateTagz = soup.findAll('div',{"class":"srp_label alt-price"})
		
        #        specialTagz2 = soup.findAll('div',{"class":"srp_res_clm srp_clm90"})
	#	specialTagz = soup.findAll('div',{"class":"srp_v-space_10"})
		typesTagz = soup.findAll('ul',{"class":"srp_list"},)
		specialTagz2 = soup.findAll('div',{"class":"srp_res_clm srp_clm90"})
                #specialTag = specialTagz2.findAll('div',{"class":"srp_v-space_$
                x = []
                for foo in specialTagz2:
			if foo.find('div',{"class":"srp_label"}):
                        	bar = foo.find('div',{"class":"srp_label"}).text
                        	if "$1" in bar or "Free" in bar or "50%" in bar:
                                	x.append(bar)
                print len(x)
	
		yield {'date': datetime.datetime.now().strftime("%m-%d"),
                'name': "Public Storage"
                       }
		size = []
		for n in range(len(sizeTagz)):
                        print len(sizeTagz)
			print len(x)
#                        print (specialTagz2[n]).get_text()
                        #print (rateTagz[n]).get_text()
                        special = re.sub(r"(?<=[a-z])\r?\n"," ",(x[n]))
                        #if "Online" in special:
                         #       special = "None"
                        
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
                        "special": "Incomplete",
                        "rate": (rateTagz[n]).get_text(),
                        'size': ((sizeTagz[n]).get_text()),
                        "types": "Outside"
	
		}
                driver.close()
                
