# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HeadportraitItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    #测试分类
    cateages=scrapy.Field()