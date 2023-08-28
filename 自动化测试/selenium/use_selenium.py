from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome()
wd.implicitly_wait(10)

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://cdn2.byhy.net/files/selenium/jsweather.html')

forecastBox = wd.find_element(By.ID,'forecastID')
cities = forecastBox.find_elements(By.TAG_NAME, 'dl')
cities_info = {}
for city in cities:
    city_name= city.find_element(By.TAG_NAME,'dt').text
    temp_min = city.find_element(By.TAG_NAME,'span').text[:2]
    cities_info[city_name] = eval(temp_min)

wd.quit()
lowest_temp = min(cities_info.values())
coldest_cities = [city for city,temp in cities_info.items() if temp==lowest_temp]
coldest_cities_str = ','.join(coldest_cities)
print(f"最低温度为{lowest_temp},其中有{coldest_cities_str}")