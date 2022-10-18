import scrapy

from spiders.items import Link

class LinkSpider(scrapy.Spider):
    name = 'link'
    start_urls = ['https://movie.douban.com/subject/26752087/']

    def parse(self, response):
        blocks = response.xpath('//div[@class="recommendations-bd"]')

        item = Link()
        item['name'] = blocks.xpath('dl/dt/a/img/@alt').extract()
        item['urls'] = blocks.xpath('dl/dt/a/@href').extract()
        
        yield item

