import random

from scrapy.exceptions import NotConfigured


class RandomProxyMiddleware(object):
    def __init__(self, settings):
        self.proxies = settings.get('PROXIES')

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool('PROXY_ENABLED'):
            raise NotConfigured
        if not crawler.settings.getlist('PROXIES'):
            raise NotConfigured
        return cls(crawler.settings)

    def process_request(self, request, spider):
        request.meta['proxy'] = random.choice(self.proxies)







