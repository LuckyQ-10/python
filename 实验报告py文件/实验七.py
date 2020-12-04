import requests
import urllib
import time
import os
def picture_url(page): #获取每个图片的url地址
    url_list = []
    for i in range(page+1):
        url = 'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?sDataType=JSON&iListNum=20&page='+str(i)+'&iActId=2735&iTypeId=2'
        req = requests.get(url)
        json = req.json()['List']

        for url in json:
                url_list.append([urllib.parse.unquote(url['sProdImgNo_2'][:-3:])+'0',urllib.parse.unquote(url['sProdName'])])   #对url地址进行解码
        time.sleep(3)
    print('图片URL地址爬取完毕！')
    return url_list

def dow_picture(url):
    address = 'D:\yun0101\python\实验报告py文件\王者荣耀\\'
    os.mkdir(address)
    x = 0
    for i in url:
        req = requests.get(i[0]).content
        with open(address + i[1] + '.jpg', 'wb') as f:  # 保存图片
            f.write(req)
            x += 1
            print(i[1]+'已下载')
    print('总共'+str(x)+'张图片以下载完毕')

dow_picture(picture_url(22))


