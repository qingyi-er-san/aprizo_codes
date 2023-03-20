from time import sleep

import csv
import requests
from lxml import etree

from datetime import datetime
import pytz



urls = ['https://www.eclatparis.com/produits',
        'https://www.eclatparis.com/produits?offset=200',
        'https://www.eclatparis.com/produits?offset=400',
        'https://www.eclatparis.com/produits?offset=600'
        ]

url_header = 'https://www.eclatparis.com'


# 存储所有产品的URL的列表
product_urls = []

# 由于要布置到云端，pythonanywhere对selenium的限制太多了，
# 直接布置selenium会导致程序无法运行
# 这里的cookies是从本地版的运行中，利用selenium得到的，
# 直接使用cookies就可以绕过登录界面

cookies= {'hasCart': 'true',
  '_ga_ZMDKD43H01': 'GS1.1.1677141224.1.1.1677141248.0.0.0', 
  'siteUserCrumb': '91m8yMQracXHvtn3hp_zqJZ29UAbVo6aaNclbA8xsq_qVyEboCKRsEBv3EqT4dQmzImPIrdRSieZfpx1drxkGFQAvslwA5temqFq29j_XcmIbFuE51bxgA1TRcZFYz1o',
  'SiteUserInfo': '%7B%22authenticated%22%3Atrue%2C%22lastAuthenticatedOn%22%3A%222023-02-23T08%3A34%3A03.898Z%22%2C%22siteUserId%22%3A%2263dc38e82b1d5869bf4988e2%22%2C%22firstName%22%3A%22Wenjie%22%7D', 
  'crumb': 'BaRQABCJ44v5MTBhMjM1YWRhODA1ZDUxMWU5Y2JhYjY3MmYyNjU5', 
  'ss_cvt': '1677141232051', 
  'ss_cvr': 'cb592531-5038-4c16-bff7-3c4d1ae0cf97|1677141232051|1677141232051|1677141232051|1', 
  'CART': '-B8ztComuxoy8mZfh6NOEGGjxgnUzIdW4JGacILa', 
  '_ga': 'GA1.1.1986290368.1677141224', 
  'SiteUserSecureAuthToken': 'MXw1OTBmNTNlNy0xZWMyLTQzODctYWMzZS01NjAzZTIwYjEzOWJ8V0w0UE1BQlN3SFYwOFY0WWQyRmtsQmVDR1ktSVV1SVltTVVkZkdGcy1oel9yT21odDY4OXFZUm1IeElMWkRWQg', 
  '_fbp': 'fb.1.1677141224123.561848947'}


for url in urls:
    # get中的cookies是字典类的
    # get方法是会阻塞线程的，只有在获取完整个页面的所有数据之后才会进行下面的代码
    response =requests.get(url,cookies=cookies) 
    sleep(2)        # sleep在这里的作用并不是等待页面加载完成，而是防止过快的爬取导致ip地址被网址suspendus
    body = etree.HTML(response.content)
    links = body.xpath( '//a[contains(@class, "grid-item-link")]')
    for link in links:
        product_urls.append(url_header + link.get('href'))
sleep(2)



francetime = pytz.timezone("Europe/Paris")
dt = datetime.now(francetime)
###英文格式
timenow =str(dt.year)+' '+str(dt.month)+' '+str(dt.day)
filename = timenow + 'product_urls_1.csv'
# 将所有产品的URL存储到CSV文件中
headers = ['URL', 'Sold out']
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    for url in product_urls:
        writer.writerow([url, ''])



# 检查每个产品是否已售罄，将结果添加到CSV文件中
with open(filename, mode='r', newline='') as file:
    reader = csv.reader(file)
    next(reader)  # 跳过标题行
    rows = []
    for row in reader:
        try:
            response = requests.get(row[0], cookies=cookies)
            html = etree.HTML(response.content)
            sold_out = 'Yes' if html.xpath('//div[@class="ProductItem-details-checkout"]//div[@class="product-mark sold-out"]') else ''
            row[1] = sold_out
        except Exception as e:
            print(f"Failed to check product {row[0]}: {e}")
        rows.append(row)

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    for row in rows:
        writer.writerow(row)
print('done')
