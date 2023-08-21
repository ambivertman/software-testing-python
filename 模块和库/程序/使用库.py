import requests


def getStockPrice(stockID):
    url = 'http://hq.sinajs.cn/list=' + stockID
    headers = {'Referer': 'http://finace.sina.com.cn'}
    ret = requests.get(url, headers)
    return ret.text.split(',')[1]


stockID = 'sh601006'
print(getStockPrice(stockID))
