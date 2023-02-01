from scrapy.spiders import SitemapSpider
from scrapy.crawler import CrawlerProcess
from bearspace.bearspace.items import BearspaceItem


class BearspaceSitemapsSpider(SitemapSpider):
    name = 'bearspace_sitemaps'
    sitemap_urls = ['https://www.bearspace.co.uk/store-products-sitemap.xml']
    sitemap_rules = [('https://www.bearspace.co.uk/product-page/', 'parse_product')]

    custom_settings = {
        'ITEM_PIPELINES': {
            'bearspace.bearspace.pipelines.BearspacePipeline': 300,
        }
    }

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
    process.crawl(BearspaceSitemapsSpider)
    process.start()
