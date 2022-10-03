import scrapy

class Movie(scrapy.Item):
    '''电影Item类'''
    name = scrapy.Field()       # 名称
    director = scrapy.Field()   # 导演
    actors = scrapy.Field()     # 演员
    forms = scrapy.Field()      # 类型
    score = scrapy.Field()      # 评分

class Link(scrapy.Item):
    '''浏览器页面上其他电影链接'''
    url = scrapy.Field()