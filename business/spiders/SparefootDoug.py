import scrapy
from scrapy.selector import Selector
from business.items import TesttestItem
import datetime
import re
class MySpider(scrapy.Spider):
	name = "SparefootDoug"
	
	allowed_domains = ['https://www.sparefoot.com']
	start_urls = ['https://www.sparefoot.com/St-Peters-MO-self-storage/St-Peters-Storage-199893.html']

	def parse(self, response):
		info = response.css('.unit-min-height')
		items = []
		inside = "Indoor"
                outside = "Outdoor"
		inside_units = ["5' x 5'", "5' x 10'"]
		outside_units = ["10' x 15'","5' x 6'", "6' x 5'", "6' x 12'","10' x 10'","10' x 20'","10' x 25'","10' x 30'", "10' x 16'", "10' x 12'", "10' x 14'", "12' x 12'",]
		yield {'date': datetime.datetime.now().strftime("%m-%d-%y"),
                       'name': "Extra Space"
                       }
		for i in info:
                    
                    print i.css(".js-unit-label strong::text").extract_first()
                    for units in outside_units:
                            if units in i.css(".js-unit-label strong::text").extract_first() and 'drive up access' in i.css(".listing-unit-amenity:nth-child(1) span::text").extract_first():
                                yield {
			
                                        "special": "none",
                                        "rate": i.css(".price::text").extract_first(),
                                        "size": i.css(".js-unit-label strong::text").extract_first(),
                                        "types": i.css(".listing-unit-amenity:nth-child(1) span::text").extract_first()
	
		}

                

