import scrapy
from scrapy.utils.project import get_project_settings
import requests

from spiders.items import Link

class LinkSpider(scrapy.Spider):
    name = 'link'
    start_urls = ['https://movie.douban.com/subject/26752087/']

    def parse(self, response):
        #接在parse函数下面，这段代码产出每一部电影的具体网址
        settings = get_project_settings()
        headers = {'User-Agent': settings.get('USER_AGENTS')}
        for m in range(500):
            url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start={}'.format(m*20)
			#这里返回的是 json文件所以要用 .json()
            datas = requests.get(url, headers=headers).json() 
            datas = datas['data']     #datas是一个字典，里面的data键里包含了所需要的全部信息
            for n in datas[1:]:       #去掉上面已经爬取的我不是药神
                item = Link()
                item['url'] = n['url'].replace('\\','')
                yield item

