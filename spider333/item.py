import scrapy

class Movie(scrapy.Item):
    '''电影Item类'''
    name = scrapy.Field()       # 名称
    director = scrapy.Field()   # 导演
    actors = scrapy.Field()     # 演员
    score = scrapy.Field()      # 评分
