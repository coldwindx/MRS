import json

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)

class MoviePipeline(object):
    def __init__(self) -> None:
        self.f = open('/Users/zhulin/workspace/MRS/datasets/movies.json', 'w')
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False, cls=Encoder) + ",\n"
        self.f.write(content)
        return item
    def close(self, spider):
        self.f.close