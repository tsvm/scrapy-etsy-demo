import scrapy

from etsydemo.items import EtsyItem

class EtsySpider(scrapy.Spider):
    name = 'etsy'
    start_urls = ['https://www.etsy.com/search?q=best%20selling%20items']

    def parse(self, response):     
        # Follow all category links to find items to parse
        for href in response.xpath("//a/@href[contains(., '/search/')]"):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse)
        # Follow all product links and parse the items
        for href in response.xpath("//a/@href[contains(., '/listing/')]"):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_item)
        

    def parse_item(self, response):
        item = EtsyItem()
        item['url'] = response.request.url
        item['title'] = response.xpath("//div[@id='listing-page-cart-inner']/h1/span/text()").extract()
        item['description'] = response.xpath("//div[@id='description-text']/text()").extract()
        item['tags'] = response.xpath("//div[@id='tags']/ul/li/a/text()").extract()
        item['price'] = response.xpath("//span[@id='listing-price']/span/span[@class='currency-value']/text()").extract()
        item['rating'] = response.xpath("//span[@class='review-rating']/meta[@itemprop='rating']/@content").extract()
        item['reviews'] = response.xpath("//span[@class='review-rating']/meta[@itemprop='count']/@content").extract()
        item['treasury_lists'] = response.xpath("//a[@href[contains(., 'treasury/listing/')]]/text()").extract()
        item['favorites'] = response.xpath("//a[@href[contains(., '/favoriters?')]][1]/text()").extract()
        item['views'] = response.xpath("//li/text()[contains(., 'views')]").extract()
        yield item
