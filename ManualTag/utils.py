# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 23:23:25 2018

@author: Rogerspy
"""

import jieba
from tkinter.filedialog import *
from tkinter.messagebox import *


class ToolMenu(object):
    def __init__(self, baseframe, root):
        self.root = root
        self.bf = baseframe
        self.filename1 = ''
        self.filename2 = ''
        self.setup()
        
    def setup(self):
        pass
    
    def openfile1(self):
        self.filename1 = askopenfilename(defaultextension='.txt')
        if self.filename1 == '':
            self.filename1 = None
        else:
            self.bf.t1.delete(1.0, END)
            f = open(self.filename1, encoding='utf8')
            lines = f.readlines()
            b = 0
            self.items, pos = [], []
            for line in lines:
                if '===========' not in line and len(line.strip()) > 0:
                    pos.append(line)
                    b += 1
                else:
                    b = 0
                    self.items.append(pos)
                    pos = []
            # insert t1
            self.bf.t1.insert(INSERT, ''.join(self.items[0]))
            f.close()
    
    def openfile2(self):
        self.filename2 = askopenfilename(defaultextension='.txt')
        if self.filename2 == '':
            self.filename2 = None
        else:
            self.bf.t5.delete(1.0, END)
            f = open(self.filename2, encoding='utf8')
            self.bf.t5.insert(END, f.read())
            f.close()
    
    def saveas1(self):
        f = asksaveasfilename(initialfile='未命名.txt', defaultextension='.txt')
        self.filename1 = f
        fh = open(f, 'w+', encoding='utf8')
        msg = self.bf.t1.get(1.0, END)
        fh.write(msg)
        fh.close()
    
    def saveas2(self):
        f = asksaveasfilename(initialfile='未命名.txt', defaultextension='.txt')
        self.filename2 = f
        fh = open(f, 'w+', encoding='utf8')
        msg = self.t5.get(1.0, END)
        fh.write(msg)
        fh.close()
    
    def save1(self):
        try:
            f = open(self.filename1, 'w+', encoding='utf8')
            msg = self.bf.t1.get(1.0, END)
            f.write(msg)
            f.close()
        except:
            self.saveas()
    
    def save2(self):
        try:
            f = open(self.filename2, 'w+', encoding='utf8')
            msg = self.bf.t5.get(1.0, END)
            f.write(msg)
            f.close()
            jieba.load_userdict(self.filename2)
        except:
            self.saveas1()
            
    def undo(self):
        self.bf.widget.edit_undo()
    
    def redo(self):
        self.bf.widget.edit_redo()
    
    def selectAll(self):
        self.bf.widget.tag_add('sel', '1.0', END)  
            
    def cut(self):
        self.bf.widget.event_generate('<<Cut>>')

    def copy(self):
        self.bf.widget.event_generate('<<Copy>>')

    def paste(self):
        self.bf.widget.event_generate('<<Paste>>')
        
    def author(self):
        showinfo('作者(Author)','作者: Rogerspy')
    
    def cprt(self):
        showinfo('版权(Copyright)','版权归属: Rogerspy')  
        
    def helpdoc(self):
        showinfo('文档：', '帮助文档功能还在开发中')
        
    def opensr(self):
        showinfo('开源地址: ', 'https://github.com/Rogerspy/ManualTag')
        
    def search(self):
        def dosearch():
            myentry = entry1.get()
            whatever = str(self.bf.widget.get(1.0, END))
            tot_num = whatever.count(myentry)
            showinfo("查找结果：","一共找到了%s个%s." %(tot_num, repr(myentry)))
        topsearch = Toplevel(self.root)
        topsearch.geometry('300x35+200+250')
        label1 = Label(topsearch,text='Find')
        label1.grid(row=0, column=0, padx=5)
        entry1 = Entry(topsearch, width=28)
        entry1.grid(row=0, column=1, padx=5)
        button1 = Button(topsearch, text='查找', command=dosearch)
        button1.grid(row=0, column=2)
    
            
if __name__ == '__main__':
    tm = ToolMenu(root)
    print(dir(tm))
    
