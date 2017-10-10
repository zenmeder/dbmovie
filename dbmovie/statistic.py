#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
# import redis
# r = redis.Redis(host='localhost', port=6379, db=0)
# a = ['https://movie.douban.com/subject/25884801/','https://movie.douban.com/subject/11600078/','https://movie.douban.com/subject/26761688/','https://movie.douban.com/subject/26823828/','https://movie.douban.com/subject/26704590/','https://movie.douban.com/subject/26266085/','https://movie.douban.com/subject/26667056/','https://movie.douban.com/subject/26387939/']
# for i in a:
# 	r.sadd('movie_spider:start_urls', i)

# a = r.smembers('movie_spider:start_urls')
# b = r.smembers('movie_spider:visited_urls')
# print(len(a),len(b))

import pandas as pd
import sqlite3
from collections import defaultdict
from datetime import datetime
import matplotlib.pyplot as plt

# db_name = '../dbmovie{0}.db'.format(str(datetime.now())[:10].replace('-', ''))
db_name = '../dbmovie20170809.db'
conn = sqlite3.connect(db_name)
df = pd.read_sql_query('select * from movies', conn)  # type: pd.DataFrame
# 舍弃id列
df = df.drop('id', axis=1)  # type: pd.DataFrame
# 筛选掉重复的电影名,很不幸，两万多部电影就变成了近一万部了
df = df.drop_duplicates(['movieName'], keep='last')
# 1.根据评分和投票数对所有电影进行排序，优先比较评分（这里只统计投票数1w以上的电影)
df1 = df[df['votes']>10000].sort_values(by=['rate','votes'],ascending=False)[['movieName', 'votes', 'rate']] #type: pd.DataFrame
print(df1)
# 2.1统计所有的导演, 共6361名
directors = defaultdict(int)
for l in df['directors']:
	for director in l.split(','):
		if director:
			directors[director] += 1
# 2.2统计了每个导演的作品数，并按作品降序排列
director_has_movie = pd.Series(directors).sort_values(ascending=False)
director_has_movie[:10].plot(kind='barh')
# 3.1统计所有的演员, 共32291人
actors = defaultdict(int)
for a in df['actors']:
	for actor in a.split(','):
		if actor:
			actors[actor] += 1
# 3.2统计每个演员的作品数，并按降序排列
actor_has_movie = pd.Series(actors).sort_values(ascending=False)
# 4.1分析国家与地区数 共182个
countries = defaultdict(int)
for c in df['countries']:
	for country in c.split(','):
		if country:
			countries[country] += 1
# 4.2统计每个地区的电影数并按降序排列，1-美国 2-香港 3-日本 4-中国大陆 5-法国
country_has_movie = pd.Series(countries).sort_values(ascending=False)
# 5统计语种数, 共296种  并按语种降序排列
languages = defaultdict(int)
for d in df['languages']:
	for language in d.split(','):
		languages[language] += 1
language_has_movie = pd.Series(languages).sort_values(ascending=False)
# 6.1统计导演的平均评分
director_sum_rates = defaultdict(float)
for ix,row in df[['directors','rate']].iterrows():
	for dct in row['directors'].split(','):
		if dct:
			director_sum_rates[dct] += float(row['rate'])
director_per_rates = defaultdict(dict)
for director, num in directors.items():
	director_per_rates[director] = {'rate':round(director_sum_rates[director]/num, 3), 'num':num}
director_rate = pd.DataFrame(director_per_rates).T
# 6.2统计评分最高的几个导演 作品数要求大于5部
topDirectors = director_rate[director_rate['num']>5].sort_values(by='rate',ascending=False)
# 7 统计评分最高的演员:至少有十部电影，按评分降序
actor_sum_rates = defaultdict(float)
for ix, row in df[['actors','rate']].iterrows():
	for act in row['actors'].split(','):
		if act:
			actor_sum_rates[act] += float(row['rate'])
actor_per_rate = defaultdict(dict)
for actor, num in actors.items():
	actor_per_rate[actor] = {'rate': round(actor_sum_rates[actor]/num,3),'num':num}
actor_rate = pd.DataFrame(actor_per_rate).T
topActors = actor_rate[actor_rate['num']>10].sort_values(by='rate',ascending=False)[:100]
print(topActors)
