import scrapy
from e5p.items import E5PItem

class E5pspiderSpider(scrapy.Spider):
    name = "e5pspider"
    allowed_domains = ["www.everything5pounds.com"]
    start_urls = ["https://www.everything5pounds.com/en/Shoes/c/shoes?page=0&q=&sort=relevance"]
    heander_url = 'https://www.everything5pounds.com'
    base_url = 'https://www.everything5pounds.com/en/Shoes/c/shoes?page='
    page = 0 
    def parse(self, response):
        temp_product = response.xpath("//div[@class='product-grid row']//a")
        for p in temp_product:
            name = p.xpath("./@title").extract_first()
            product_url =self.heander_url + p.xpath("./@href").extract_first()
            sku = product_url.split('/')[-1]
            
        
        # 这是多页下载的示例
        # if self.page < 5:
        #     self.page = self.page + 1
        #     url = self.base_url + str(self.page) + '&q=&sort=relevance'
        #     yield scrapy.Request(url,callback=self.parse)
        
        # 这是页面追踪的实例
            yield scrapy.Request(url=product_url,callback=self.parse_product,meta={"name":name,"product_url":product_url,"sku":sku})
            
    def parse_product(self, response):
        list_src = response.xpath("//ul[@class='swiper-wrapper']/li/img")
        list_url_img = []
        for l in list_src:
            list_url_img.append(l.xpath("./@data-original").extract_first())
        shoes =  E5PItem(name=response.meta['name'] ,product_url=response.meta['product_url'],img_urls=list_url_img,sku=response.meta['sku'])
        yield shoes