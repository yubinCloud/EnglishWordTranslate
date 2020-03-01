# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WordspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    word_name = scrapy.Field()  # 单词名
    phonetic_Am = scrapy.Field()   # 美式音标
    phonetic_En = scrapy.Field()   # 英式音标
    paraphrase = scrapy.Field()  # 释义
