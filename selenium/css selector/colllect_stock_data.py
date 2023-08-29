import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def extract_info(table):
    info_dict = {}
    stocks = table.find_elements(By.CSS_SELECTOR, 'tr')
    for stock in stocks:
        ID = stock.find_element(By.CSS_SELECTOR, 'td:nth-child(2) > a').text
        name = stock.find_element(By.CSS_SELECTOR, 'td.mywidth > a').text
        info_dict[ID] = name
    return info_dict


wd = webdriver.Chrome()
wd.get('http://quote.eastmoney.com/center/gridlist.html#hs_a_board')
wd.implicitly_wait(5)

stock_info = []
for i in range(10):
    table = wd.find_element(By.TAG_NAME, 'tbody')
    stock_info.append(extract_info(table))
    wd.find_element(By.CSS_SELECTOR, '#main-table_paginate > a.next.paginate_button').click()
    sleep(1)

wd.quit()
file_name = 'stock_info.json'
with open(file_name, 'w', encoding='utf8') as json_file:
    json.dump(stock_info, json_file, indent=4,ensure_ascii=False)

print(f"前十页股票代码已保存至{file_name}")
