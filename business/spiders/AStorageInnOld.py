import scrapy
import csv
from scrapy.selector import Selector
from business.items import TesttestItem
from business import settings
import datetime
import re
class MySpider(scrapy.Spider):
	name = "astorageinn22"
	
	allowed_domains = ['https://www.storageinns.net']
	start_urls = ['http://www.storageinns.net/p/self_storage/sizes_prices_9709/saint-louis-mo-63129/a-storage-inn-st-louis-lemay-ferry-9709']

	def parse(self, response):
		titles = response.css('.unit-row')
                outside_units = ["5' x 15'","8' x 10'","10' x 10'","10' x 20'","10' x 25'","10' x 30'"]
                inside_units = ["5' x 5'", "5' x 10'"]
                inside = "Indoor"
                outside = "Outdoor"
                
		yield {'date': datetime.datetime.now().strftime("%m-%d"),
                       'name': "AStorageInn Lemay"
                       }
		for i in titles:
                    #item = TesttestItem()
                    #item ["special"] = i.css(".promo::text").extract_first()
                    rate = i.css(".rate::text").extract()
                    #if i.css(".RamaGothicSemiBold div:nth-child(1)::text").extract_first() in outside_units and "Drive" in i.css("li:nth-child(2)::text").extract_first():
                    if i.css(".rate::text").extract() == []:
                        rate = "call for details"
                                #print "second logic"
                    #if i.css(".RamaGothicSemiBold div:nth-child(1)::text").extract_first() in outside_units and "Drive" in i.css("li:nth-child(2)::text").extract_first():
                    if "Outside" in i.css(".amenities+ .amenities::text").extract_first():       
                            #print "second logic"
                        yield {
                            
                        'special': i.css(".special_rate::text").extract_first(),
                        'types': i.css(".amenities+ .amenities::text").extract_first(),
                        'size': i.css(".size_width::text").extract_first(),  
                        'rate': rate
                        }
