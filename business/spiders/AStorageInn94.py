import scrapy
import csv
from scrapy.selector import Selector
from business.items import TesttestItem
from business import settings
import datetime
import re
class MySpider(scrapy.Spider):
	name = "AStorageInn9422"
	
	allowed_domains = ['https://www.storageinns.net']
	start_urls = ['http://www.storageinns.net/p/self_storage/sizes_prices_9707/saint-charles-mo-63303/a-storage-inn-highway-94-9707']

	def parse(self, response):
		titles = response.css('.unit-row')
                outside_units = ["10 x 16","5 x 6", "6 x 12","8 x 10","10 x 12","12 x 12", "10 x 24", "10 x 16"]

                inside_units = ["5' x 5'", "5' x 10'"]
                inside = "Indoor"
                outside = "Outdoor"
                
		yield {'date': datetime.datetime.now().strftime("%m-%d"),
                       'name': "Ninety Four"
                       }
		for i in titles:
                    print len(titles)
		    x = i.css(".special_size , .special_rate::text").extract_first()
		    x = x.replace('\n','')
		    x = x.replace(' ', '')
		    x = re.sub('<[^<]+?>', '', x)
                    if len(x) < 3:
			x = "none"
                    if i.css(".size_width::text").extract_first() in outside_units and "Drive" in i.css(".unit-marketing_name::text").extract_first():
                            
                            print "second logic"
                            yield {
                            
                        'special': x,
                        'types': "Outside",#i.css(".unit-marketing_name::text").extract_first(),
                        'size': i.css(".size_width::text").extract_first(),  
                        'rate': i.css(".no-inventory div , .rate::text").extract()
                        }
                
                
                

