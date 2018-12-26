from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://stock.finance.sina.com.cn/option/quotes.html')

while True:
    r = driver.execute_script("return ")
    print(r)
    time.sleep(1)