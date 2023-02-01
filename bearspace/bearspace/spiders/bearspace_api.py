from scrapy.crawler import CrawlerProcess
from scrapy import Spider, Request
from bearspace.bearspace.items import BearspaceItem
import json


class BearspaceApiSpider(Spider):

    name = 'bearspace_api'
    allowed_domains = ['bearspace.co.uk']

    headers = {
        "Authorization": "rGWCUhVKK7jTy_hiX-4gQGPL9g8aUC33UTUt3Hiz6MU.eyJpbnN0YW5jZUlkIjoiOWRiZDIzZjktMzE0YS00NzVjLWI4OTAtYTZhNjQ1ZGNiZTdhIiwiYXBwRGVmSWQiOiIxMzgwYjcwMy1jZTgxLWZmMDUtZjExNS0zOTU3MWQ5NGRmY2QiLCJtZXRhU2l0ZUlkIjoiOGQ3ODQxYzctNmFkMC00MjdkLTg5NWMtMzFkYzE0ODhmYWVlIiwic2lnbkRhdGUiOiIyMDIzLTAxLTMxVDA3OjIwOjA2LjY5NVoiLCJ2ZW5kb3JQcm9kdWN0SWQiOiJzdG9yZXNfc2lsdmVyIiwiZGVtb01vZGUiOmZhbHNlLCJvcmlnaW5JbnN0YW5jZUlkIjoiYmNiOTQyNzItZTZlYS00NzVhLTllOGUtZmNhMTAwMjg3NmViIiwiYWlkIjoiNzVkOWZlYTctMDNlNy00YWM4LTk3MzktMDE2OGRjZGVhMWI2IiwiYmlUb2tlbiI6IjEwYzU2MjNlLTViOWEtMDUyMS0zMWNjLTk3N2E1MTU0NDQ5NCIsInNpdGVPd25lcklkIjoiMjNhMmVkMTgtYzJhOC00M2VmLThmYjMtZmZhMGMyNDM0ZjI4In0",
        "Content-Type": "application/json; charset=utf-8",
        "Referer": "https://www.bearspace.co.uk/_partials/wix-thunderbolt/dist/clientWorker.1f8b25cb.bundle.min.js",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    }

    def start_requests(self):
        url = 'https://www.bearspace.co.uk/_api/wix-ecommerce-storefront-web/api?o=getFilteredProducts&s=WixStoresWebClient&q=query,getFilteredProducts($mainCollectionId:String!,$filters:ProductFilters,$sort:ProductSort,$offset:Int,$limit:Int,$withOptions:Boolean,=,false,$withPriceRange:Boolean,=,false){catalog{category(categoryId:$mainCollectionId){numOfProducts,productsWithMetaData(filters:$filters,limit:$limit,sort:$sort,offset:$offset,onlyVisible:true){totalCount,list{id,options{id,key,title,@include(if:$withOptions),optionType,@include(if:$withOptions),selections,@include(if:$withOptions){id,value,description,key,linkedMediaItems{url,fullUrl,thumbnailFullUrl:fullUrl(width:50,height:50),mediaType,width,height,index,title,videoFiles{url,width,height,format,quality}}}}productItems,@include(if:$withOptions){id,optionsSelections,price,formattedPrice,formattedComparePrice,availableForPreOrder,inventory{status,quantity}isVisible,pricePerUnit,formattedPricePerUnit}customTextFields(limit:1){title}productType,ribbon,price,comparePrice,sku,isInStock,urlPart,formattedComparePrice,formattedPrice,pricePerUnit,formattedPricePerUnit,pricePerUnitData{baseQuantity,baseMeasurementUnit}itemDiscount{discountRuleName,priceAfterDiscount}digitalProductFileItems{fileType}name,media{url,index,width,mediaType,altText,title,height}isManageProductItems,productItemsPreOrderAvailability,isTrackingInventory,inventory{status,quantity,availableForPreOrder,preOrderInfoView{limit}}subscriptionPlans{list{id,visible}}priceRange(withSubscriptionPriceRange:true),@include(if:$withPriceRange){fromPriceFormatted}discount{mode,value}}}}}}&v={"mainCollectionId":"00000000-000000-000000-000000000001","offset":0,"limit":1000,"sort":null,"filters":null,"withOptions":true,"withPriceRange":true}'
        yield Request(url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        json_response = json.loads(response.text)
        catalog = json_response['data']['catalog']['category']['productsWithMetaData']['list']
        for one in catalog:
            item = BearspaceItem()
            item['url'] = f'https://www.bearspace.co.uk/product-page/{one.get("urlPart")}'
            item['title'] = one.get('name')
            item['price_gbp'] = one.get('price')
            yield item


# Left for debugging
if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(BearspaceApiSpider)
    process.start()
