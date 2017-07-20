# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ReposItem(scrapy.Item):
    url = scrapy.Field()
    # 仓库名
    reposName = scrapy.Field()
    # 仓库描述
    reposDesc = scrapy.Field()
    # 语言类型
    languageType = scrapy.Field()
    # 语言颜色
    languageColor = scrapy.Field()
    # star
    star = scrapy.Field()
    # todya star
    starToday = scrapy.Field()
    # fork
    fork = scrapy.Field()
    # users
    users = scrapy.Field()


class UserItem(scrapy.Item):
    userName = scrapy.Field()
    userIcon = scrapy.Field()


class DeveloperItem(scrapy.Item):
    userName = scrapy.Field()
    nickName = scrapy.Field()
    userIcon = scrapy.Field()
    popReposName = scrapy.Field()
    popReposDesc = scrapy.Field()
    popReposUrl = scrapy.Field()