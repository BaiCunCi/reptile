# -*- coding: utf-8 -*-
import scrapy
from  py_scrapy_first.items import PyScrapyFirstItem
from  scrapy.http import Request
class PcDangdangSpider(scrapy.Spider):
    name = 'pc_dangdang'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=python&act=input&page_index=1']

    def parse(self, response):
        item=PyScrapyFirstItem()
        item["title"]=response.xpath("//p[@name='title']/a/@title").extract()
        item["link"]=response.xpath("//p[@name='title']/a/@href").extract()
        item["comment"]=response.xpath("//p/a[@class='search_comment_num']/text()").extract()
        yield  item
        for i in range(1,101):
            url="http://search.dangdang.com/?key=python&act=input&page_index="+str(i)
            print(url)
            yield Request(url,callback=self.parse)
