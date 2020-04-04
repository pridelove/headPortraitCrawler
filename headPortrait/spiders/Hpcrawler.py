# -*- coding: utf-8 -*-
import re

import scrapy
from headPortrait.items import HeadportraitItem
# 导入可以修改url 的模板
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class HpcrawlerSpider(CrawlSpider):
    name = 'Hpcrawler'
    allowed_domains = ['m.woyaogexing.com']
    start_urls = ['https://m.woyaogexing.com/touxiang/']

    # 规则定制
    rules = (
        Rule(LinkExtractor(allow=r'/touxiang/[a-z]{2,7}/'), callback="parse_detail", follow=True),
    )

    def parse_detail(self, response):
        print(response)
        # 获取标题
        title = response.xpath('//h1[@class="m-page-title"]/text()').get()
        print(title)
        # 存在标题 说明有图
        if title is not None:
            # 某些字符不能创建文件夹 防止出现这种情况 进行修正
            title = re.sub(r'[<||>.:?]+', '', title)
            # 获取原始图片链接
            image_urls = response.xpath('//img//@data-src').getall()
            # 链接格式化 带上https
            image_Urls = list(map(lambda url: response.urljoin(url), image_urls))
            item = HeadportraitItem(image_urls=image_Urls, title=title)
            yield item

