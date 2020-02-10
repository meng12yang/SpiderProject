from tkinter import *
from movieTopSpider import *
import webbrowser

#视频榜单页面
class MovieTopPage(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry("%dx%d" % (1300, 600))

        #获取爬虫内容
        self.qqTopDict = getMovieTop_QQ()
        self.iqiyiDict = getMovieTop_iqiyi()
        self.bilibiliDict = getMovieTop_bilibili()

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

        # 标题
        Label(self.qqPage, text="腾讯视频榜单", font=("华文行楷", 15), fg="blue").pack(pady=20)
        Label(self.iqiyiPage, text="爱奇艺榜单", font=("华文行楷", 15), fg="blue").pack(pady=20)
        Label(self.bilibiliPage, text="哔哩哔哩榜单", font=("华文行楷", 15), fg="blue").pack(pady=20)
        doubanLabel = Label(self.extraPage, text="查看豆瓣电影榜单", font=("华文行楷", 15), fg="blue", cursor="cross")
        doubanLabel.pack(pady=20)

        # 内容
        # 腾讯视频
        for key in self.qqTopDict:
            keyStr = StringVar()
            keyStr.set(key)
            Button(self.qqPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
                   command=lambda: self.open_url(self.qqTopDict[key])).pack(pady=6)
        #爱奇艺
        for key in self.iqiyiDict:
            keyStr = StringVar()
            keyStr.set(key)
            Button(self.iqiyiPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
                   command=lambda: self.open_url(self.iqiyiDict[key])).pack(pady=6)
        #哔哩哔哩
        for key in self.bilibiliDict:
            keyStr = StringVar()
            keyStr.set(key)
            Button(self.bilibiliPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
                   command=lambda: self.open_url(self.bilibiliDict[key])).pack(pady=6)

        #豆瓣电影榜单标签绑定点击事件
        doubanLabel.bind("<Button-1>", self.getTop_douban)

    # 打开url
    def open_url(self, url):
            webbrowser.open(url, new=0)

    #获取豆瓣电影榜单
    def getTop_douban(self, event):
        doubanTopDict = getMovieTop_douban()
        top = Toplevel()
        top.title("豆瓣电影榜单")
        top.geometry("%dx%d" % (1600, 750))

        Label(top, text="豆瓣电影榜单", font=("华文行楷", 15), fg="blue").grid(row=0, column=0, columnspan=3 ,pady=10)
        rowTemp = 1
        colTemp = 0
        for key in doubanTopDict:
            keyStr = StringVar()
            keyStr.set(key)
            valueStr = StringVar()
            valueStr.set(doubanTopDict[key])
            Label(top, textvariable=keyStr, font=("华文行楷", 12), fg="blue").grid(row=rowTemp, column=colTemp)
            rowTemp += 1
            Label(top, textvariable=valueStr, font=("华文行楷", 12)).grid(row=rowTemp, column=colTemp, pady=5)
            rowTemp += 1
            if rowTemp == 19:
                rowTemp = 1
                colTemp += 1
