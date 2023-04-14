# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import requests
import os

class E5PPipeline:
    # 在爬虫程序开始之前执行的程序
    def open_spider(self,spider):
        self.fp = open('shoes.json','w',encoding='utf-8') 

    # 接收由spider传来的数据，并且负责写入
    def process_item(self, item, spider):
        # 注意一下 ，write函数只能操作string类型的值
        self.fp.write(str(item))
        return item

    # 在spider结束之后执行的程序
    def close_spider(self,spider):
        self.fp.close()
class E5PPipeline_picture:
    def process_item(self,item,spider):
        urls = item.get('img_urls')
        sku = item.get('sku')
        for index,url in enumerate(urls):
            path_base = './picture_shoes/'+sku +'/'
            folder = os.path.exists(path=path_base)
            if not folder:
                os.makedirs(path_base)
            else:
                pass
            path = path_base + str(index)+'.jpg'
            url= 'https:' + url
            response = requests.get(url=url)
            with open(path,'wb') as f:
                f.write(response.content)