# Scrapy settings for spiders project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'spiders'

SPIDER_MODULES = ['spiders.spiders']
NEWSPIDER_MODULE = 'spiders.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'spiders (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False  # 默认为True，过滤不规范的url
# 管道
ITEM_PIPELINES = {
    'spiders.pipelines.Pipeline': 300, 
}
# 爬取间隔时间
DOWNLOAD_DELAY = 3
# User Agent池
USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15"
]
# 下载中间件
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None, 
    'spiders.middlewares.AgentMiddleware': 400,
    # 'spiders.middlewares.ProxyMiddleware': 543
}
# IP池 WTF:大写可以，小写不可以？
# http://ip.yqie.com/ipproxy.htm
IPS=[
'http://47.101.44.122:80',
'http://116.63.93.172:8081',
'http://42.180.208.43:8070',
'http://60.255.151.82:8',
'http://218.2.214.107:80',
'http://116.117.134.135:9999',
'http://202.108.22.5:80',
'http://45.64.22.24:80',
'http://180.97.34.35:80',
'http://112.80.248.73:80',
'http://116.117.134.135:8828',
'http://47.92.234.75:80',
'http://203.74.120.79:3128',
'http://60.255.151.81:80',
'http://39.106.223.134:80',
'http://222.74.202.229:80',
'http://58.240.52.114:80'
]