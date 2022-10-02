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
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"
]
# 下载中间件
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None, 
    'spiders.middlewares.AgentMiddleware': 400,
    'spiders.middlewares.ProxyMiddleware': 543
}
# IP池
Ips=[
    'http://183.237.45.34:9091',
    'http://120.26.37.240:8000',
    'http://183.233.169.226:9091',
    'http://118.212.152.82:9091',
    'http://101.132.100.26:80',
    'http://39.130.150.43:80',
    'http://223.68.190.136:9091',
    'http://111.85.159.65:9091',
    'http://60.214.128.150:9091',
    'http://218.202.7.125:80',
    'http://118.119.238.91:9080',
    'http://218.75.38.154:9091',
    'http://175.6.185.156:9128',
    'http://183.129.190.172:9091',
    'http://112.6.117.178:8085',
    'http://183.224.41.199:80',
    'http://58.246.58.150:9002',
    'http://139.9.64.238:443',
    'http://120.237.144.200:9091',
    'http://47.107.150.251:80'
]