from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get('https://y.qq.com/n/ryqq/toplist/27')

songlist = wd.find_element(By.CLASS_NAME,'songlist__list')
songs = songlist.find_elements(By.TAG_NAME,"li")

rank_up_songs = []
for song in songs:
    try:
        song.find_element(By.CLASS_NAME,'icon_rank_up')
        rank_up_songs.append(song)
    except:
        continue

for song in rank_up_songs:
    print(f"{song.find_element(By.CSS_SELECTOR,'a[title]:not([class])').get_attribute('title'):<25}:"
          f"{song.find_element(By.CLASS_NAME,'songlist__artist').text:>10}")

wd.quit()
