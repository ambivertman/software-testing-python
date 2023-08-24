import requests
from threading import Thread,Lock
taskList = [
    'http://httpbin.org/ip',
    'http://lf26-cdn-tos.bytecdntp.com/cdn/expire-1-M/ace/1.4.14/ext-linking.js',
    'http://lf26-cdn-tos.bytecdntp.com/cdn/expire-1-M/Base64/1.1.0/base64.min.js.map',
]

txtlock = Lock()
def crawl(url, filepath):
    content = requests.get(url).text
    txtlock.acquire()
    with open(filepath,'a',encoding='utf8') as f:
        f.write(content)
    txtlock.release()
    print(f"{url}中的内容已写入文件")


for url in taskList:
    thread = Thread(
        target=crawl,
        args = (url,'./mergedfile.txt')
    )
    thread.start()
    thread.join()

print("爬取合并完成")