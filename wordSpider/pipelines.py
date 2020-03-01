# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from .spiders.const import Const


# 根据爬取的item组合成一个word词条，并返回此词条
def combine_word(item):
    word = ''.join([item['word_name'] + '   ' + '<英' + item['phonetic_En'] + '> <美' + item['phonetic_Am'],
                    '>\n',
                    item['paraphrase']])
    return word


class WordspiderPipeline(object):
    def __init__(self):
        print('\n***初始化pipeline***\n')
        self.target = open(Const.TARGET_FILE, 'w', encoding='utf-8')

    def process_item(self, item, spider):
        word = combine_word(item)
        self.target.write(word)
        return item

    def close_spider(self, spider):
        self.target.close()