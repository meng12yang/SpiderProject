import requests
import json
import time
from bs4 import BeautifulSoup

#获取QQ音乐榜单
def getMusicTop_QQ():
    currentDate = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    data = '{"detail":{"module":"musicToplist.ToplistInfoServer","method":"GetDetail","param":{"topId":4,"offset":0,"num":20,"period":'+ currentDate +'}},"comm":{"ct":24,"cv":0}}'
    topUrl = "https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI6453559837868272&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22topId%22%3A4%2C%22offset%22%3A0%2C%22num%22%3A20%2C%22period%22%3A%222019-12-29%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari / 537.36',
        'Referer': 'https://y.qq.com/',
        'Cookie': 'yqq_stat=0; pgv_info=ssid=s4911121138; ts_refer=www.baidu.com/link; pgv_pvid=1516219040; ts_uid=49965356; pgv_pvi=2006104064; pgv_si=s7889741824; ts_last=y.qq.com/n/yqq/toplist/4.html; userAction=1'
    }
    topObj = requests.get(topUrl, headers=headers)
    topObj.encoding = 'utf-8'
    res = json.loads(topObj.text)
    topDict = {}
    songList = res['detail']['data']['data']['song']
    for i in range(len(songList)):
        title = songList[i]['title']          #歌曲名
        singer = songList[i]['singerName']    #歌手
        topDict[title] = singer

    #返回歌曲榜单字典（title：singer）
    return topDict

#获取酷我音乐榜单
def getMusicTop_kuwo():
    topUrl = "http://www.kuwo.cn/api/www/bang/bang/musicList?bangId=93&pn=1&rn=30&reqId=94c75540-2a16-11ea-8d57-536a4f759f79"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari / 537.36',
        'Referer': 'http://www.kuwo.cn/',
        'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1577523486,1577524182,1577597359,1577608675; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1577608675; kw_token=0M32KHUOY1',
        'csrf': '0M32KHUOY1'
    }
    topObj = requests.get(topUrl, headers=headers)
    topObj.encoding = 'utf-8'
    res = json.loads(topObj.text)
    topList = []
    songList = res['data']['musicList']
    for i in range(len(songList)):
        title = songList[i]['name']          #歌曲名
        singer = songList[i]['artist']      #歌手
        album = songList[i]['album']        #专辑
        topList.append([title, singer, album])

    #返回歌曲榜单列表（[title, singer, album]）
    return topList

#获取虾米音乐榜单
def getMusicTop_xiami():
    topUrl = "https://emumo.xiami.com/chart/data?c=103&type=0&page=1&limit=100&_=1577609624058"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari / 537.36',
        'Referer': 'https://emumo.xiami.com/chart',
        'Cookie': 'xmgid=fa628e67-a8e0-4ede-a44d-8043abc20d7d; xm_sg_tk=11a79f0180564d098ecc1275b5414f81_1577604028654; xm_sg_tk.sig=wionlEBuaWKAQiSd-ZYhL-D3LIMX2gjCA-K_32kByxI; cna=aUGPFgGljQACAXE5sL317EqB; gid=157760470330848; PHPSESSID=bdb815b8e5e190368abb60d3dce645cb; _xiamitoken=9a57478b21e29b7901ba2447352abfba; _unsign_token=521c07f2396f56ec54a5a1c3231bf79f; xm_traceid=0b01dc9615776061358793214e0419; xm_oauth_state=9d2124a993782cb1d9cff0011c677ecb; join_from=1zufSNtP6D010%2FjCCA; music_tab=%2Fmusic%2Fhot; UM_distinctid=16f50da3072548-069e91898d759a-55123a11-144000-16f50da3073776; CNZZDATA921634=cnzz_eid%3D2036678880-1577608558-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1577608558; CNZZDATA2629111=cnzz_eid%3D312127067-1577607809-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1577607809; isg=BJ-fogWzPV6UHzoWP2MCIm4VLvMpBPOmS7uiBjHs9s6VwL5COdH_9vXRghAb2Mse; l=cBx7L5PrquaBK_cdBOfZnurza77OZIRb4sPzaNbMiICPO7CB5KKGWZcTcA86CnGVp6hkR3uMBu73BeYBqgUqaLYVEK6Au'
    }
    topObj = requests.get(topUrl, headers=headers)
    topObj.encoding = 'utf-8'
    topObj = BeautifulSoup(topObj.text, 'html.parser')
    titleList = topObj.select(".info p strong a")     #歌曲名列表
    singerList = topObj.select("a.artist")             #歌手列表
    topDict = {}
    for i in range(20):
        topDict[titleList[i].get_text()] = singerList[i].get_text()

    # 返回歌曲榜单列表（title:singer）
    return topDict

#获取豆瓣音乐榜单（豆瓣音乐top250）
def getMusicTop_douban():
    topUrl = "https://music.douban.com/top250"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari / 537.36',
        'Referer': 'https://emumo.xiami.com/chart'
    }
    topObj = requests.get(topUrl, headers=headers)
    topObj.encoding = 'utf-8'
    topObj = BeautifulSoup(topObj.text, 'html.parser')
    topDict = {}
    titleList = topObj.select("div.pl2 a")       #标题列表
    msgList = topObj.select("div.pl2 p.pl")      #信息列表
    #删除标题列表中的冗余数据
    tempList = []
    for i in range(len(titleList)):
        if len(titleList[i].get_text()) == 0:
            tempList.append(titleList[i])
    for i in range(len(tempList)):
        titleList.remove(tempList[i])

    for i in range(len(titleList)):
        topDict[titleList[i].get_text().strip()] = msgList[i].get_text()

    # 返回歌曲榜单列表（title:msg）
    return topDict

#获取酷狗音乐榜单
def getMusicTop_kugou():
    topUrl = "https://www.kugou.com/yy/html/rank.html"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari / 537.36',
        'Referer': 'https://www.kugou.com/'
    }
    topObj = requests.get(topUrl, headers=headers)
    topObj.encoding = 'utf-8'
    topObj = BeautifulSoup(topObj.text, 'html.parser')
    topDict = {}
    msgList = topObj.select(".pc_temp_songname")  # 信息列表
    for i in range(len(msgList)):
        msg = msgList[i].get_text().split(" ")
        topDict[msg[2]] = msg[0]

    # 返回歌曲榜单列表（title:singer）
    return topDict

if __name__ == '__main__':
    # getMusicTop_QQ()
    # getMusicTop_kuwo()
    getMusicTop_xiami()
    # getMusicTop_douban()
    # getMusicTop_kugou()