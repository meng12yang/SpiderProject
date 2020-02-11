import requests
from bs4 import BeautifulSoup

#获取腾讯视频榜单
def getMovieTop_QQ():
    topUrl = "https://v.qq.com/biu/ranks/?t=hotsearch"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari / 537.36',
        'Referer': 'https://v.qq.com/'
    }
    topObj = requests.get(topUrl, headers=headers)
    topObj.encoding = 'utf-8'
    topObj = BeautifulSoup(topObj.text, 'html.parser')
    topDict = {}
    topList = topObj.select("a[rel='noopener noreferrer']")
    for i in range(10):
        topDict[topList[i].get_text()] = "https:" + topList[i].get("href")

    # 返回视频榜单字典（title：href）
    return topDict

#获取爱奇艺视频榜单
def getMovieTop_iqiyi():
    topUrl = "http://top.iqiyi.com/index.html"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari / 537.36',
        'Referer': 'http://v.iqiyi.com/'
    }
    topObj = requests.get(topUrl, headers=headers)
    topObj.encoding = 'utf-8'
    topObj = BeautifulSoup(topObj.text, 'html.parser')
    topDict = {}
    topList = topObj.select(".title-left-box a")
    for i in range(10):
        topDict[topList[i].get_text()] = "https:" + topList[i].get("href")

    # 返回视频榜单字典（title：href）
    return topDict

#获取哔哩哔哩视频榜单
def getMovieTop_bilibili():
    topUrl = "https://www.bilibili.com/ranking?spm_id_from=333.851.b_7072696d61727950616765546162.3"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari / 537.36',
        'Referer': 'https://www.bilibili.com/'
    }
    topObj = requests.get(topUrl, headers=headers)
    topObj.encoding = 'utf-8'
    topObj = BeautifulSoup(topObj.text, 'html.parser')
    topDict = {}
    topList = topObj.select(".info a.title")
    for i in range(10):
        topDict[topList[i].get_text()] = topList[i].get("href")

    # 返回视频榜单字典（title：href）
    return topDict

#获取豆瓣电影top250榜单
def getMovieTop_douban():
    topUrl = "https://movie.douban.com/top250"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari / 537.36',
        'Referer': 'https://movie.douban.com/'
    }
    topObj = requests.get(topUrl, headers=headers)
    topObj.encoding = 'utf-8'
    topObj = BeautifulSoup(topObj.text, 'html.parser')
    topDict = {}
    titleList = topObj.select(".hd a")     #标题列表
    msgList = topObj.select(".info .bd p")       #内容列表
    for i in range(len(titleList)):
        topDict[titleList[i].get_text().strip().replace("\n", "").replace(" ", "")] = msgList[i].get_text().strip().replace(" ", "")

    # 返回视频榜单字典（title：msg）
    return topDict

if __name__ == '__main__':
    # getMovieTop_QQ()
    # getMovieTop_iqiyi()
    # getMovieTop_bilibili()
    getMovieTop_douban()