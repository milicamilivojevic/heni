from scrapy import Spider, Request
from scrapy.crawler import CrawlerProcess
from bearspace.bearspace.items import BearspaceItem


class BearspaceHtmlSpider(Spider):

    name = 'bearspace_html'
    allowed_domains = ['bearspace.co.uk']
    start_urls = ['https://www.bearspace.co.uk/purchase']

    custom_settings = {
        'ITEM_PIPELINES': {
            'bearspace.bearspace.pipelines.BearspacePipeline': 300,
        }
    }

    def parse(self, response):
        links = response.xpath('.//a[@data-hook="product-item-product-details-link"]/@href').extract()
        for link in links:
            yield Request(link, callback=self.parse_product)
        pages = response.xpath('.//a[@data-hook="product-list-pagination-link-seo-link"]/@href').extract()
        if pages:
            yield Request(pages[-1], self.parse)

    def parse_product(self, response):
        item = BearspaceItem()
        item['url'] = response.url
        item['title'] = response.xpath('.//h1[@data-hook="product-title"]/text()').extract_first()
        item['raw_data'] = response.xpath('.//pre[@data-hook="description"]/p//text()').extract()
        item['price_gbp'] = response.xpath('.//span[@data-hook="formatted-primary-price"]/text()').extract_first()
        yield item


# Left for debugging
if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(BearspaceHtmlSpider)
    process.start()
