#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class dbmovieSpiderMiddleware(object):
	def process_request(self, request, spider):
		if spider.name == 'movie':
			print('start')
			print(request)