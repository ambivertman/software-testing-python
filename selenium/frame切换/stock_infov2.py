from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import csv
from threading import Thread


def switch_window(wd, main_window):
    for handle in wd.window_handles:
        wd.switch_to.window(handle)
        if '_数据_资料_信息' in handle:
            break
    # 点击公司概况
    sleep(1)
    wd.find_element(By.CSS_SELECTOR, '#ul_tab > li.at').click()
    company_intro = wd.find_element(By.CSS_SELECTOR, '#m_gsjj > tbody > tr:nth-child(5) > td.tal').text
    wd.close()
    wd.switch_to.window(main_window)
    return company_intro


def extract_info(table,wd):
    company_list = []
    stocks = table.find_elements(By.CSS_SELECTOR, 'tr')
    for stock in stocks:
        ID = stock.find_element(By.CSS_SELECTOR, 'td:nth-child(2) > a').text
        name = stock.find_element(By.CSS_SELECTOR, 'td.mywidth > a').text
        main_window = wd.current_window_handle
        sleep(1)
        # 进入数据页面
        try:
            stock.find_element(By.CSS_SELECTOR, 'td.listview-col-Links > a:nth-child(3)').click()
        except:
            stock.find_element(By.CSS_SELECTOR, 'td.listview-col-Links > a:nth-child(3)').click()
        # 切换窗口
        intro_txt = switch_window(wd,main_window)
        company_info = {'ID': ID, 'name': name, 'intro': intro_txt }
        company_list.append(company_info)

    return company_list


wd = webdriver.Chrome()
wd.get('http://quote.eastmoney.com/center/gridlist.html#hs_a_board')
wd.implicitly_wait(10)

stock_info = []
for i in range(10):
    table = wd.find_element(By.TAG_NAME, 'tbody')
    stock_info.append(extract_info(table, wd))
    wd.find_element(By.CSS_SELECTOR, '#main-table_paginate > a.next.paginate_button').click()
    sleep(1)

filepath = 'stock_info.csv'
fields = ['ID','name','intro']
with open(filepath, 'w',encoding='utf8', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fields)
    # 写入列名
    writer.writeheader()
    # 写入字典列表的内容
    for table in stock_info:
        for row in table:
            writer.writerow(row)