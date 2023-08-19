import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose

def clean_text(text):
    return text.strip()

class MultisearchItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field(  
                         input_processor=MapCompose(clean_text),
                         output_processor=TakeFirst()
                         )
    price = scrapy.Field()
    seller = scrapy.Field()