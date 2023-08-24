import requests
from threading import Thread, Lock

taskList = [
    'http://httpbin.org/ip',
    'http://lf26-cdn-tos.bytecdntp.com/cdn/expire-1-M/ace/1.4.14/ext-linking.js',
    'http://lf26-cdn-tos.bytecdntp.com/cdn/expire-1-M/Base64/1.1.0/base64.min.js.map',
]

txtlock = Lock()
def crawl(url, idx, contentDict):
    content = requests.get(url).text
    txtlock.acquire()
    contentDict[idx] = content
    txtlock.release()


contentDict = {}
threadlist = []
for idx, url in enumerate(taskList):
    thread = Thread(
        target=crawl,
        args=(url, idx, contentDict)
    )
    thread.start()
    threadlist.append(thread)
    # 循环中，启动线程后，就立即join这个线程对象，
    # 就会一直等待该线程，直到该线程执行完结束，才会从join调用返回
for thread in threadlist:
    thread.join()

with open('./mergedfile.txt', 'a', encoding='utf8') as f:
    for i in range(len(contentDict)):
        f.write(contentDict[i])

print("爬取合并完成")
