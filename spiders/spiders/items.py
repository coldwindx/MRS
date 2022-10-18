import scrapy

class Movie(scrapy.Item):
    '''电影Item类'''
    id = scrapy.Field()         # ID
    name = scrapy.Field()       # 名称
    director = scrapy.Field()   # 导演
    actors = scrapy.Field()     # 演员
    forms = scrapy.Field()      # 类型
    score = scrapy.Field()      # 评分
    n_comments = scrapy.Field() # 评论数量

class Link(scrapy.Item):
    '''浏览器页面上其他电影链接'''
    name = scrapy.Field()
    urls = scrapy.Field()

class Comment(scrapy.Item):
    '''用户评分'''
    movie_id = scrapy.Field()   # 电影
    user_name = scrapy.Field()  # 用户
    score = scrapy.Field()      # 评分
