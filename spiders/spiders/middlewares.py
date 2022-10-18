import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

class AgentMiddleware(UserAgentMiddleware):
    '''用户代理中间件，用于拦截请求，添加User-Agent请求头'''
    def __init__(self, user_agent):
        super().__init__(user_agent)
    @classmethod
    def from_crawler(cls, crawler):
        return cls(user_agent=crawler.settings.get('USER_AGENTS'))
    def process_request(self, request, spider):
        # agent = random.choice(self.user_agent)
        request.headers['User-Agent'] = self.user_agent

class ProxyMiddleware(UserAgentMiddleware):
    '''IP代理中间件，用于拦截请求，添加IP代理（停用）'''
    def __init__(self, ip):
        self.ip = ip

    @classmethod
    def from_crawler(cls, crawler):
        return cls(ip=crawler.settings.get('IPS'))

    def process_request(self, request, spider):
        ip = random.choice(self.ip)
        request.meta['proxy'] = ip