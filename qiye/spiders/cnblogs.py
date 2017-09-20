# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from qiye.items import QiyeItem

class CnblogsSpider(scrapy.Spider):
    name = 'cnblogs'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://www.cnblogs.com/qiyeboy/default.html?page=1']

    def parse(self, response):
        # pass
        papers = response.xpath('.//*[@class="day"]')

        for paper in papers:
            title = paper.xpath('.//*[@class="postTitle"]/a/text()').extract_first()
            url = paper.xpath('.//div[@class="postTitle"]/a/@href').extract_first()
            time = paper.xpath('.//div[@class="dayTitle"]/a/text()').extract_first()
            content = paper.xpath('.//div[@class="c_b_p_desc"]/text()').extract_first()
            item = QiyeItem(url=url,title=title,time=time,content=content)
            yield item

            # print title,url,time
            # print content
        next_page = Selector(response).re(u'<a href="(\S*)">下一页</a>')
        if next_page:
            yield scrapy.Request(url=next_page[0],callback=self.parse)



            
