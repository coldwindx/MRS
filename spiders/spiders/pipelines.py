import json

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)

class MoviePipeline(object):
    '''豆瓣电影数据存储pipeline'''
    def __init__(self) -> None:
        self.f = open('/Users/zhulin/workspace/MRS/datasets/movies.json', 'w')
    def process_item(self, item, spider):
        if spider.name != 'movie':
            return item
        content = json.dumps(dict(item), ensure_ascii=False, cls=Encoder) + ",\n"
        self.f.write(content)
        return item
    def close(self, spider):
        self.f.close

class LinkPipeline(object):
    '''页面子链接存储pipeline'''
    def __init__(self) -> None:
        self.f = open('/Users/zhulin/workspace/MRS/datasets/links.json', 'w')
    def process_item(self, item, spider):
        if spider.name != 'link':
            return item
        content = json.dumps(dict(item), ensure_ascii=False, cls=Encoder) + ",\n"
        self.f.write(content)
        return item
    def close(self, spider):
        self.f.close

class CommentPipeline(object):
    '''用户评分存储pipeline'''
    def __init__(self) -> None:
        self.f = open('/Users/zhulin/workspace/MRS/datasets/comments.json', 'a')
    def process_item(self, item, spider):
        if spider.name != 'comment':
            return item
        content = json.dumps(dict(item), ensure_ascii=False, cls=Encoder) + ",\n"
        self.f.write(content)
        return item
    def close(self, spider):
        self.f.close