from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

import csv
from bs4 import BeautifulSoup
import requests
from lxml import etree

from datetime import datetime
import pytz

# 设置 ChromeOptions 配置，禁用图片加载，加快网页加载速度
# 使用Selenium和Chrome浏览器启动爬虫

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
#chrome_options.add_argument('--headless')  # 隐藏Chrome窗口
# 设置 ChromeOptions 配置，设置浏览器分辨率，防止被识别为自动化浏览器
chrome_options.add_argument("window-size=1280,800")

# 启动 Chrome 浏览器
driver = webdriver.Chrome(options=chrome_options)

# 打开登录页面
driver.get("https://www.eclatparis.com/account/login")


# 等待页面元素加载完成
wait = WebDriverWait(driver, 10000)
#sleep(2)

# 填写用户名和密码
loginFrame = driver.find_element(By.XPATH, "//*[@id='accountFrame']")
driver.switch_to.frame(loginFrame)
driver.find_element(By.XPATH, "//input[contains(@type, 'email')]").send_keys("wenjiexu@preciousse.com")
driver.find_element(By.XPATH, '//input[@data-test="login-password"]')\
    .send_keys("Nbb7415157!")

# 点击登录按钮
driver.find_element(By.XPATH, '//button[@data-test="login-button"]')\
    .click()


urls = ['https://www.eclatparis.com/produits',
        'https://www.eclatparis.com/produits',
        'https://www.eclatparis.com/produits?offset=200',
        'https://www.eclatparis.com/produits?offset=400',
        'https://www.eclatparis.com/produits?offset=600'
        ]




# 存储所有产品的URL的列表
product_urls = []

for url in urls:
    driver.get(url)  # get方法是会阻塞线程的，只有在获取完整个页面的所有数据之后才会进行下面的代码
    sleep(2)        # sleep在这里的作用并不是等待页面加载完成，而是防止过快的爬取导致ip地址被网址suspendus
    # wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(@class, "grid-item-link")]')))
    links = driver.find_elements(By.XPATH, '//a[contains(@class, "grid-item-link")]')
    for link in links:
        product_urls.append(link.get_attribute('href'))
        #print(link.get_attribute('href'))
sleep(2)


cookies = {cookie['name']: cookie['value'] for cookie in driver.get_cookies()}
print(cookies)
francetime = pytz.timezone("Europe/Paris")
dt = datetime.now(francetime)
###英文格式
timenow =str(dt.year)+' '+str(dt.month)+' '+str(dt.day)
filename = timenow + 'product_urls.csv'
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
            cookies = {cookie['name']: cookie['value'] for cookie in driver.get_cookies()}
            response = requests.get(row[0], cookies=cookies)
            html = etree.HTML(response.content)
            #soup = BeautifulSoup(response.text, 'html.parser')
            sold_out = 'Yes' if html.xpath('//div[@class="ProductItem-details-checkout"]//div[@class="product-mark sold-out"]') else ''
            row[1] = sold_out
            print(sold_out)
        except Exception as e:
            print(f"Failed to check product {row[0]}: {e}")
        rows.append(row)

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    for row in rows:
        writer.writerow(row)
print('driver quit')
driver.quit()