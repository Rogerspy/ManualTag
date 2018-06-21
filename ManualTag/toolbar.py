# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 22:32:27 2018

@author: Rogers
"""


from tkinter import *
from .Baseframe import BaseFrame
from .utils import ToolMenu


class Toolbar(object):
    def __init__(self, baseframe, toolmenu):
        self.bf = baseframe
        self.tm = toolmenu
#        self.tm.filename1 = None
#        self.tm.filename2 = None
        self.filename1 = self.tm.filename1
        self.filename2 = self.tm.filename2
        
    def setup(self):
        pass
    
    def addtoolbar(self):
        ## frame1 add button
        b1 = Button(self.bf.frame1, text='打开', command=self.tm.openfile1)
        b1.config(font=('黑体',12))
        b1.place(relx=0.01, rely=0.02,  relwidth=0.12, relheight=0.04)
        b2 = Button(self.bf.frame1, text='保存', command=self.tm.save1)
        b2.config(font=('黑体',12))
        b2.place(relx=0.2, rely=0.02, relwidth=0.12, relheight=0.04)
        ## frame5 add button
        b5 = Button(self.bf.frame5,text = '打开',command = self.tm.openfile2)
        b5.config(font=('黑体', 12))
        b5.place(relx=0.01, rely=0.,  relwidth=0.12, relheight=0.1)
        b5 = Button(self.bf.frame5, text = '保存', command = self.tm.save2)
        b5.config(font=('黑体', 12))
        b5.place(relx=0.2, rely=0., relwidth=0.12, relheight=0.1)
        

if __name__ == '__main__':
    root = Tk()
    root.update()
    root.title('Data Tag')
    root.geometry('1920x1080')
    root.update()
    bf = BaseFrame(root)
    tm = ToolMenu(bf)
    t = Toolbar(bf, tm)
    t.addtoolbar()
    mainloop()