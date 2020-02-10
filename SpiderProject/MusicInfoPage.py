from tkinter import *
import tkinter.messagebox as msgBox
from musicSpider import *
from MusicSearchPage import *

#音乐详情页
class MusicInfoPage(object):
    def __init__(self, master=None, keyword=None):
        self.root = master
        self.keyword = keyword    #音乐搜索关键词
        self.basicDict, self.commentDict = getMusicMessage_QQ(self.keyword)
        #设置歌曲基本信息
        self.text1 = StringVar()
        self.text2 = StringVar()
        self.text3 = StringVar()
        self.text4 = StringVar()
        self.text5 = StringVar()
        self.text6 = StringVar()
        self.text1.set(self.basicDict["singer"])
        self.text2.set(self.basicDict["album"])
        self.text3.set(self.basicDict["lan"])
        self.text4.set(self.basicDict["genre"])
        self.text5.set(self.basicDict["company"])
        self.text6.set(self.basicDict["pub_time"])
        #设置简介信息
        self.text7 = self.basicDict["intro"]
        #设置歌词信息
        self.text8 = self.basicDict["lyric"]

        self.root.geometry('%dx%d' % (800, 500))
        self.createPage()

    def createPage(self):
        #基本信息（歌手、专辑、语种、流派、唱片公司、发行时间）
        self.basicInfoPage = Frame(self.root)
        self.basicInfoPage.pack(pady=30)
        Label(self.basicInfoPage, text='歌手：', font=("华文行楷", 12)).grid(row=0, column=0, stick=E)
        Label(self.basicInfoPage, textvariable=self.text1, font=("华文行楷", 12)).grid(row=0, column=1, stick=W)
        Label(self.basicInfoPage, text='专辑：', font=("华文行楷", 12)).grid(row=0, column=2, stick=E)
        Label(self.basicInfoPage, textvariable=self.text2, font=("华文行楷", 12)).grid(row=0, column=3, stick=W)
        Label(self.basicInfoPage, text='语种：', font=("华文行楷", 12)).grid(row=1, column=0, stick=E)
        Label(self.basicInfoPage, textvariable=self.text3, font=("华文行楷", 12)).grid(row=1, column=1, stick=W)
        Label(self.basicInfoPage, text='流派：', font=("华文行楷", 12)).grid(row=1, column=2, stick=E)
        Label(self.basicInfoPage, textvariable=self.text4, font=("华文行楷", 12)).grid(row=1, column=3, stick=W)
        Label(self.basicInfoPage, text='唱片公司：', font=("华文行楷", 12)).grid(row=2, column=0, stick=E)
        Label(self.basicInfoPage, textvariable=self.text5, font=("华文行楷", 12)).grid(row=2, column=1, stick=W)
        Label(self.basicInfoPage, text='发行时间：', font=("华文行楷", 12)).grid(row=2, column=2, stick=E)
        Label(self.basicInfoPage, textvariable=self.text6, font=("华文行楷", 12)).grid(row=2, column=3, stick=W)

        #简介信息
        self.introInfoPage = Frame(self.root)
        self.introInfoPage.pack()
        scroll = Scrollbar()
        introText = Text(self.introInfoPage, height="7")
        scroll.pack(side=RIGHT, fill=Y)
        introText.pack()
        scroll.config(command=introText.yview)
        introText.config(yscrollcommand=scroll.set)
        introText.insert("end", self.text7)

        #歌词信息
        self.lyricInfoPage = Frame(self.root)
        self.lyricInfoPage.pack(pady=30)
        scroll2 = Scrollbar()
        lyricText = Text(self.lyricInfoPage, height="8")
        scroll2.pack(side=RIGHT, fill=Y)
        scroll2.config(command=lyricText.yview)
        lyricText.config(yscrollcommand=scroll2.set)
        lyricText.pack()
        lyricText.insert("end", self.text8)

        #评论信息
        self.commentInfoPage = Frame(self.root)
        self.commentInfoPage.pack()
        Button(self.commentInfoPage, text="QQ音乐评论", padx=5, pady=5, command=self.getComment_QQ).grid(row=0, column=0, padx=20)
        Button(self.commentInfoPage, text="酷我音乐评论", padx=5, pady=5, command=self.getComment_kuwo).grid(row=0, column=1)
        Button(self.commentInfoPage, text="虾米音乐评论", padx=5, pady=5, command=self.getComment_xiami).grid(row=0, column=2, padx=20)

    #获取QQ音乐评论
    def getComment_QQ(self):
        #设置QQ音乐评论信息
        text9 = StringVar()
        str = ""
        for key in self.commentDict:
            str = str+key+"：\n"+self.commentDict[key]+"\n\n"
        str = self.re_emojis(str)
        try:
            text9.set(str)
            top = Toplevel()
            top.title("QQ音乐评论")
            top.geometry("%dx%d" % (700, 800))
            Message(top, textvariable=text9, width=500).pack()
        except BaseException:
            msgBox.showinfo(title="错误", message="当前评论出错")

    #获取酷我音乐评论
    def getComment_kuwo(self):
        commentDict = getMusicMessage_kuwo(self.keyword)
        text10 = StringVar()
        str = ""
        for key in commentDict:
            str = str+key+"：\n"+commentDict[key]+"\n\n"
        str = self.re_emojis(str)
        try:
            text10.set(str)
            top = Toplevel()
            top.title("酷我音乐评论")
            top.geometry("%dx%d" % (700, 800))
            Message(top, textvariable=text10, width=500).pack()
        except BaseException:
            msgBox.showinfo(title="错误", message="当前评论出错")

    #获取虾米音乐评论
    def getComment_xiami(self):
        commentDict = getMusicMessage_xiami(self.keyword)
        text11 = StringVar()
        str = ""
        for key in commentDict:
            str = str + key + "：\n" + commentDict[key] + "\n\n"
        str = self.re_emojis(str)
        try:
            text11.set(str)
            top = Toplevel()
            top.title("虾米音乐评论")
            top.geometry("%dx%d" % (700, 800))
            Message(top, textvariable=text11, width=500).pack()
        except BaseException:
            msgBox.showinfo(title="错误", message="当前评论出错")

    #删除字符串中的表情
    def re_emojis(self, text):
        emoji_pattern = re.compile("["
                                   u"\U0001F600-\U0001F64F"
                                   u"\U0001F300-\U0001F5FF"
                                   u"\U0001F680-\U0001F6FF"
                                   u"\U0001F1E0-\U0001F1FF"
                                   "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r' ', text)
