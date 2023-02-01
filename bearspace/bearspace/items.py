# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BearspaceItem(scrapy.Item):

    url = scrapy.Field()
    title = scrapy.Field()
    raw_data = scrapy.Field()
    price_gbp = scrapy.Field()
