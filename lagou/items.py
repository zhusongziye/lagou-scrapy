# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    day = scrapy.Field()
    salary = scrapy.Field()
    require = scrapy.Field()
    tag = scrapy.Field()
    keyWord = scrapy.Field()
    companyName = scrapy.Field()
    companyType = scrapy.Field()
    location = scrapy.Field()
