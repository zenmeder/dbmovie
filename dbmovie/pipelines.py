# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
from datetime import datetime

db_name = 'dbmovie{0}.db'.format(str(datetime.now())[:10].replace('-', ''))


class DbmoviePipeline(object):
	def process_item(self, item, spider):
		if item:
			conn = sqlite3.connect(db_name)
			cursor = conn.cursor()
			try:
				cursor.execute(
						'CREATE TABLE IF NOT EXISTS movies(id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, movieName VARCHAR(50),url VARCHAR (50), directors VARCHAR(50), actors VARCHAR(200), countries VARCHAR (50), genres VARCHAR (50), languages VARCHAR (50), runtime INTEGER , udate VARCHAR (15), rate VARCHAR (5), votes INTEGER )')
				cursor.execute(
						'insert into movies(id, movieName,url, directors, actors, countries, genres, languages, runtime, udate,rate, votes) VALUES (NULL, \'{0}\',\'{1}\',\'{2}\',\'{3}\',\'{4}\',\'{5}\',\'{6}\',\'{7}\',\'{8}\',\'{9}\',\'{10}\' )'.format(
								item['movieName'], item['url'], item['directors'], item['actors'], item['countries'],
								item['genres'],
								item['languages'], item['runtime'], item['date'], item['rate'], item['votes'])
				)
			except sqlite3.Error as e:
				print(e.args[0])
				cursor.close()
				conn.close()
			else:
				conn.commit()
				cursor.close()
				conn.close()
		return item
