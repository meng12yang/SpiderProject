import requests
from bs4 import BeautifulSoup

#获取腾讯视频视频信息
def getMovieMessage_QQ():
    startUrl = "https://v.qq.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Referer': 'https://v.qq.com/'
    }
    startObj = requests.get(startUrl, headers=headers)
    startObj.encoding = 'utf-8'
    startObj = BeautifulSoup(startObj.text, 'html.parser')
    movieDict = {}
    movieList = startObj.find_all('a', attrs={'class':'nav_link', 'data-navcolor':'undefined'})
    # 删除冗余数据
    movieList.pop()
    for i in range(len(movieList)):
        movieDict[movieList[i].get_text()] = movieList[i].get("href")

    #返回视频字典（title:href）
    return movieDict

#获取爱奇艺视频信息
def getMovieMessage_iqiyi():
    startUrl = "https://www.iqiyi.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Referer': 'https://www.iqiyi.com/'
    }
    startObj = requests.get(startUrl, headers=headers)
    startObj.encoding = 'utf-8'
    startObj = BeautifulSoup(startObj.text, 'html.parser')
    movieDict = {}
    movieList = startObj.find_all('a', attrs={'class': 'side-link'})
    for i in range(len(movieList)):
        movieDict[movieList[i].get_text().strip()] = movieList[i].get("href")

    # 返回视频字典（title:href）
    return movieDict

#获取优酷视频信息
def getMovieMessage_youku():
    startUrl = "https://www.youku.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Referer': 'https://www.youku.com/'
    }
    startObj = requests.get(startUrl, headers=headers)
    startObj.encoding = 'utf-8'
    startObj = BeautifulSoup(startObj.text, 'html.parser')
    movieDict = {}
    movieList = startObj.find_all('a', attrs={'class': 'swiper-slide'})
    for i in range(len(movieList)):
        movieDict[movieList[i].get_text().strip()] = "https:" + movieList[i].get("href")

    # 返回视频字典（title:href）
    return movieDict

#获取哔哩哔哩视频信息
def getMovieMessage_bilibili():
    startUrl = "https://www.bilibili.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Referer': 'https://www.bilibili.com/'
    }
    startObj = requests.get(startUrl, headers=headers)
    startObj.encoding = 'utf-8'
    startObj = BeautifulSoup(startObj.text, 'html.parser')
    movieDict = {}
    movieList = startObj.select(".info-box a")
    for i in range(len(movieList)):
        movieDict[movieList[i].get_text().strip()] = "https:" + movieList[i].get("href")

    # 返回视频字典（title:href）
    return movieDict


# 获取虎牙视频信息
def getMovieMessage_huya():
    startUrl = "https://www.huya.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Referer': 'https://www.huya.com/'
    }
    startObj = requests.get(startUrl, headers=headers)
    startObj.encoding = 'utf-8'
    startObj = BeautifulSoup(startObj.text, 'html.parser')
    movieDict = {}
    movieList = startObj.find_all('a', attrs={'class': 'remen-item new-clickstat'})
    for i in range(len(movieList)):
        movieDict[movieList[i].get_text().strip()] = movieList[i].get("href")

    # 返回视频字典（title:href）
    return movieDict

# 获取斗鱼视频信息
def getMovieMessage_douyu():
    startUrl = "https://www.douyu.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Referer': 'https://www.douyu.com/'
    }
    startObj = requests.get(startUrl, headers=headers)
    startObj.encoding = 'utf-8'
    startObj = BeautifulSoup(startObj.text, 'html.parser')
    movieDict = {}
    movieList = startObj.select("div.layout-Module-container ul li.layout-List-item a")
    for i in range(len(movieList)):
        movieDict[movieList[i].get_text().strip()] = "https://www.douyu.com" + movieList[i].get("href")

    # 返回视频字典（title:href）
    return movieDict

if __name__ == '__main__':
    # getMovieMessage_QQ()
    # getMovieMessage_iqiyi()
    # getMovieMessage_youku()
    # getMovieMessage_bilibili()
    # getMovieMessage_huya()
    getMovieMessage_douyu()