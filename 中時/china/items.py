# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinaItem(scrapy.Item):

    url = scrapy.Field()
    title = scrapy.Field()
    catagory = scrapy.Field()
    publish_time = scrapy.Field()
    content = scrapy.Field()
