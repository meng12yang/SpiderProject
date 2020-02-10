import requests
import urllib.parse
import json

#获取QQ音乐歌曲详细页网址
#musicName：歌曲名称
def getMusicContentUrl_QQ(musicName):
    musicName = urllib.parse.quote(musicName)
    startUrl = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=63634299934024947&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%s&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0"%musicName
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari / 537.36',
        'Referer': 'https://y.qq.com/'
    }
    startObj = requests.get(startUrl, headers=headers)
    startObj.encoding = 'utf-8'
    res = json.loads(startObj.text)
    song_type = res['data']['song']['list'][0]['type']
    song_mid = res['data']['song']['list'][0]['mid']
    song_id = res['data']['song']['list'][0]['id']
    musicDict = {"song_type":str(song_type), "song_mid":str(song_mid), "song_id":str(song_id)}
    return musicDict

#获取QQ音乐歌曲信息
#musicName：歌曲名称
def getMusicMessage_QQ(musicName):
    musicDict = getMusicContentUrl_QQ(musicName)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari / 537.36',
        'Referer': 'https://y.qq.com/'
    }
    #1.爬取歌曲基本信息
    data = '{"comm":{"ct":24,"cv":0},"songinfo":{"method":"get_song_detail_yqq","param":{"song_type":'+ musicDict["song_type"] +',"song_mid":"'+ musicDict["song_mid"] +'","song_id":'+ musicDict["song_id"] +'},"module":"music.pf_song_detail_svr"}}'
    basicUrl = "https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI8252236102860127&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%s"%data
    basicObj = requests.get(basicUrl, headers=headers)
    res = json.loads(basicObj.text)
    try:
        company = res['songinfo']['data']['info']['company']['content'][0]['value']    #唱片公司
    except BaseException:
        company = "无"
    try:
        genre = res['songinfo']['data']['info']['genre']['content'][0]['value']    #歌曲流派
    except BaseException:
        genre = "无"
    try:
        intro = res['songinfo']['data']['info']['intro']['content'][0]['value']    #简介
    except BaseException:
        intro = "无"
    try:
        lan = res['songinfo']['data']['info']['lan']['content'][0]['value']        #歌曲语种
    except BaseException:
        lan = "无"
    try:
        pub_time = res['songinfo']['data']['info']['pub_time']['content'][0]['value']      #发行时间
    except BaseException:
        pub_time = "无"
    try:
        singer = res['songinfo']['data']['track_info']['singer'][0]['name']        #歌手
    except BaseException:
        singer = "无"
    try:
        album = res['songinfo']['data']['track_info']['album']['name']             #专辑
    except BaseException:
        album = "无"

    #2.爬取歌词
    lyricUrl = "https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg?nobase64=1&musicid=%s&-=jsonp1&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0"%musicDict["song_id"]
    lyricObj = requests.get(lyricUrl, headers=headers)
    res = json.loads(lyricObj.text)
    try:
        lyric = res['lyric']      #歌词
    except BaseException:
        lyric = "无"

    #3.爬取评论
    commentDict = {}
    commentUrl = "https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid=%s&cmd=8&needmusiccrit=0&pagenum=0&pagesize=25&lasthotcommentid=&domain=qq.com&ct=24&cv=10101010"%musicDict["song_id"]
    commentObj = requests.get(commentUrl, headers=headers)
    res = json.loads(commentObj.text)
    commentList = res["hot_comment"]["commentlist"]
    for i in range(len(commentList)):
        commentAuthor = commentList[i]["nick"]      #评论作者
        commentContent = commentList[i]["rootcommentcontent"]     #评论内容
        commentDict[commentAuthor] = commentContent

    basicDict = {"company":company, "genre":genre, "intro":intro, "lan":lan, "pub_time":pub_time, "singer":singer, "album":album, "lyric":lyric}

    #返回基本信息（包括歌词）字典和评论字典
    return basicDict, commentDict

#获取酷我音乐详细页网址
#musicName：歌曲名称
def getMusicContentUrl_kuwo(musicName):
    musicName = urllib.parse.quote(musicName)
    startUrl = "http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key=%s&pn=1&rn=30&reqId=84584990-295c-11ea-8ac9-8f8ca17b0a5d"%musicName
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1577523112,1577523486,1577524182; userid=502498009; username=1577527750270qq; logintype=3; uph=1135078146; sid=35327287_1; websid=790433257; uname3=%u6070%u540C%u5B66%u5C11%u5E74; t3kwid=502498009; pic3="http://qzapp.qlogo.cn/qzapp/100243533/F3EE8E63D465A54C3C6847FDE378E5EA/100"; t3=qq; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1577528724; kw_token=THM7JQ99MYD',
        'csrf': 'THM7JQ99MYD',
        'Referer': 'http://www.kuwo.cn/'
    }
    startObj = requests.get(startUrl, headers=headers)
    startObj.encoding = 'utf-8'
    res = json.loads(startObj.text)
    sid = res["data"]["list"][0]["rid"]
    return str(sid)

