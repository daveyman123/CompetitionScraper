import scrapy
import csv
from scrapy.selector import Selector
from business.items import TesttestItem
from business import settings
import datetime
import re
class MySpider(scrapy.Spider):
	name = "StorageMasters94"
	
	allowed_domains = ['https://www.selfstorage.com']
	start_urls = ['https://www.selfstorage.com/self-storage/missouri/st-charles/storage-masters-st-charles-64476/']

	def parse(self, response):
		titles = response.css('.facility-unit--storage')
                outside_units = ["5' x 5'","5' x 15'","5' x 10'","8' x 10'","10' x 10'","10' x 15'","10' x 20'","10' x 24'","10' x 25'","10' x 30'"]
                inside_units = ["5' x 5'", "5' x 10'"]
                inside = "Indoor"
                outside = "Outdoor"
                
		yield {'date': datetime.datetime.now().strftime("%m-%d"),
                       'name': "Storage Masters"
                       }
		for i in titles:
                    item = TesttestItem()
                    item ["special"] = i.css(".promo::text").extract_first()

                    if i.css(".unit-size::text").extract_first() in outside_units and "Drive" in i.css("li:nth-child(3)::text").extract_first():
                            
                            print "second logic"
                            yield {
                            
                        'special': "incomplete",
                        'types': i.css("li:nth-child(3)::text").extract_first(),
                        'size': i.css(".unit-size::text").extract_first(),  
                        'rate': i.css(".unit-price::text").extract()
                        }
                
                
                

