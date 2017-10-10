#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

from scrapy import Spider
from bs4 import BeautifulSoup
from scrapy.http import FormRequest, Request
from scrapy_redis.spiders import RedisCrawlSpider
from dbmovie.items import DbmovieItem
import redis
import time
import random


class movieSpider(RedisCrawlSpider):
	# todo  不要使用豆瓣推荐的相关电影(会导致爬取大量相同类型的电影)
	name = 'movie'
	allow_domains = ['douban.com']
	custom_settings = {
		'ITEM_PIPELINES': {
			'dbmovie.pipelines.DbmoviePipeline': 100
		}
	}
	redis_key = 'movie_spider:start_urls'
	redis_visited_key = 'movie_spider:visited_urls'

	def parse(self, response):
		time.sleep(1)
		r = redis.Redis(host='localhost', port=6379, db=0)
		bs = BeautifulSoup(response.body, 'lxml')
		try:
			movieUrl = response.url
			movieName = bs.find('span', attrs={'property': 'v:itemreviewed'}).get_text()
			r.sadd(self.redis_visited_key, movieName)
			directors = [director.get_text() for director in bs.find_all('a', attrs={'rel': 'v:directedBy'})]
			actors = [actor.get_text() for actor in bs.find_all('a', attrs={'rel': 'v:starring'})]
			genres = [genre.get_text() for genre in bs.find_all('span', attrs={'property': 'v:genre'})]
			countries = [country.strip() for country in
						 bs.find('span', text='制片国家/地区:', class_='pl').next_sibling.split('/')]
			languages = [language.strip() for language in
						 bs.find('span', text='语言:', class_='pl').next_sibling.split('/')]
			date = bs.find('span', attrs={'property': 'v:initialReleaseDate'}).get_text()[:10]
			runtime = bs.find('span', attrs={'property': 'v:runtime'}).get_text()[:3]
			rate = bs.find('strong', attrs={'property': 'v:average'}).get_text()
			votes = bs.find('span', attrs={'property': 'v:votes'}).get_text()
		except Exception as e:
			print(e.args[0])
		recommendations = []
		for rec in bs.find(class_='recommendations-bd').find_all('dt'):
			recommendations.append({'url': (rec.find('a'))['href'], 'name': (rec.find('img'))['alt']})
		count = times = 0
		while count < 3 and times < 8: # 从每个电影的八部推荐电影里取三个没有爬取过的电影加入到队列里
			times += 1
			recommendation = recommendations[random.randint(0, len(recommendations) - 1)]
			if not r.sismember(self.redis_visited_key, recommendation['name']) :
				r.sadd(self.redis_key, recommendation['url'])
				count += 1

		result = DbmovieItem()
		result['url'] = movieUrl
		result['movieName'] = movieName
		result['directors'] = ','.join(directors)
		result['actors'] = ','.join(actors)
		result['genres'] = ','.join(genres)
		result['countries'] = ','.join(countries)
		result['languages'] = ','.join(languages)
		result['date'] = date if date else '0000-00-00'
		result['runtime'] = runtime if runtime else -1
		result['rate'] = rate if rate else '0'
		result['votes'] = votes if votes else 0
		return result
