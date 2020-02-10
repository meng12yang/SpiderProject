from tkinter import *
from movieSpider import *
import webbrowser

#视频详情页
class MovieInfoPage(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry("%dx%d" % (1600, 600))

        #获取爬虫内容
        self.qqMovieDict = getMovieMessage_QQ()
        self.iqiyiMovieDict = getMovieMessage_iqiyi()
        self.bilibiliMovieDict = getMovieMessage_bilibili()

        self.createPage()

    def createPage(self):
        self.qqPage = Frame(self.root)
        self.qqPage.grid(row=0, column=0, stick=N)
        self.iqiyiPage = Frame(self.root)
        self.iqiyiPage.grid(row=0, column=1, stick=N, padx=20)
        self.bilibiliPage = Frame(self.root)
        self.bilibiliPage.grid(row=0, column=2, stick=N)
        self.extraPage = Frame(self.root)
        self.extraPage.grid(row=0, column=3, padx=80)

        #标题
        Label(self.qqPage, text="腾讯视频", font=("华文行楷", 15), fg="blue").pack(pady=20)
        Label(self.iqiyiPage, text="爱奇艺", font=("华文行楷", 15), fg="blue").pack(pady=20)
        Label(self.bilibiliPage, text="哔哩哔哩", font=("华文行楷", 15), fg="blue").pack(pady=20)
        huyaLabel = Label(self.extraPage, text="查看虎牙直播视频", font=("华文行楷", 15), fg="blue", cursor="cross")
        huyaLabel.pack(pady=20)
        douyuLabel = Label(self.extraPage, text="查看斗鱼直播视频", font=("华文行楷", 15), fg="blue", cursor="cross")
        douyuLabel.pack()

        #内容
        #腾讯视频
        temp = 1
        for key in self.qqMovieDict:
            keyStr = StringVar()
            keyStr.set(key)
            Button(self.qqPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
                   command=lambda :self.open_url(self.qqMovieDict[key])).pack(pady=6)
        #爱奇艺
        temp = 1
        for key in self.iqiyiMovieDict:
            keyStr = StringVar()
            keyStr.set(key)
            Button(self.iqiyiPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
                   command=lambda: self.open_url(self.iqiyiMovieDict[key])).pack(pady=6)
        #哔哩哔哩
        temp = 1
        for key in self.bilibiliMovieDict:
            keyStr = StringVar()
            keyStr.set(key)
            Button(self.bilibiliPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
                   command=lambda: self.open_url(self.bilibiliMovieDict[key])).pack(pady=6)

        #虎牙、斗鱼直播标签绑定点击事件
        huyaLabel.bind("<Button-1>", self.getMovie_huya)
        douyuLabel.bind("<Button-1>", self.getMovie_douyu)

    #打开url
    def open_url(self, url):
        webbrowser.open(url, new=0)

    #获取虎牙直播视频
    def getMovie_huya(self, event):
        huyaMovieDict = getMovieMessage_huya()
        top = Toplevel()
        top.title("虎牙直播推荐视频")
        top.geometry("%dx%d" % (500, 600))

        Label(top, text="虎牙直播视频", font=("华文行楷", 15), fg="blue").pack(pady=20)
        temp = 1
        for key in huyaMovieDict:
            keyStr = StringVar()
            keyStr.set(key)
            Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
                   command=lambda: self.open_url(huyaMovieDict[key])).pack(pady=6)

    #获取斗鱼直播视频
    def getMovie_douyu(self, event):
        douyuMovieDict = getMovieMessage_douyu()
        top = Toplevel()
        top.title("斗鱼直播推荐视频")
        top.geometry("%dx%d" % (500, 600))

        Label(top, text="斗鱼直播视频", font=("华文行楷", 15), fg="blue").pack(pady=20)
        temp = 1
        for key in douyuMovieDict:
            keyStr = StringVar()
            keyStr.set(key)
            Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
                   command=lambda: self.open_url(douyuMovieDict[key])).pack(pady=6)


