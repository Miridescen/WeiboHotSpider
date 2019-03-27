# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeibohotspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    NO = scrapy.Field()
    keyword = scrapy.Field()
    state = scrapy.Field()
    hot = scrapy.Field()
    href = scrapy.Field()

    pass
