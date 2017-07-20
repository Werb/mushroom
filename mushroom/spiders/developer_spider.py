# -*- coding: utf-8 -*-
import scrapy

from mushroom.items import DeveloperItem

class developerSpider(scrapy.Spider):
    name = "developers"

    def parse(self, response):
        items = []
        for developers in response.xpath('//li[@class = "d-sm-flex flex-justify-between border-bottom border-gray-light py-3"]'):
            item = DeveloperItem()
            item['userName'] = developers.xpath('normalize-space(.//div[2][@class = "mx-2"]//a/text())').extract_first()
            item['nickName'] = developers.xpath('normalize-space(.//div[2][@class = "mx-2"]//a//span[@class = "text-gray text-bold"]/text())').extract_first()
            item['userIcon'] = developers.xpath('normalize-space(.//div[1][@class = "mx-2"]//a//img/@src)').extract_first()
            item['popReposName'] = developers.xpath('normalize-space(.//a[@class = "repo-snipit css-truncate"]//span[@class = "repo"]/text())').extract_first()
            item['popReposDesc'] = developers.xpath('normalize-space(.//a[@class = "repo-snipit css-truncate"]//span[@class = "repo-snipit-description css-truncate-target"]/text())').extract_first()
            item['popReposUrl'] = "https://www.github.com/" + item['popReposName']
            items.append(item)
        return items
