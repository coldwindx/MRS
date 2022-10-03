# MRS
Movie recommendation system
# 文件结构
数据爬取代码均位于spiders文件夹下，作为单独项目使用，采用scrapy框架。
```bash
├── scrapy.cfg
└── spiders
    ├── __init__.py
    ├── items.py            # 实体类
    ├── middlewares.py      # 中间件
    ├── pipelines.py        # 存储管道
    ├── settings.py         # 全局配置
    └── spiders             # 爬虫类
        ├── __init__.py
        ├── comment.py      # 爬取评论
        ├── link.py         # 爬取链接
        └── movie.py        # 爬取电影
```
## 运行
```bash
cd spiders
scrapy crawl moive  # 爬取电影信息
scrapy crawl link   # 爬取电影链接
```
