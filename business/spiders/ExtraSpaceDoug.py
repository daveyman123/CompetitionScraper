import scrapy
from scrapy.selector import Selector
from business.items import TesttestItem
import datetime
import re
from scrapy.utils.markup import remove_tags

from bs4 import BeautifulSoup
class MySpider(scrapy.Spider):
	name = "ExtraSpaceDoug22"
	
	allowed_domains = ['https://www.extraspace.com']
	start_urls = ['https://www.extraspace.com/Storage/Facilities/US/Missouri/St._Peters/1000000466/Facility.aspx']

	def parse(self, response):
		info = response.css('.unit')
		items = []
		inside = "Indoor"
                outside = "Outdoor"
		inside_units = ["5' x 5'", "5' x 10'"]
		outside_units = ["10' x 24'","5' x 5'", "10' x 15'","5' x 6'", "6' x 12'","10' x 10'","10' x 20'","10' x 25'","10' x 30'", "10' x 16'", "10' x 12'", "10' x 14'", "12' x 12'",]
		yield {'date': datetime.datetime.now().strftime("%m-%d"),
                       'name': "Extra Space"
                       }
		for i in info:
                    rate = (i.css(".promo, .promo span::text").extract_first())
                    print len(info)
		   
		    rate2 = i.css(".strikeout+ .rate div::text").extract_first()
		    
                    rate = remove_tags(rate)
                    #print i.css(".RamaGothicSemiBold div:nth-child(1)::text").extract_first()   
                    if i.css(".RamaGothicSemiBold div:nth-child(1)::text").extract_first() in outside_units and rate2 != None and 'Drive-Up Access' in i.css("li:nth-child(2)::text").extract_first():
                        yield {
			
                                        "special": rate,
                                        "rate": rate2,
                                        "size": i.css(".RamaGothicSemiBold div:nth-child(1)::text").extract_first(),
                                        "types": i.css("li:nth-child(2)::text").extract_first()
	
		}

                

