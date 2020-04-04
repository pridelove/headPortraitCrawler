# -*- coding: utf-8 -*-
import scrapy
from headPortrait.items import HeadportraitItem

class HpcrawlerSpider(scrapy.Spider):
    name = 'Hpcrawler'
    allowed_domains = ['m.woyaogexing.com']
    start_urls = ['https://m.woyaogexing.com/touxiang/katong/index_2.html']

    def parse(self, response):
        # 获取整个页面的链接
        picUrl = response.xpath('//div//ul[@class="g-piclist-container"]//li//img//@data-src').getall()
        #进行链接格式化 response.urljoin(url) 自动对链接进行格式化
        newUrl = list(map(lambda url: response.urljoin(url), picUrl))
        #print(newUrl)
        #把item传入到pipelines
        item = HeadportraitItem(image_urls=newUrl,cateages='Ceshi')
        yield item