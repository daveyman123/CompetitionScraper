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
        name = "AStorageInnWeidmanblah"

        
	
	allowed_domains = ['https://storageinns.net']
	start_urls = ['http://www.storageinns.net/p/self_storage/sizes_prices_9703/ballwin-mo-63011/a-storage-inn-ballwin-9703']

	def parse(self, response):
                
                display = Display(visible=0, size=(800, 600))
                display.start()
                TAG_RE = re.compile(r'<[^>]+>')

                def remove_tags(text):
                    return TAG_RE.sub('', text)
                
                url='http://www.storageinns.net/p/self_storage/sizes_prices_9703/ballwin-mo-63011/a-storage-inn-ballwin-9703'
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
		outside_units = ["4 x 6", "5 x 6", "6 x 8", "6 x 12", "8 x 10", "10 x 14", "10 x 12,", "10 x 16","10 x 10","10 x 20","10 x 25", "10 x 30"]
		
		#print soup.findAll('span',{"class":"sss-unit-size"})
		
                
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                
                sizeTagz = soup.findAll('div',{"class":"sitelink_classic_unit_cell unit-size size_width"})
		
		
		rateTagz = soup.findAll('span',{"class":"unit_rate rate "})
		
		
                #specialTagz2 = soup.findAll('div',{"class":"srp_label"})
		specialTagz = soup.findAll('div',{"class":"sitelink_classic_unit_cell unit-special special_size"})
		typesTagz = soup.findAll('span',{"class":"unit-marketing_name"},)
		
		yield {'date': datetime.datetime.now().strftime("%m-%d"),
                'name': "A Storage Inn Weidman"
                       }
		size = []
		for n in range(len(sizeTagz)):
                        #specialTagz = re.sub('<[^<]+?>', '', specialTagz)
                        #print specialTagz[n].get_text()
                        x = (sizeTagz[n]).get_text()
                        #x = re.sub('[*]', '', x)
                        #x = x.replace(' ', '')
                        #print x
                        #print x
                        print len(rateTagz)
			print len(sizeTagz)
                        
                        #if "Outdoor" in (typesTagz[n]).get_text():
                                #print "Outdoor hit"
                        
                        
                       # for sizes in outside_units:
                         #       sizes = sizes.replace("'", '')
                         #       if sizes in x:
                                 #               print "right size"
                          #              if x not in size:
                                
                              #                  size.append(x)
                               # #size.append(re.findall(r'\d+',(sizeTagz2[n]).get_text()))
                                  #                      print "logic hit"
                                #                x = re.sub(',', 'x', x)
                                #                x = re.findall(r'\d+', x)
                                #                x = " ".join(str(i) for i in x)
                                #                y = y.replace(' ', '')
                        y = specialTagz[n].get_text()
                        y = y.replace(' ', '')
                        y = y.strip('\n')
                        y = y.replace('\n','')        
                        try:
                                if x in outside_units:
                                        yield {
                        #soup.findAll('p',{"class":"icon-bg"})
                        #'name': soup.find('strong', {'class':'high'}).text
                       
                
                        "special": y,
                        "rate": rateTagz[n].get_text(),
                        'size': x,
                        "types": typesTagz[n].get_text()
	
		}
                        except IndexError:
                                yield {
                        #soup.findAll('p',{"class":"icon-bg"})
                        #'name': soup.find('strong', {'class':'high'}).text
                       
                
                        "special": y,
                        "rate": "none",
                        'size': x,
                        "types": "Outside"}
                driver.close()
