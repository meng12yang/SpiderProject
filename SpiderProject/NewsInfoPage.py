from tkinter import *
from newsSpider import *
import webbrowser

#新闻详情页
class NewsInfoPage(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry("%dx%d" % (1600, 600))

        #获取爬虫内容
        self.sinaDict = getNewsMessage_sina()
        self.ifengDict = getNewsMessage_ifeng()
        self.pengpaiDict = getNewsMessage_pengpai()

        self.createPage()

    def createPage(self):
        self.sinaPage = Frame(self.root)
        self.sinaPage.grid(row=0, column=0, stick=N)
        self.ifengPage = Frame(self.root)
        self.ifengPage.grid(row=0, column=1, stick=N, padx=20)
        self.pengpaiPage = Frame(self.root)
        self.pengpaiPage.grid(row=0, column=2, stick=N)
        self.extraPage = Frame(self.root)
        self.extraPage.grid(row=0, column=3, padx=80)

        #标题
        Label(self.sinaPage, text="新浪新闻", font=("华文行楷", 15), fg="blue").pack(pady=20)
        Label(self.ifengPage, text="凤凰网新闻", font=("华文行楷", 15), fg="blue").pack(pady=20)
        Label(self.pengpaiPage, text="澎湃新闻", font=("华文行楷", 15), fg="blue").pack(pady=20)
        sohuLabel = Label(self.extraPage, text="获取搜狐新闻要闻", font=("华文行楷", 15), fg="blue", cursor="cross")
        sohuLabel.pack(pady=20)
        huanqiuLabel = Label(self.extraPage, text="获取环球网新闻要闻", font=("华文行楷", 15), fg="blue", cursor="cross")
        huanqiuLabel.pack()
        infzmLabel = Label(self.extraPage, text="获取南方周末新闻要闻", font=("华文行楷", 15), fg="blue", cursor="cross")
        infzmLabel.pack(pady=20)
        baiduLabel = Label(self.extraPage, text="获取百度新闻要闻", font=("华文行楷", 15), fg="blue", cursor="cross")
        baiduLabel.pack()

        #内容
        #新浪新闻
        keys1 = list(self.sinaDict.keys())
        values1 = list(self.sinaDict.values())
        keyStr = StringVar()
        keyStr.set(keys1[0])
        Button(self.sinaPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
                command=lambda :self.open_url(values1[0])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys1[1])
        Button(self.sinaPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values1[1])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys1[2])
        Button(self.sinaPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values1[2])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys1[3])
        Button(self.sinaPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values1[3])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys1[4])
        Button(self.sinaPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values1[4])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys1[5])
        Button(self.sinaPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values1[5])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys1[6])
        Button(self.sinaPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values1[6])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys1[7])
        Button(self.sinaPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values1[7])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys1[8])
        Button(self.sinaPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values1[8])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys1[9])
        Button(self.sinaPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values1[9])).pack(pady=6)
        #凤凰网新闻
        keys2 = list(self.ifengDict.keys())
        values2 = list(self.ifengDict.values())
        keyStr = StringVar()
        keyStr.set(keys2[0])
        Button(self.ifengPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
                command=lambda :self.open_url(values2[0])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys2[1])
        Button(self.ifengPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values2[1])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys2[2])
        Button(self.ifengPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values2[2])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys2[3])
        Button(self.ifengPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values2[3])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys2[4])
        Button(self.ifengPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values2[4])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys2[5])
        Button(self.ifengPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values2[5])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys2[6])
        Button(self.ifengPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values2[6])).pack(pady=6)
        #澎湃新闻
        keys = list(self.pengpaiDict.keys())
        values = list(self.pengpaiDict.values())
        keyStr = StringVar()
        keyStr.set(keys[0])
        Button(self.pengpaiPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[0])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[1])
        Button(self.pengpaiPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[1])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[2])
        Button(self.pengpaiPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[2])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[3])
        Button(self.pengpaiPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[3])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[4])
        Button(self.pengpaiPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[4])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[5])
        Button(self.pengpaiPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[5])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[6])
        Button(self.pengpaiPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[6])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[7])
        Button(self.pengpaiPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[7])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[8])
        Button(self.pengpaiPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[8])).pack(pady=6)
        keyStr = StringVar()
        keyStr.set(keys[9])
        Button(self.pengpaiPage, textvariable=keyStr, font=("华文行楷", 12), activebackground="red",
               command=lambda: self.open_url(values[9])).pack(pady=6)

        #搜狐、环球网、南方周末、百度新闻标签绑定点击事件
        sohuLabel.bind("<Button-1>", self.getNews_sohu)
        huanqiuLabel.bind("<Button-1>", self.getNews_huanqiu)
        infzmLabel.bind("<Button-1>", self.getNews_infzm)
        baiduLabel.bind("<Button-1>", self.getNews_baidu)


    # 打开url
    def open_url(self, url):
        webbrowser.open(url, new=0)

    #获取搜狐新闻要闻
    def getNews_sohu(self, event):
        sohuDict = getNewsMessage_sohu()
        top = Toplevel()
        top.title("搜狐新闻要闻")
        top.geometry("%dx%d" % (700, 600))

        Label(top, text="搜狐新闻", font=("华文行楷", 15), fg="blue").pack(pady=20)
        keys = list(sohuDict.keys())
        values = list(sohuDict.values())
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

    #获取环球网新闻要闻
    def getNews_huanqiu(self, event):
        huanqiuDict = getNewsMessage_huanqiu()
        top = Toplevel()
        top.title("环球网新闻要闻")
        top.geometry("%dx%d" % (700, 600))

        Label(top, text="环球网新闻", font=("华文行楷", 15), fg="blue").pack(pady=20)
        keys = list(huanqiuDict.keys())
        values = list(huanqiuDict.values())
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

    #获取南方周末新闻要闻
    def getNews_infzm(self, event):
        infzmDict = getNewsMessage_infzm()
        top = Toplevel()
        top.title("南方周末新闻要闻")
        top.geometry("%dx%d" % (700, 600))

        Label(top, text="南方周末新闻", font=("华文行楷", 15), fg="blue").pack(pady=20)
        keys = list(infzmDict.keys())
        values = list(infzmDict.values())
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

    #获取百度新闻要闻
    def getNews_baidu(self, event):
        baiduDict = getNewsMessage_baidu()
        top = Toplevel()
        top.title("百度新闻要闻")
        top.geometry("%dx%d" % (700, 600))

        Label(top, text="百度新闻", font=("华文行楷", 15), fg="blue").pack(pady=20)
        keys = list(baiduDict.keys())
        values = list(baiduDict.values())
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