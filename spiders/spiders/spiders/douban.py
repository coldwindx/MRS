import scrapy

from spiders.items import Movie

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    start_urls = ['https://movie.douban.com/subject/26752088/']

    def parse(self, response):
        site = response.xpath('//div[@id="content"]') 
        infos = site.xpath('//div[@id="info"]')
        
        item = Movie() 
        item['name'] = site.xpath('h1/span[1]/text()').extract()
        item['director'] = infos.xpath('span[1]/span[2]/a/text()').extract()
        item['actors'] = infos.xpath('span[3]/span/a/text()').extract()
        item['forms'] = infos.xpath('//span[@property="v:genre"]/text()').extract()
        item['score'] = infos.xpath('//strong[@property="v:average"]/text()').extract()
        yield item
