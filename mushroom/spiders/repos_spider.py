# -*- coding: utf-8 -*-
import scrapy

from mushroom.items import ReposItem
from mushroom.items import UserItem

class reposSpider(scrapy.Spider):
    name = "repos"

    def parse(self, response):
        items = []
        for repos in response.xpath('//li[@class = "col-12 d-block width-full py-4 border-bottom"]'):
            item = ReposItem()
            item['url'] = 'http://www.github.com' + repos.xpath('.//div[@class = "d-inline-block col-9 mb-1"]//h3//a/@href').extract()[0]
            item['reposName'] = repos.xpath('.//div[@class = "d-inline-block col-9 mb-1"]//h3//a/@href').extract_first()
            item['reposDesc'] = repos.xpath('normalize-space(.//p[@class = "col-9 d-inline-block text-gray m-0 pr-4"]/text())').extract_first()
            item['languageColor'] = repos.xpath('normalize-space(.//span[@class = "repo-language-color ml-0"]/@style)').extract_first()[17:24]
            item['languageType'] = repos.xpath('normalize-space(.//span[@itemprop = "programmingLanguage"]/text())').extract_first()
            item['star'] = repos.xpath('normalize-space(.//a[1][@class = "muted-link d-inline-block mr-3"])').extract_first()
            item['fork'] = repos.xpath('normalize-space(.//a[2][@class = "muted-link d-inline-block mr-3"])').extract_first()
            item['starToday'] = repos.xpath('normalize-space(.//span[@class = "d-inline-block float-sm-right"])').extract_first()
            item['users'] = []
            for users in repos.xpath('.//img[@class = "avatar mb-1"]'):
                user = UserItem()
                user["userName"] = users.xpath('./@alt').extract_first()
                user["userIcon"] = users.xpath('./@src').extract_first()
                item['users'].append(user)
            items.append(item)
        return items
