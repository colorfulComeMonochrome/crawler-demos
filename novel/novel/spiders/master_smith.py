# -*- coding: utf-8 -*-
import scrapy
from novel.items import NovelItem
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class MasterSmithSpider(scrapy.Spider):
    name = 'master_smith'
    allowed_domains = ['book.qidian.com', 'read.qidian.com']
    start_urls = ['https://book.qidian.com/info/1010991657#Catalog/']

    # 设置初始化参数 通过-a调用   max_num 爬取的章节数
    def __init__(self, max_num=0, *args, **kwargs):
        super(MasterSmithSpider, self).__init__(*args, **kwargs)
        self.max_num = int(max_num)

    def parse(self, response):
        chapters = response.xpath("//ul[@class='cf']/li/a/@href").extract()
        # chap_name = response.xpath("//ul[@class='cf']/li/a/text()").extract()
        # print(chapters)
        for i in range(len(chapters)):
            if self.max_num and self.max_num <= i:
                break
            chapter = chapters[i]
            if not chapter.startswith('https:'):
                chapter = 'https:%s' % chapter
            request = scrapy.Request(chapter, callback=self.get_content)
            # request.meta['title'] = chap_name[i]
            request.headers['Host'] = 'read.qidian.com'
            print(request.url)
            print(request.headers)
            yield request

    def get_content(self, response):
        title = response.xpath('//h3[@class="j_chapterName"]/text()').extract_first()
        # xpath 的extract()方法返回一个元组, 里面是一个列表,列表中含有N个元素(小说里一个p标签为一个元素)
        body = response.xpath("//div[@class='read-content j_readContent']//p/text()").extract(),
        content = ''.join(body[0])
        item = NovelItem()
        item['title'] = title
        item['content'] = content
        logger.info('%s has grabed, content: %s' % (title, content))
        yield item
