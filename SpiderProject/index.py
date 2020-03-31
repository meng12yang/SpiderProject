from tkinter import *
from MusicSearchPage import *
from MusicTopPage import *
from MovieInfoPage import *
from MovieTopPage import *
from NewsInfoPage import *
from tkinter.ttk import *

#首页
class Index(object):
    #初始化函数
    def __init__(self, master=None):
        self.root = master      #实例化首页根变量
        self.root.geometry("%dx%d" % (800, 450))      #设置首页长宽
        self.createPage()     #调用首页布局函数

    #页面主体布局
    def createPage(self):
               
        menubar = Menu(root)    #建立最上层菜单
        
        #建立菜单类别对象，命名为视频
        moviemenu = Menu(menubar)
        menubar.add_cascade(label="视频",menu=moviemenu)
        #在Movie菜单里建立菜单列表
        moviemenu.add_command(label="推荐视频",command=self.skipToMovieInfoPage)
        moviemenu.add_command(label="视频榜单",command=self.skipToMovieTop)
        root.config(menu=menubar)

        #建立菜单类别对象，命名为音乐
        musicmenu = Menu(menubar)
        menubar.add_cascade(label="音乐",menu=musicmenu)
        #在Music菜单里建立菜单列表
        musicmenu.add_command(label="音乐搜索",command=self.skipToMusicSearch)
        musicmenu.add_command(label="音乐榜单",command=self.skipToMusicTop)
        root.config(menu=menubar)

        #建立菜单类别对象，命名为新闻
        newsmenu = Menu(menubar)
        menubar.add_cascade(label="新闻",menu=newsmenu)
        #在news菜单里建立菜单列表
        newsmenu.add_command(label="热搜",command=self.skipToNewsInfo)
        root.config(menu=menubar)

        #插入背景图片
        self.sea_png = PhotoImage(file="tu0_seasky.png")
        lab1 = Label(root,image=self.sea_png)
        lab1.place(x=0,y=0)
        
        #插入标题
        myTitle = "“爬你所享”，让共享更轻松！"
        lab2 = Label(root,text=myTitle,font="方正姚体 22")
        lab2.place(x=215,y=50)

        #创建PanedWindow对象
        pw = PanedWindow(orient=HORIZONTAL)
        leftframe = LabelFrame(pw,text="视频",width=160,height=200)
        pw.add(leftframe,weight=1)
        myContent1 = """腾讯视频、爱奇艺、

哔哩哔哩和豆瓣电

影等各大视频网站

视频榜单和推荐视

频！"""
        lab3 = Label(root,text=myContent1,font="方正姚体 12")
        lab3.place(x=190,y=125)
        middleframe = LabelFrame(pw,text="音乐",width=160,height=200)
        pw.add(middleframe,weight=1)
        myContent2 = """QQ音乐、酷我音乐、

虾米音乐和酷狗音

乐等各大音乐网站

音乐榜单，更有音

乐搜索功能！"""
        lab4 = Label(root,text=myContent2,font="方正姚体 12")
        lab4.place(x=350,y=125)
        rightframe = LabelFrame(pw,text="新闻",width=160,height=200)
        pw.add(rightframe,weight=1)
        myContent3 = """新浪新闻、凤凰新

闻、澎湃新闻和南

方周末新闻等各新

闻网站的热点新闻！"""
        lab5 = Label(root,text=myContent3,font="方正姚体 12")
        lab5.place(x=515,y=125)
        pw.place(x=180,y=100)

        #插入小图标
        self.tx_png = PhotoImage(file="tu1_tx.png")
        lab5 = Label(root,image=self.tx_png)
        lab5.place(x=185,y=320)
        self.aqy_png = PhotoImage(file="tu2_aqy.png")
        lab6 = Label(root,image=self.aqy_png)
        lab6.place(x=218,y=320)
        self.bili_png = PhotoImage(file="tu3_bilibili.png")
        lab7 = Label(root,image=self.bili_png)
        lab7.place(x=251,y=320)
        self.db_png = PhotoImage(file="tu4_dbdy.png")
        lab8 = Label(root,image=self.db_png)
        lab8.place(x=284,y=320)

        self.qqyy_png = PhotoImage(file="tu5_qqyy.png")
        lab9 = Label(root,image=self.qqyy_png)
        lab9.place(x=317,y=320)
        self.kgyy_png = PhotoImage(file="tu6_kgyy.png")
        lab10 = Label(root,image=self.kgyy_png)
        lab10.place(x=350,y=320)
        self.xmyy_png = PhotoImage(file="tu7_xmyy.png")
        lab11 = Label(root,image=self.xmyy_png)
        lab11.place(x=383,y=320)
        self.kwyy_png = PhotoImage(file="tu8_kwyy.png")
        lab12 = Label(root,image=self.kwyy_png)
        lab12.place(x=416,y=320)

        self.xl_png = PhotoImage(file="tu9_xl.png")
        lab13 = Label(root,image=self.xl_png)
        lab13.place(x=449,y=320)
        self.pp_png = PhotoImage(file="tu10_pp.png")
        lab14 = Label(root,image=self.pp_png)
        lab14.place(x=482,y=320)
        self.fh_png = PhotoImage(file="tu11_fh.png")
        lab15 = Label(root,image=self.fh_png)
        lab15.place(x=515,y=320)
        self.nfzm_png = PhotoImage(file="tu12_nfzm.png")
        lab16 = Label(root,image=self.nfzm_png)
        lab16.place(x=548,y=320)
        self.bd_png = PhotoImage(file="tu13_bd.png")
        lab17 = Label(root,image=self.bd_png)
        lab17.place(x=581,y=320)
        self.hqw_png = PhotoImage(file="tu14_hqw.png")
        lab18 = Label(root,image=self.hqw_png)
        lab18.place(x=614,y=320)
        self.sh_png = PhotoImage(file="tu15_sh.png")
        lab19 = Label(root,image=self.sh_png)
        lab19.place(x=647,y=320)

        #插入地址
        myContent4 = """联系我们:

邮编：430000
地址：湖北省武汉市武昌区和平大道1178号"""
        lab20 = Label(root,text=myContent4,font="方正姚体 8")
        lab20.place(x=215,y=360)
        
        #插入微信二维码
        self.mywec1_png = PhotoImage(file="tu16_mywechat.png")
        lab21 = Label(root,image=self.mywec1_png)
        lab21.place(x=460,y=360)
        lab22 = Label(root,text="wwb19970525",font="Arial 5")
        lab22.place(x=465,y=417)
        self.mywec2_png = PhotoImage(file="tu17_mywechat.png")
        lab23 = Label(root,image=self.mywec2_png)
        lab23.place(x=550,y=360)
        lab24 = Label(root,text="myr1510707100",font="Arial 5")
        lab24.place(x=555,y=417)
        
    def skipToMovieInfoPage(self):
        MovieInfoPage(Toplevel())
    def skipToMovieTop(self):
        MovieTopPage(Toplevel())
    def skipToMusicSearch(self):
        MusicSearchPage(Toplevel())
    def skipToMusicTop(self):
        MusicTopPage(Toplevel())
    def skipToNewsInfo(self):
        NewsInfoPage(Toplevel())
        
#程序开始的起点
if __name__ == '__main__':
    root = Tk()
    root.title("'爬'你所享")

    Index(root)     #调用首页类，默认首先调用首页类__init__初始化函数
    root.mainloop()
