from selenium import webdriver
from selenium.webdriver.common.by import By
import time

wd = webdriver.Chrome()
wd.get('https://www.51job.com/')
wd.implicitly_wait(5)

#输入python
wd.find_element(By.CSS_SELECTOR,'#kwdselectid').send_keys('python')
#修改城市
wd.find_element(By.CSS_SELECTOR,'#work_position_input').click()
#选择杭州
wd.find_element(By.CSS_SELECTOR,'#work_position_click_center_right_list_category_000000_080200').click()
#点击确定
wd.find_element(By.CSS_SELECTOR,'#work_position_click_bottom_save').click()
#点击搜索
wd.find_element(By.CSS_SELECTOR,'body > div.content > div > div.fltr.radius_5 > div > button').click()

time.sleep(5)
joblist = wd.find_element(By.CSS_SELECTOR,"div.j_joblist")
jobs = joblist.find_elements(By.CSS_SELECTOR,'div.e.sensors_exposure')
for job in jobs:
    jname = job.find_element(By.CSS_SELECTOR,'span.jname.at').text
    jsalary = job.find_element(By.CSS_SELECTOR,'span.sal').text
    cname = job.find_element(By.CSS_SELECTOR,'a.cname.at').text
    print(f"{jname:<15}|{jsalary:<15}|{cname:<20}")

wd.quit()