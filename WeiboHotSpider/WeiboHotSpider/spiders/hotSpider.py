# -*- coding: utf-8 -*-

import sys
import scrapy

from WeiboHotSpider import items





class hotSpider(scrapy.Spider):

    name = "hotSpider"

    allowed_domains = ['s.weibo.com']

    start_urls = ['https://s.weibo.com/top/summary?cate=realtimehot']

    def parse(self, response):

        item = items.WeibohotspiderItem()
        tr = response.xpath("//tr")

        for sel in tr:


            NO = sel.xpath("td[@class='td-01 ranktop']/text()").extract()
            if NO:
                item['NO'] = NO[0].encode('utf-8')


            keyword = sel.xpath("td[@class='td-02']/a/text()").extract()
            if keyword:
                item["keyword"] = keyword[0].encode('utf-8')

            state = sel.xpath("td[@class='td-03']/i/text()").extract()
            if state:
                item["state"] = state[0].encode('utf-8')

            hot = sel.xpath("td[@class='td-02']/span/text()").extract()
            if hot:
                item["hot"] = hot[0].encode('utf-8')


            href = sel.xpath("td[@class='td-02']/a/@href").getall()
            if href:
                item["href"] = "https://s.weibo.com" + href[0].encode('utf-8')

            yield item








