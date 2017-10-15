from scrapy.selector import HtmlXPathSelector
import scrapy
import csv
from scrapy.selector import Selector
from business.items import TesttestItem
from business import settings
import datetime
import re
from scrapy.item import Item, Field
class MyItem(Item):
	value = Field()

class MySpider(scrapy.Spider):
	name = "StorageMasters942"
	
	allowed_domains = ['https://www.extraspace.com']
	start_urls = ['http://www.storagemasters.net/locations/st-charles-mo/']
    	def parse(self, response):
        	#hxs = HtmlXPathSelector(response)
        	#sel = Selector(response)
                items = response.xpath('//*[@id="tabreservebody"]')
		print items
        	for item in items:
			print item
        	    	my_item = MyItem()
        	    	my_item['value'] = item.xpath('td[1]/text()').extract()
			#list = sel.xpath('.//text()')
        	    	yield my_item
         #       outside_units = ["5' x 5'","5' x 10'","5' x 15'","8' x 10'","10' x 10'","10' x 20'","10' x 25'","10' x 30'","10' x 24'", "10' x 15'"]
          #      inside_units = ["5' x 5'", "5' x 10'"]
           #     inside = "Indoor"
            #    outside = "Outdoor"
                
	#yield {'date': datetime.datetime.now().strftime("%m-%d"),
                      # 'name': "ExtraSpace"
                      # }
		#for row in response.selector.xpath('//*[(@id = "tabreservebody")]'):
		 #   print row
                  #  item = TesttestItem()
                   # item ["special"] = i.css(".promo::text").extract_first()

                    #if i.css(".RamaGothicSemiBold div:nth-child(1)::text").extract_first() in outside_units and "Drive" in i.css("li:nth-child(2)::text").extract_first():
                            
                     #       print "second logic"
                      #      yield {
                            
                       # 'special': i.css(".promo::text").extract_first(),
                        #'types': i.css("li:nth-child(2)::text").extract_first(),
                       # 'size': i.css(".RamaGothicSemiBold div:nth-child(1)::text").extract_first(),  
                       # 'rate': i.css(".strikeout+ .rate div::text").extract()
                       # }
                
                
                

