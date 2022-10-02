# 管道
ITEM_PIPELINES = {
    'pipelines.Pipeline': 300, 
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
    'middlewares.AgentMiddleware': 400,
    'middlewares.ProxyMiddleware': 543
}
# IP池
Ips=[
    {"http://61.129.70.131:8080"},
    {"http://61.152.81.193:9100"},
    {"http://120.204.85.29:3128"},
    {"http://219.228.126.86:8123"},
    {"http://61.152.81.193:9100"},
    {"http://218.82.33.225:53853"}
]