# -*- coding: utf-8 -*-
import scrapy
from .const import Const


# 能够连续产生单词的可迭代函数
def yield_word():
    with open(Const.SOURCE_FILE, 'r', encoding='utf-8') as source_file:
        for word in source_file:
            yield word


# 根据web prefix和待查询的word构建出查询结果的url
def build_url(prefix, word):
    return prefix + word


# 提取单词名称
def extract_word_name(response):
    return response.xpath('.//span[@class="keyword"]/text()').extract_first()


# 提取音标，返回 (英式音标， 美式音标)
def extract_phonetic(response):
    phonetic_nodes = response.xpath('.//span[@class="pronounce"]/span[@class="phonetic"]')
    phonetic_En = phonetic_nodes[0].xpath('./text()').extract_first()
    phonetic_Am = phonetic_nodes[1].xpath('./text()').extract_first()
    return phonetic_En, phonetic_Am


# 提取释义
def extract_paraphrase(response):
    res = str()
    for node in response.xpath('.//div[@class="trans-container"][1]/ul/li'):
        res += node.xpath('./text()').extract_first().split('\n', 1)[0] + '\n'
    return res


class MyspiderSpider(scrapy.Spider):
    name = 'mySpider'
    allowed_domains = []

    def start_requests(self):
        for word in yield_word():
            yield scrapy.Request(build_url(Const.WEB_PREFIX, word), callback=self.parse)

    def parse(self, response):
        item = dict()

        item['word_name'] = extract_word_name(response)  # 提取单词名

        item['phonetic_En'], item['phonetic_Am'] = extract_phonetic(response)  # 提取音标

        item['paraphrase'] = extract_paraphrase(response)  # 提取释义

        yield item
