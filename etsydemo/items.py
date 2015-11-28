# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

def serialize_description(value):
    return '\n'.join(value)

class EtsyItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field(serializer=serialize_description)
    tags = scrapy.Field()

