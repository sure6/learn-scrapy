import scrapy


class HuyaSpider(scrapy.Spider):
    name = 'huya'
    allowed_domains = ['https://www.baidu.com']
    start_urls = ['https://www.baidu.com']

    def parse(self, response):
        tile = response.xpath('//html/head/title/text()')
        print(tile)
