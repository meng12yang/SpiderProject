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
        keys1 = list(self.qqMovieDict.keys())
        values1 = list(self.qqMovieDict.values())
        keyStr = StringVar()
        keyStr.set(keys1[0])
        Button(self.qqPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values1[0])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys1[1])
        Button(self.qqPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values1[1])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys1[2])
        Button(self.qqPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values1[2])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys1[3])
        Button(self.qqPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values1[3])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys1[4])
        Button(self.qqPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values1[4])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys1[5])
        Button(self.qqPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values1[5])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys1[6])
        Button(self.qqPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values1[6])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys1[7])
        Button(self.qqPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values1[7])).pack(pady=6)
        #爱奇艺
        keys2 = list(self.iqiyiMovieDict.keys())
        values2 = list(self.iqiyiMovieDict.values())
        keyStr = StringVar()
        keyStr.set(keys2[0])
        Button(self.iqiyiPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values2[0])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys2[1])
        Button(self.iqiyiPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values2[1])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys2[2])
        Button(self.iqiyiPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values2[2])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys2[3])
        Button(self.iqiyiPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values2[3])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys2[4])
        Button(self.iqiyiPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values2[4])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys2[5])
        Button(self.iqiyiPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values2[5])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys2[6])
        Button(self.iqiyiPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values2[6])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys2[7])
        Button(self.iqiyiPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values2[7])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys2[8])
        Button(self.iqiyiPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values2[8])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys2[9])
        Button(self.iqiyiPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values2[9])).pack(pady=6)
        #哔哩哔哩
        keys = list(self.bilibiliMovieDict.keys())
        values = list(self.bilibiliMovieDict.values())
        keyStr = StringVar()
        keyStr.set(keys[0])
        Button(self.bilibiliPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[0])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[1])
        Button(self.bilibiliPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[1])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[2])
        Button(self.bilibiliPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[2])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[3])
        Button(self.bilibiliPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[3])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[4])
        Button(self.bilibiliPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[4])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[5])
        Button(self.bilibiliPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[5])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[6])
        Button(self.bilibiliPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[6])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[7])
        Button(self.bilibiliPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[7])).pack(pady=6)

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
        keys = list(huyaMovieDict.keys())
        values = list(huyaMovieDict.values())
        keyStr = StringVar()
        keyStr.set(keys[0])
        Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[0])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[1])
        Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[1])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[2])
        Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[2])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[3])
        Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[3])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[4])
        Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[4])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[5])
        Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[5])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[6])
        Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[6])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[7])
        Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[7])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[8])
        Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[8])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[9])
        Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[9])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[10])
        Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[10])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[11])
        Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[11])).pack(pady=6)

    #获取斗鱼直播视频
    def getMovie_douyu(self, event):
        douyuMovieDict = getMovieMessage_douyu()
        top = Toplevel()
        top.title("斗鱼直播推荐视频")
        top.geometry("%dx%d" % (500, 600))

        Label(top, text="斗鱼直播视频", font=("华文行楷", 15), fg="blue").pack(pady=20)
        keys = list(douyuMovieDict.keys())
        values = list(douyuMovieDict.values())
        keyStr = StringVar()
        keyStr.set(keys[0])
        Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[0])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[1])
        Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[1])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[2])
        Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[2])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[3])
        Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[3])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[4])
        Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[4])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[5])
        Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[5])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[6])
        Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[6])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[7])
        Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[7])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[8])
        Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[8])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[9])
        Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[9])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[10])
        Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[10])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[11])
        Button(top, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[11])).pack(pady=6)


