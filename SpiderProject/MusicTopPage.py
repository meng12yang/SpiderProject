from tkinter import *
from musicTopSpider import *

#音乐排行榜页
class MusicTopPage(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry("%dx%d" % (1300, 800))

        #获取爬虫内容
        self.qqTopDict = getMusicTop_QQ()
        self.kuwoTopList = getMusicTop_kuwo()

        self.createPage()

    def createPage(self):
        self.qqPage = Frame(self.root)
        self.qqPage.grid(row=0, column=0, stick=N)
        self.kuwoPage = Frame(self.root)
        self.kuwoPage.grid(row=0, column=1, stick=N)
        self.extraPage = Frame(self.root)
        self.extraPage.grid(row=0, column=2, padx=80)

        #标题
        Label(self.qqPage, text="QQ音乐榜单", font=("华文行楷", 15), fg="blue").grid(row=0, column=0, columnspan=2, pady=10)
        Label(self.kuwoPage, text="酷我音乐榜单", font=("华文行楷", 15), fg="blue").grid(row=0, column=0, columnspan=3, pady=10)
        xiamiLabel = Label(self.extraPage, text="查看虾米音乐榜单", font=("华文行楷", 15), fg="blue", cursor="cross")
        xiamiLabel.pack()
        doubanLabel = Label(self.extraPage, text="查看豆瓣音乐榜单", font=("华文行楷", 15), fg="blue", cursor="cross")
        doubanLabel.pack(pady=20)
        kugouLabel = Label(self.extraPage, text="查看酷狗音乐榜单", font=("华文行楷", 15), fg="blue", cursor="cross")
        kugouLabel.pack()

        #导航
        Label(self.qqPage, text="歌曲", font=("华文行楷", 12), fg="blue").grid(row=1, column=0, stick=E)
        Label(self.qqPage, text="歌手", font=("华文行楷", 12), fg="blue").grid(row=1, column=1, stick=W, padx=10)
        Label(self.kuwoPage, text="歌曲", font=("华文行楷", 12), fg="blue").grid(row=1, column=0, stick=E)
        Label(self.kuwoPage, text="歌手", font=("华文行楷", 12), fg="blue").grid(row=1, column=1, stick=W, padx=10)
        Label(self.kuwoPage, text="专辑", font=("华文行楷", 12), fg="blue").grid(row=1, column=2, stick=W)

        #内容
        #QQ音乐榜单
        temp = 2
        for key in self.qqTopDict:
            keyStr = StringVar()
            keyStr.set(key)
            valueStr = StringVar()
            valueStr.set(self.qqTopDict[key])
            Label(self.qqPage, textvariable=keyStr, font=("华文行楷", 12)).grid(row=temp, column=0, stick=E)
            Label(self.qqPage, textvariable=valueStr, font=("华文行楷", 12)).grid(row=temp, column=1, stick=W, padx=10)
            temp += 1
        #酷我音乐榜单
        temp = 2
        for i in range(len(self.kuwoTopList)):
            titleStr = StringVar()
            titleStr.set(self.kuwoTopList[i][0])
            singerStr = StringVar()
            singerStr.set(self.kuwoTopList[i][1])
            albumStr = StringVar()
            albumStr.set(self.kuwoTopList[i][2])
            Label(self.kuwoPage, textvariable=titleStr, font=("华文行楷", 12)).grid(row=temp, column=0, stick=E)
            Label(self.kuwoPage, textvariable=singerStr, font=("华文行楷", 12)).grid(row=temp, column=1, stick=W, padx=10)
            Label(self.kuwoPage, textvariable=albumStr, font=("华文行楷", 12)).grid(row=temp, column=2, stick=W)
            temp += 1

        #虾米、豆瓣、酷狗音乐榜单标签绑定点击事件
        xiamiLabel.bind("<Button-1>", self.getTop_xiami)
        doubanLabel.bind("<Button-1>", self.getTop_douban)
        kugouLabel.bind("<Button-1>", self.getTop_kugou)

    #获取虾米音乐榜单
    def getTop_xiami(self, event):
        xiamiTopDict = getMusicTop_xiami()
        top = Toplevel()
        top.title("虾米音乐榜单")
        top.geometry("%dx%d" % (500, 700))

        Label(top, text="虾米音乐榜单", font=("华文行楷", 15), fg="blue").grid(row=0, column=0, columnspan=2, pady=10)
        Label(top, text="歌曲", font=("华文行楷", 12), fg="blue").grid(row=1, column=0, stick=E)
        Label(top, text="歌手", font=("华文行楷", 12), fg="blue").grid(row=1, column=1, stick=W, padx=10)
        temp = 2
        for key in xiamiTopDict:
            keyStr = StringVar()
            keyStr.set(key)
            valueStr = StringVar()
            valueStr.set(xiamiTopDict[key])
            Label(top, textvariable=keyStr, font=("华文行楷", 12)).grid(row=temp, column=0, stick=E)
            Label(top, textvariable=valueStr, font=("华文行楷", 12)).grid(row=temp, column=1, stick=W, padx=10)
            temp += 1

    #获取豆瓣音乐榜单
    def getTop_douban(self, event):
        doubanTopDict = getMusicTop_douban()
        top = Toplevel()
        top.title("豆瓣音乐榜单")
        top.geometry("%dx%d" % (1300, 700))

        Label(top, text="豆瓣音乐榜单", font=("华文行楷", 15), fg="blue").grid(row=0, column=0, columnspan=3 ,pady=10)
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

    #获取酷狗音乐榜单
    def getTop_kugou(self, event):
        kugouTopDict = getMusicTop_kugou()
        top = Toplevel()
        top.title("酷狗音乐榜单")
        top.geometry("%dx%d" % (400, 700))

        Label(top, text="酷狗音乐榜单", font=("华文行楷", 15), fg="blue").grid(row=0, column=0, columnspan=2, pady=10)
        Label(top, text="歌曲", font=("华文行楷", 12), fg="blue").grid(row=1, column=0, stick=E)
        Label(top, text="歌手", font=("华文行楷", 12), fg="blue").grid(row=1, column=1, stick=W, padx=10)
        temp = 2
        for key in kugouTopDict:
            keyStr = StringVar()
            keyStr.set(key)
            valueStr = StringVar()
            valueStr.set(kugouTopDict[key])
            Label(top, textvariable=keyStr, font=("华文行楷", 12)).grid(row=temp, column=0, stick=E)
            Label(top, textvariable=valueStr, font=("华文行楷", 12)).grid(row=temp, column=1, stick=W, padx=10)
            temp += 1

