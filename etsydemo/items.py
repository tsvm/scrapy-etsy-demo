# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

def serialize_description(value):
    return '\n'.join(value)

def serialize_favorites(value):
    return value[0].partition(' ')[0]

def serialize_extract_first_word(value):
    return value[0].strip().partition(' ')[0]

class EtsyItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field(serializer=serialize_description)
    tags = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    reviews = scrapy.Field()
    views = scrapy.Field(serializer=serialize_extract_first_word)
    favorites = scrapy.Field(serializer=serialize_extract_first_word)
    treasury_lists = scrapy.Field(serializer=serialize_extract_first_word)
