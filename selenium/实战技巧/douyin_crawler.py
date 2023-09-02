from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(10)

wd.get('https://www.douyin.com/discover')
wd.find_element(By.CSS_SELECTOR, 'div.dy-account-close').click()
while True:
    try:
        wd.find_element(By.CSS_SELECTOR, 'svg.verify-bar-close--icon').click()
    except:
        break

container = wd.find_element(By.CSS_SELECTOR, 'div#waterFallScrollContainer')
items = container.find_elements(By.CSS_SELECTOR, 'div.ekJG6htF')

titles = []
for item in items:
    if item.get_attribute('id') == 'hotItem':
        continue
    title = item.find_element(By.CSS_SELECTOR, 'div.CfK3UpJ3').text
    titles.append(title)

print(titles)
