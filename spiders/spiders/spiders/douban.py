import scrapy

from spiders.items import Movie

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    start_urls = ['https://movie.douban.com/subject/26752088/']

    def parse(self, response):
        sites = response.xpath('//div[@id="content"]') 
        for i in sites:
            item = Movie() 
            item['name'] = i.xpath('h1/span[1]/text()').extract()
            yield item
