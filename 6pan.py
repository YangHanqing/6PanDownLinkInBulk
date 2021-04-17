import requests


print("请输入6盘 Cookie e.g locale=zh-cn; token=1234 ：")
cookie = input()

print("请输入路径名 e.g /路径1/路径2 ：")
pathName = input()

# 获取的文件列表最大值，6盘下载链接有失效时间，需要尽快下载
pageSize = 200

# 解决编码问题
pathName=pathName.encode("utf-8").decode("latin1")

# 解决 eval 函数的问题
false = False
true = True

headers = {
    'authority': 'api.2dland.cn',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'accept': 'application/json, text/plain, */*',
    'dnt': '1',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'content-type': 'application/json',
    'origin': 'https://2dland.cn',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://2dland.cn/',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': cookie,
}


# 根据文件ID换下载链接
def getUrlByIdentity(identity):

    data = '{"identity":"%s"}'%identity
    response = requests.post('https://api.2dland.cn/v3/newfile/download', headers=headers, data=data)
    d = eval(response.text)
    print(d["downloadAddress"])

# 根据文件路径换文件列表
def getFileListByPathName(pathName):
    data = '{"parentPath":"%s","name":"","start":0,"limit":%s,"orderby":[]}' %(pathName,pageSize)
    response = requests.post('https://api.2dland.cn/v3/newfile/list', headers=headers, data=data)
    d = eval(response.text)

    for i in d["dataList"]:
        getUrlByIdentity(i["identity"])

getFileListByPathName(pathName)
