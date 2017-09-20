# -*- coding: utf-8 -*-
import scrapy


class CnblogsSpider(scrapy.Spider):
    name = 'cnblogs'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://www.cnblogs.com/qiyeboy/default.html?page=1']

    def parse(self, response):
        # pass
        papers = response.xpath('.//*[@class="day"]')

        for paper in papers:
            title = paper.xpath('.//*[@class="postTitle"]/a/text()').extract_first()
            
