import scrapy

from spiders.items import Movie

class MovieSpider(scrapy.Spider):
    name = 'movie'
    start_urls = ['https://movie.douban.com/subject/26752088/']

    # def start_requests(self):
    #     '''用于生成爬虫访问请求'''
    #     data={'ch':'photography','listtype':'new'}
    #     base_url='https://image.so.com/zj?'
    #     for page in range(1,self.settings.get('MAX_PAGE')+1):
    #         data['sn']=page*30
    #         params=urlencode(data)
    #         url=base_url+params
    #         yield Request(url=url,callback=self.parse)

    def parse(self, response):
        site = response.xpath('//div[@id="content"]') 
        infos = site.xpath('//div[@id="info"]')
        # 电影数据爬取
        item = Movie() 
        item['name'] = site.xpath('h1/span[1]/text()').extract()
        item['director'] = infos.xpath('span[1]/span[2]/a/text()').extract()
        item['actors'] = infos.xpath('span[3]/span/a/text()').extract()
        item['forms'] = infos.xpath('//span[@property="v:genre"]/text()').extract()
        item['score'] = infos.xpath('//strong[@property="v:average"]/text()').extract()
        yield item
