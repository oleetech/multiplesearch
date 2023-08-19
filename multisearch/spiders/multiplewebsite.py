import scrapy
from urllib.parse import quote
from multisearch.items import MultisearchItem
import re
class MultiplewebsiteSpider(scrapy.Spider):
    name = "multiplewebsite"
    allowed_domains = ["startech.com.bd", "ultratech.com.bd","techlandbd.com","vibegaming.com.bd","selltech.com.bd"]

    def start_requests(self):
        search_query = self.settings.get('SEARCH_QUERY')
        start_urls = [
            f"https://www.startech.com.bd/product/search?search={quote(search_query)}",
            f"https://www.ultratech.com.bd/index.php?route=product/search&search={quote(search_query)}",
            f"https://www.techlandbd.com/index.php?route=product/search&search={quote(search_query)}",
            f"https://www.vibegaming.com.bd/?s=+{quote(search_query)}",
            f"https://selltech.com.bd/intel-core-i3-10105-10th-gen-processor?search={quote(search_query)}"
            
      
            
        ]
        
        for url in start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        if 'startech' in response.url:
            for index, link in enumerate(response.css('div.p-item h4.p-item-name a'), start=1):
                product_link = link.attrib['href'] 
            
                yield response.follow(product_link,self.parse_startech)
                if index == 1:
                    break  

        elif 'ultratech' in response.url:
            for index, link in enumerate(response.css('div.image a.product-img '), start=1):
                product_link = link.attrib['href'] 
            
                yield response.follow(product_link,self.parse_ultratech)
                if index == 1:
                    break                  
        elif 'techlandbd' in response.url:
            for index, link in enumerate(response.css('div.name a '), start=1):
                product_link = link.attrib['href'] 
            
                yield response.follow(product_link,self.parse_techlandbd)
                if index == 1:
                    break  
              

        elif 'vibegaming' in response.url:
            for index, link in enumerate(response.css('a.post-title'), start=1):
                product_link = link.attrib['href'] 
            
                yield response.follow(product_link,self.parse_vibegaming)    
                if index == 1:
                    break                  
                
        elif 'selltech' in response.url:
            for index, link in enumerate(response.css('.name a'), start=1):
                product_link = link.attrib['href'] 
            
                yield response.follow(product_link,self.parse_selltech)    
                if index == 1:
                    break     
                
                                                     
    def parse_startech(self, response):
        item = MultisearchItem()
        item['seller'] = 'startech'
        item['title'] = response.css('div.product-short-info h1.product-name::text').get()
        price_with_symbol = response.css('td.product-price::text').get()

        if price_with_symbol:
            # Remove the dollar sign from the price
            numeric_price = re.sub(r'[^0-9]', '', price_with_symbol)

            item['price'] =    numeric_price
        yield item  

    def parse_ultratech(self, response):
        item = MultisearchItem()
        item['seller'] = 'ultratech'      
        item['title']  = response.css('.page-title::text').get() 
        price_with_symbol = response.css('div.product-price-new::text').get() 
        if price_with_symbol:
            # Remove the dollar sign from the price
            # Remove the dollar sign from the price
            numeric_price = re.sub(r'[^0-9]', '', price_with_symbol)

            item['price'] =    numeric_price

                  
        yield item  
        
    def parse_techlandbd(self, response):
        item = MultisearchItem()
        item['seller'] = 'techlandbd'      
        item['title']  = response.css('.page-title::text').get() 
        price_with_symbol = response.css('div.product-price::text').get() 
        if price_with_symbol:
            # Remove the dollar sign from the price
            # Remove the dollar sign from the price
            numeric_price = re.sub(r'[^0-9]', '', price_with_symbol)

            item['price'] =    numeric_price

                  
        yield item  
        
    def parse_vibegaming(self, response):
        item = MultisearchItem()
        item['seller'] = 'vibegaming'      
        item['title']  = response.css('.entry-title::text').get()
        price_with_symbol = response.xpath('//span[@class="woocommerce-Price-currencySymbol"]/following-sibling::text()').get()

        if price_with_symbol:
            # Remove commas, decimal points, and convert to int
            price_int = int(price_with_symbol.replace(',', '').split('.')[0] )


            item['price'] =    price_int

                  
        yield item          
       
    def parse_selltech(self, response):     
        item = MultisearchItem()
        item['seller'] = 'selltech'      
        item['title']  = response.css('.page-title::text').get()
        
        price_with_symbol = response.css('.product-price-new::text').get()

        if price_with_symbol:
            # Remove the dollar sign from the price
            numeric_price = re.sub(r'[^0-9]', '', price_with_symbol)

            item['price'] =    numeric_price
        yield item  
        
                

        
  