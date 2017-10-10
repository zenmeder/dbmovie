# -*- coding: utf-8 -*-

# Scrapy settings for dbmovie project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'dbmovie'

SPIDER_MODULES = ['dbmovie.spiders']
NEWSPIDER_MODULE = 'dbmovie.spiders'

# settings for redis
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
REDIS_URL = 'redis://127.0.0.1:6379'
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
REDIS_START_URLS_AS_SET = True
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'dbmovie (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "zh-CN,zh;q=0.8,ja;q=0.6,en;q=0.4",
	"Connection": "keep-alive",
	"Cache-Control": "max-age=0",
	"Cookie": 'bid=hv_Xc9Vtsq0; gr_user_id=c0020f79-22d7-48c0-9c0f-678d862de44b; ue="948586331@qq.com"; ll="108296"; viewed="3435735_26892803"; _ga=GA1.2.1679313253.1478168820; dbcl2="41482037:Sqb4Z4LbK+c"; ap=1; ck=2pY5; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1502160926%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=b0003673e45fab90.1478168831.89.1502161534.1500173231.; _pk_ses.100001.4cf6=*; __utma=30149280.1679313253.1478168820.1501038695.1502160864.165; __utmb=30149280.2.10.1502160864; __utmc=30149280; __utmz=30149280.1500356938.163.52.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; __utmv=30149280.4148; __utma=223695111.1003425480.1478168831.1500086758.1502160926.86; __utmb=223695111.0.10.1502160926; __utmc=223695111; __utmz=223695111.1502160926.86.74.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; push_noty_num=0; push_doumail_num=0; _vwo_uuid_v2=DDFDCB6DEA78B216F6C2C7E422B40959|ed38808e6f92506b86a924e8cbd609bf',
	"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
	"Host": "movie.douban.com",
	"Upgrade-Insecure-Requests": "1"
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'dbmovie.middlewares.DbmovieSpiderMiddleware': 543,
# 	'dbmovie.spiders.DbmovieSpiderMiddleware.dbmovieSpiderMiddleware':100
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'dbmovie.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'dbmovie.pipelines.DbmoviePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
