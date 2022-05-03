from utils import *

def getAll():
    base_url = 'https://search.bilibili.com/all?keyword=%E9%AB%98%E6%95%B0&from_source=webtop_search&spm_id_from=333.851'
    data = []
    try:
        for i in range(10):
            url = base_url + '&page=' + str(i + 1)
            for d in getKeys(getHtml(url)):
                data.append(d)
            print('已抓取', i + 1, '页\n')
    except:
        pass

    with open('a.txt', 'a') as f:
        for d in data:
            for x in d:
                f.write(x + "   ")
            f.write('\n')
        f.close()

    return data

