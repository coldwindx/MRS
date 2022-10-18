import scrapy
from scrapy import Request

from spiders.items import Comment

class CommentSpider(scrapy.Spider):
    name = 'comment'
    # start_urls = ['https://movie.douban.com/subject/26752088/comments?sort=new_score&status=P']
    
    def start_requests(self):
        '''用于生成爬虫访问请求'''
        start, limit = 0, 20
        base_url = 'https://movie.douban.com/subject/{}/comments?start={}&limit={}&status=P&sort=new_score'
        for _ in range(20):
            url = base_url.format('26752088', start, limit)
            yield Request(url=url,callback=self.parse)
            start += 20

    def parse(self, response):
        comments = response.xpath('//div[@id="comments"]/div')

        item = Comment()
        item['user_name'] = comments.xpath('div[2]/h3/span[2]/a/text()').extract()
        item['score'] = comments.xpath('div[2]/h3/span[2]/span[2]/@class').extract()
        
        yield item
