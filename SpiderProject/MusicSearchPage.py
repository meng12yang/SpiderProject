from tkinter import *
from tkinter.messagebox import *
from MusicInfoPage import *

#音乐搜索页
class MusicSearchPage(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('%dx%d' % (500, 300))
        self.keyword = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)
        self.page.pack()
        label = Label(self.page, text="音乐搜索", font=("华文行楷", 20), fg="blue")

        label.grid(row=0, column=0, columnspan=2, pady=50)
        label.focus()
        Entry(self.page, textvariable=self.keyword, bd=4, width=35).grid(row=1, column=0)
        Button(self.page, text="搜索", padx=5, pady=5, command=self.searchMusic).grid(row=1, column=1, padx=30)

    #搜索音乐
    def searchMusic(self):
        inputword = self.keyword.get()
        if inputword=='':
            showinfo(title='错误', message='您未输入任何搜索信息!')
        else:
            self.page.destroy()
            MusicInfoPage(self.root, inputword)     #跳转到音乐详情页并传输搜索关键词
