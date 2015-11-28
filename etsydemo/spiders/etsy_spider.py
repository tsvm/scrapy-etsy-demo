import scrapy

from etsydemo.items import EtsyItem

class EtsySpider(scrapy.Spider):
    name = 'etsy'
    start_urls = ['https://www.etsy.com/c/accessories/belts-and-suspenders/belts']

    def parse(self, response):     
        # Follow all category links to find items to parse
        for href in response.xpath("//a/@href[contains(., '/c/')]"):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse)
        # Follow all product links and parse the items
        for href in response.xpath("//a/@href[contains(., '/listing/')]"):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_item)
        

    def parse_item(self, response):
        item = EtsyItem()
        item['title'] = response.xpath("//div[@id='listing-page-cart-inner']/h1/span/text()").extract()
        item['description'] = response.xpath("//div[@id='description-text']/text()").extract()
        item['tags'] = response.xpath("//div[@id='tags']/ul/li/a/text()").extract()
        yield item

