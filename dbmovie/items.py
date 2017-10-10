# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DbmovieItem(scrapy.Item):
	movieName = scrapy.Field()
	directors = scrapy.Field() #导演
	actors = scrapy.Field() #主演
	genres = scrapy.Field() #类型
	countries = scrapy.Field() #国家地区
	languages = scrapy.Field() #语言
	date = scrapy.Field() #上映日期
	runtime = scrapy.Field() #片长
	rate = scrapy.Field() #评分
	votes = scrapy.Field() #评分人数
	url = scrapy.Field() #网页链接url
