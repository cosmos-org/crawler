# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlPostItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    content = scrapy.Field()
    author = scrapy.Field()
    url_author = scrapy.Field()
    type = scrapy.Field()
    source = scrapy.Field()
    url = scrapy.Field()
    rating = scrapy.Field()
    comment_number = scrapy.Field()
    crawl_time = scrapy.Field()
    created_time = scrapy.Field()
    pass