#获取酷我音乐歌曲信息
#musicName：歌曲名称
def getMusicMessage_kuwo(musicName):
    sid = getMusicContentUrl_kuwo(musicName)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1577523112,1577523486; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1577523486; kw_token=DZ9S3AHT8LM',
        'Referer': 'http://www.kuwo.cn/'
    }
    #爬取歌曲评论
    commentDict = {}
    commentUrl = "http://www.kuwo.cn/comment?type=get_rec_comment&f=web&page=1&rows=20&digest=15&sid=%s&uid=0&prod=newWeb&reqId=2fe0ab70-295a-11ea-8313-090b380a9d73"%sid
    commentObj = requests.get(commentUrl, headers=headers)
    commentObj.encoding = 'utf-8'
    res = json.loads(commentObj.text)
    rows = res["rows"]
    for i in range(len(rows)):
        commentContent = rows[i]["msg"]     #评论内容
        commentTime = rows[i]["time"]       #评论时间
        commentDict[commentTime] = commentContent

    #返回评论字典
    return commentDict

#获取虾米音乐歌曲id
#musicName：歌曲名称
def getMusicContentUrl_xiami(musicName):
    musicName = urllib.parse.quote(musicName)
    keyDict = '{"key":"'+ musicName +'","pagingVO":{"page":1,"pageSize":30}}'
    startUrl = "https://www.xiami.com/api/search/searchSongs?_q=%s&_s=57c64effc16038cb1ff7853d9238b04e"%keyDict
    print(startUrl)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Referer': 'https://www.xiami.com',
        'Cookie': 'xmgid=fa628e67-a8e0-4ede-a44d-8043abc20d7d; cna=aUGPFgGljQACAXE5sL317EqB; gid=157760470330848; _unsign_token=521c07f2396f56ec54a5a1c3231bf79f; UM_distinctid=16f50da3072548-069e91898d759a-55123a11-144000-16f50da3073776; xm_sg_tk=7b6f96f217d75c2cabd336260cd264d9_1581245948598; xm_sg_tk.sig=yFiTNVuXEImq9MJ6TO-hXNhK9nm13sU6yMyLrrJLi1I; _xm_umtoken=T042AFED0684540374EAF4F614CA01CEFD1F30DC4AA7D3EA502687249A0; xm_traceid=0be2de0e15812459753601165ee37f; xm_oauth_state=20cd212ed2f805520e64dd5df138cca5; _xm_cf_=HidLxOkxTrEB2CLeur14DxoJ; isg=BM_PAvEmzflLR8rmz3Nyst4FXmPZ9CMW-6tyluHcBj5tsOyy-cE3Zg_hsuAOyPuO; l=cBx7L5PrquaBKPr5BOCwhurza77OGIRfguPzaNbMi_5B79T6c7_Oo2v1uh96cjWhTFxB4VvT4w2TxUL7J_sw7_98vuEbw'
    }
    startObj = requests.get(startUrl, headers=headers)
    startObj.encoding = 'utf-8'
    res = json.loads(startObj.text)
    mid = res['result']['data']['songs'][0]['songStringId']

    #返回歌曲id
    return str(mid)


#获取虾米音乐歌曲信息
#musicName：歌曲名称
def getMusicMessage_xiami(musicName):
    mid = getMusicContentUrl_xiami(musicName)
    q = '{"objectId":'+ mid +',"objectType":"song","pagingVO":{"page":1,"pageSize":20}}'
    startUrl = "https://www.xiami.com/api/comment/getCommentList?_q=%7B%22objectId%22:%22mSHNI555c51%22,%22objectType%22:%22song%22,%22pagingVO%22:%7B%22page%22:1,%22pageSize%22:20%7D%7D&_s=37f41f579d84d04a7d06239f265ed953"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Referer': 'https://www.xiami.com',
        'Cookie': 'xmgid=fa628e67-a8e0-4ede-a44d-8043abc20d7d; xm_sg_tk=11a79f0180564d098ecc1275b5414f81_1577604028654; xm_sg_tk.sig=wionlEBuaWKAQiSd-ZYhL-D3LIMX2gjCA-K_32kByxI; cna=aUGPFgGljQACAXE5sL317EqB; _xm_umtoken=T69B6E966C014E946629541C505BD76FC47C43C272D47E64C6D47FB20F3; xm_traceid=0b0fdd0215776043963498591e930e; xm_oauth_state=72f83161a8f4bee0d13172375bf54c41; _xm_cf_=NptGMeUrj0Um-Ae4AnA0oZSF; isg=BDo6R0E7ML01mr8Fatw_YSNCi2Bc677Fdoxn9UQyjk8CN91xI3mr1doGh4NOpzZd; l=cBx7L5PrquaBKD1-BOfaKurza77T1IObzsPzaNbMiICPO8W952lhWZcTdCKpCnGVLst2u3uMBu73B-Y3ly4EQ6AJpXyavnSl'
    }
    startObj = requests.get(startUrl, headers=headers)
    startObj.encoding = 'utf-8'
    res = json.loads(startObj.text)
    commentDict = {}
    commentList = res['result']['data']['commentList']
    for i in range(len(commentList)):
        commentAuthor = commentList[i]['nickName']       #评论作者
        commentContent = commentList[i]['message']       #评论内容
        commentDict[commentAuthor] = commentContent

    print(commentDict)
    #返回评论列表
    return commentDict

if __name__ == '__main__':
    musicName = "等你下课"
    # getMusicMessage_QQ(musicName)
    # getMusicMessage_kuwo(musicName)
    getMusicMessage_xiami(musicName)
