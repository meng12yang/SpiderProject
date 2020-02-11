import requests
from bs4 import BeautifulSoup
import json

#获取新浪新闻要闻
def getNewsMessage_sina():
    hotUrl = "http://news.sina.com.cn"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari / 537.36',
        'Referer': 'http://news.sina.com.cn/'
    }
    hotObj = requests.get(hotUrl, headers=headers)
    hotObj.encoding = 'utf-8'
    hotObj = BeautifulSoup(hotObj.text, 'html.parser')
    hotList = hotObj.select("div.ct_t_01 h1 a")
    hotDict = {}
    for i in range(len(hotList)):
        hotDict[hotList[i].get_text()] = hotList[i].get("href")

    #返回新浪新闻要闻字典（title:href）
    return hotDict

#获取凤凰网新闻要闻
def getNewsMessage_ifeng():
    hotUrl = "http://news.ifeng.com"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari / 537.36',
        'Referer': 'http://news.ifeng.com/'
    }
    hotObj = requests.get(hotUrl, headers=headers)
    hotObj.encoding = 'utf-8'
    hotObj = BeautifulSoup(hotObj.text, 'html.parser')
    hotList = hotObj.select("div.topNews-2BQWVUtl h3 a")
    hotDict = {}
    for i in range(len(hotList)):
        hotDict[hotList[i].get_text()] = hotList[i].get("href")

    # 返回凤凰网新闻要闻字典（title:href）
    return hotDict

#获取澎湃新闻要闻
def getNewsMessage_pengpai():
    hotUrl = "http://www.thepaper.cn"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari / 537.36',
        'Referer': 'http://www.thepaper.cn/'
    }
    hotObj = requests.get(hotUrl, headers=headers)
    hotObj.encoding = 'utf-8'
    hotObj = BeautifulSoup(hotObj.text, 'html.parser')
    hotList = hotObj.select("ul.list_hot li a")
    hotDict = {}
    for i in range(10):
        hotDict[hotList[i].get_text()] = "http://www.thepaper.cn/"+hotList[i].get("href")

    # 返回澎湃新闻要闻字典（title:href）
    return hotDict

#获取搜狐新闻要闻
def getNewsMessage_sohu():
    hotUrl = "http://news.sohu.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari / 537.36',
        'Referer': 'http://news.sohu.com/'
    }
    hotObj = requests.get(hotUrl, headers=headers)
    hotObj.encoding = 'utf-8'
    hotObj = BeautifulSoup(hotObj.text, 'html.parser')
    hotDict = {}
    hotList = hotObj.select("div.choice-pic a")
    hotDict[hotList[0].get("title")] = "http:"+hotList[0].get("href")
    hotList = hotObj.select("div.choice-list ul li a")
    for i in range(len(hotList)):
        hotDict[hotList[i].get_text()] = "http:"+hotList[i].get("href")

    # 返回搜狐新闻要闻字典（title:href）
    return hotDict

#获取环球网新闻要闻
def getNewsMessage_huanqiu():
    hotUrl = "https://www.huanqiu.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari / 537.36',
        'Referer': 'https://www.huanqiu.com/'
    }
    hotObj = requests.get(hotUrl, headers=headers)
    hotObj.encoding = 'utf-8'
    hotObj = BeautifulSoup(hotObj.text, 'html.parser')
    hotDict = {}
    hotList = hotObj.select("div.secNewsList p.listp a")
    for i in range(10):
        hotDict[hotList[i].get_text()] = hotList[i].get("href")

    # 返回环球网新闻要闻字典（title:href）
    return hotDict

#获取南方周末新闻要闻
def getNewsMessage_infzm():
    hotUrl = "http://www.infzm.com/topics/t1.html"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari / 537.36',
        'Referer': 'http://www.infzm.com/topics/t1.html',
    }
    hotObj = requests.get(hotUrl, headers=headers)
    hotObj.encoding = 'utf-8'
    hotObj = BeautifulSoup(hotObj.text, 'html.parser')
    hotDict = {}
    titleList = hotObj.select("div.row div.col-sm-8 article ul li a h5")
    hrefList = hotObj.select("div.row div.col-sm-8 article ul li a")
    for i in range(len(titleList)):
        hotDict[titleList[i].get_text().strip()] = "http://www.infzm.com"+hrefList[i].get("href")

    # 返回南方周末新闻要闻字典（title:href）
    return hotDict

#获取百度新闻要闻
def getNewsMessage_baidu():
    hotUrl = "http://news.baidu.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari / 537.36',
        'Referer': 'http://news.baidu.com/',
    }
    hotObj = requests.get(hotUrl, headers=headers)
    hotObj.encoding = 'utf-8'
    hotObj = BeautifulSoup(hotObj.text, 'html.parser')
    hotDict = {}
    hotList = hotObj.select("div.hotnews ul li strong a")
    for i in range(len(hotList)):
        hotDict[hotList[i].get_text()] = hotList[i].get("href")

    # 返回百度新闻要闻字典（title:href）
    return hotDict

if __name__ == '__main__':
    # getNewsMessage_sina()
    # getNewsMessage_ifeng()
    # getNewsMessage_pengpai()
    # getNewsMessage_sohu()
    # getNewsMessage_huanqiu()
    # getNewsMessage_infzm()
    getNewsMessage_baidu()