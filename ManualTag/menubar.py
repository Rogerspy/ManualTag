# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 14:21:29 2018

@author: Rogerspy
"""

import json
import jieba
from tkinter import *


class Menubar(object):
    def __init__(self, baseframe, toolmenu, root):
        self.root = root
        self.bf = baseframe
        self.tm = toolmenu
        self.char_or_word = 'word'
        self.ner_or_rela = 'rela'
        self.setup()
    
    def setup(self):
        pass
    
    def word_ner(self):
        self.char_or_word = 'word'
        self.ner_or_rela = 'ner'
        # get start position
        try:
            num = open('src/word_ner_config.json')
            nums = json.load(num)
            num.close()
            self.i, self.j, self.k = nums['i'], nums['j'], nums['k']
        except:
            self.i, self.j, self.k = 0, 0, 0
        # update t1 texts
        self.bf.t1.delete(1.0, END)
        self.bf.t1.insert(INSERT, ''.join(self.tm.items[self.k][:self.j]))
        self.bf.t1.insert(INSERT, self.tm.items[self.k][self.j], 'color')
        if self.j+1 < len(self.tm.items[self.k]):
            self.bf.t1.insert(INSERT, ''.join(self.tm.items[self.k][self.j+1:]))
            
        # insert t2
        cut = list(jieba.cut(self.tm.items[self.k][self.j]))[:-1]
        self.texts = [x for x in cut if x != ' ']
        self.bf.t2.delete(1.0, END)
        self.bf.t2.insert(INSERT, '\n')
        if self.i == 0:
            self.bf.t2.insert(INSERT, self.texts[0], 'color')
            self.bf.t2.insert(INSERT, '|' + '|'.join(self.texts[1:]))
        else:
            self.bf.t2.insert(INSERT, '|'.join(self.texts[:self.i])+'|')
            self.bf.t2.insert(INSERT, self.texts[self.i], 'color')
            if self.i+1 < len(self.texts):
                self.bf.t2.insert(END, '|'+'|'.join(self.texts[self.i+1:]))
    
    def char_ner(self):
        self.char_or_word = 'char'
        self.ner_or_rela = 'ner'
        # get start position
        try:
            num = open('src/char_ner_config.json')
            nums = json.load(num)
            num.close()
            self.i, self.j, self.k = nums['i'], nums['j'], nums['k']
        except:
            self.i, self.j, self.k = 0, 0, 0
        # update t1 texts
        self.bf.t1.delete(1.0, END)
        self.bf.t1.insert(INSERT, ''.join(self.tm.items[self.k][:self.j]))
        self.bf.t1.insert(INSERT, self.tm.items[self.k][self.j], 'color')
        if self.j+1 < len(self.tm.items[self.k]):
            self.bf.t1.insert(INSERT, ''.join(self.tm.items[self.k][self.j+1:]))
            
        # insert t2
        self.bf.t2.delete(1.0, END)
        cut = list(self.tm.items[self.k][self.j])[:-1]
        self.texts = [x for x in cut if x != ' ']
        self.bf.t2.delete(1.0, END)
        self.bf.t2.insert(INSERT, '\n')
        if self.i == 0:
            self.bf.t2.insert(INSERT, self.texts[0], 'color')
            self.bf.t2.insert(INSERT, '|' + '|'.join(self.texts[1:]))
        else:
            self.bf.t2.insert(INSERT, '|'.join(self.texts[:self.i])+'|')
            self.bf.t2.insert(INSERT, self.texts[self.i], 'color')
            if self.i+1 < len(self.texts):
                self.bg.t2.insert(END, '|'+'|'.join(self.texts[self.i+1:]))
        
    def word_rela(self):
        self.char_or_word = 'word'
        self.ner_or_rela = 'rela'
        # get start position
        try:
            num = open('src/word_rela_config.json')
            nums = json.load(num)
            num.close()
            self.i, self.j, self.k = nums['i'], nums['j'], nums['k']
        except:
            self.i, self.j, self.k = 0, 0, 0
        # update t1 texts
        self.bf.t1.delete(1.0, END)
        self.bf.t1.insert(INSERT, ''.join(self.tm.items[self.k][:self.j]))
        self.bf.t1.insert(INSERT, self.tm.items[self.k][self.j], 'color')
        if self.j+1 < len(self.tm.items[self.k]):
            self.bf.t1.insert(INSERT, ''.join(self.tm.items[self.k][self.j+1:]))
        
        # insert t2
        self.bf.t2.delete(1.0, END)
        cut = list(jieba.cut(self.tm.items[self.k][self.j]))[:-1]
        self.texts = [x for x in cut if x != ' ']
        self.bf.t2.delete(1.0, END)
        self.bf.t2.insert(INSERT, '\n')
        disp = [self.texts[n]+'/'+str(n) for n in range(len(self.texts))]
        self.bf.t2.insert(INSERT, ' '.join(disp))
            
        # build word to id dict
        self.word2id = {str(x):self.texts[x] for x in range(len(self.texts))}

        
    def char_rela(self):
        self.char_or_word = 'char'
        self.ner_or_rela = 'rela'
        # get start position
        try:
            num = open('src/word_rela_config.json')
            nums = json.load(num)
            num.close()
            self.i, self.j, self.k = nums['i'], nums['j'], nums['k']
        except:
            self.i, self.j, self.k = 0, 0, 0
        # update t1 texts
        self.bf.t1.delete(1.0, END)
        self.bf.t1.insert(INSERT, ''.join(self.tm.items[self.k][:self.j]))
        self.bf.t1.insert(INSERT, self.tm.items[self.k][self.j], 'color')
        if self.j+1 < len(self.tm.items[self.k]):
            self.bf.t1.insert(INSERT, ''.join(self.tm.items[self.k][self.j+1:]))
        
        # insert t2
        self.bf.t2.delete(1.0, END)
        cut = list(self.tm.items[self.k][self.j])[:-1]
        self.texts = [x for x in cut if x != ' ']
        self.bf.t2.delete(1.0, END)
        self.bf.t2.insert(INSERT, '\n')
        disp = [self.texts[n]+'/'+str(n) for n in range(len(self.texts))]
        self.bf.t2.insert(INSERT, ' '.join(disp))
        
        # build char to id dict
        self.word2id = {str(x):self.texts[x] for x in range(len(self.texts))}
    

    def addmenubar(self):
        #Create Menu
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        
        ## 文件
        filemenu = Menu(menubar)
        casmenue = Menu(filemenu)
        casmenue.add_command(label='打开待标记文件', command=self.tm.openfile1)
        casmenue.add_command(label='打开自定义词库', command=self.tm.openfile2)
        filemenu.add_cascade(label='打开', menu=casmenue)
        filemenu.add_command(label='保存', accelerator='Ctrl+S', command=self.tm.save2)
        self.bf.t5.bind('<Control-KeyPress-S>', self.tm.save2)
        filemenu.add_command(label='另存为', accelerator='Ctrl+Shift+S', command=self.tm.saveas2)
        self.bf.t5.bind('<Control-Shift-KeyPress-S>', self.tm.save2)
        menubar.add_cascade(label='文件', menu=filemenu)
        
        # 编辑
        editmenu = Menu(menubar)
        editmenu.add_command(label='撤销', accelerator='Ctrl+Z', command=self.tm.undo)
        self.bf.widget.bind('<Control-KeyPress-Z>', self.tm.undo)
        editmenu.add_command(label='恢复', accelerator='Ctrl+Y', command=self.tm.redo)
        self.bf.widget.bind('<Control-KeyPress-Y>', self.tm.redo)
        editmenu.add_separator()
        editmenu.add_command(label="剪切", accelerator = "Ctrl+X", command=self.tm.cut)
        self.bf.widget.bind('<Control-KeyPress-X>', self.tm.cut)
        editmenu.add_command(label="复制", accelerator = "Ctrl+C", command=self.tm.copy)
        self.bf.widget.bind('<Control-KeyPress-C>', self.tm.copy)
        editmenu.add_command(label="粘贴", accelerator = "Ctrl+V", command=self.tm.paste)
        self.bf.widget.bind('<Control-KeyPress-V>', self.tm.paste)
        editmenu.add_separator()
        editmenu.add_command(label="查找", accelerator = "Ctrl+F", command=self.tm.search)
        self.bf.widget.bind('<Control-KeyPress-F>', self.tm.search)
        editmenu.add_command(label="全选", accelerator = "Ctrl+A", command=self.tm.selectAll)
        self.bf.widget.bind('<Control-KeyPress-A>', self.tm.selectAll)
        menubar.add_cascade(label= "编辑", menu = editmenu)
        
        # 设置
        setmenu = Menu(menubar)
        casset = Menu(setmenu)
        casset.add_command(label='单词标记', command=self.word_ner)
        casset.add_command(label='字符标记', command=self.char_ner)
        setmenu.add_cascade(label='命名实体标记', menu=casset)
        casset = Menu(setmenu)
        casset.add_command(label='单词标记', command=self.word_rela)
        casset.add_command(label='字符标记', command=self.char_rela)
        setmenu.add_cascade(label='实体关系标记', menu=casset)
        menubar.add_cascade(label="设置", menu=setmenu)
        
        # 帮助
        helpmenu = Menu(menubar)
        helpmenu.add_command(label='开源地址', command=self.tm.opensr)
        helpmenu.add_command(label='帮助文档', command=self.tm.helpdoc)
        menubar.add_cascade(label="帮助", menu=helpmenu)
        
        # 关于
        aboutmenu = Menu(menubar)
        aboutmenu.add_command(label="作者", command=self.tm.author)
        aboutmenu.add_command(label="版权", command=self.tm.cprt)
        menubar.add_cascade(label="关于", menu=aboutmenu)
