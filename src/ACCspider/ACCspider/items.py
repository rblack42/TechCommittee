# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AccspiderItem(scrapy.Item):
    # define the fields for your item here like:
    course = scrapy.Field()
    synonym = scrapy.FIeld()
    room = scrapy.Field()
    days = scrapy.Field()
    time = scrapy.Field()
    instructor = scrapy.Field()
