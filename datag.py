# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 12:35:18 2018

@author: Rogerspy
"""


import jieba
import json
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *


jieba.load_userdict('src/wordsSet.txt')


class DataTag(object):
    """
    Manual text annotation tool.
    """
    def __init__(self, tags=None, ner='', relation='', bio=''):
        self.tags = tags
        self.word = ''
        self.ner = ner
        self.relation = relation
        self.bio = bio
        self.setup()
    
    def setup(self):
        # get start position
        try:
            num = open('src/config.json')
            nums = json.load(num)
            num.close()
            self.i, self.j, self.k = nums['i'], nums['j'], nums['k']
        except:
            self.i, self.j, self.k = 0, 0, 0
            
        # get tags if tags in a file
        if isinstance(self.tags, str):
            f = open(self.tags, encoding='utf8').readlines()
            lines = f.readlines()
            f.close()
            self.tags = {item[0]: item[1] for item in lines}
            
    def cut(self):
        self.widget.event_generate('<<Cut>>')

    def copy(self):
        self.widget.event_generate('<<Copy>>')

    def paste(self):
        self.widget.event_generate('<<Paste>>')

    def openfile1(self):
        self.filename1 = askopenfilename(defaultextension='.txt')
        if self.filename1 == '':
            self.filename1 = None
        else:
            self.t1.delete(1.0, END)
            f = open(self.filename1, encoding='utf8')
            lines = f.readlines()
            b = 0
            self.items, pos = [], []
            for line in lines:
                if '===========' not in line:
                    pos.append(line)
                    b += 1
                else:
                    b = 0
                    self.items.append(pos)
                    pos = []
            self.t1.insert(INSERT, ''.join(self.items[self.k][:self.j]))
            self.t1.insert(INSERT, self.items[self.k][self.j], 'color')
            if self.j+1 < len(self.items[self.k]):
                self.t1.insert(INSERT, ''.join(self.items[self.k][self.j+1:]))
            cut = list(jieba.cut(self.items[self.k][self.j]))[:-1]
            self.texts = [x for x in cut if x != ' ']
            self.t2.insert(INSERT, '\n')
            self.t2.insert(INSERT, '|'.join(self.texts[:self.i])+'|')
            self.t2.insert(INSERT, self.texts[self.i], 'color')
            if self.i+1 < len(self.texts):
                self.t2.insert(END, '|'+'|'.join(self.texts[self.i+1:]))
            f.close()
    
    def openfile2(self):
        self.filename2 = askopenfilename(defaultextension='.txt')
        if self.filename2 == '':
            self.filename2 = None
        else:
            self.t5.delete(1.0, END)
            f = open(self.filename2, encoding='utf8')
            self.t5.insert(END, f.read())
            f.close()
    
    def saveas1(self):
        f = asksaveasfilename(initialfile='未命名.txt', defaultextension='.txt')
        self.filename1 = f
        fh = open(f, 'w+', encoding='utf8')
        msg = self.t1.get(1.0, END)
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
            msg = self.t1.get(1.0, END)
            f.write(msg)
            f.close()
        except:
            self.saveas()
    
    def save2(self):
        try:
            f = open(self.filename2, 'w+', encoding='utf8')
            msg = self.t5.get(1.0, END)
            f.write(msg)
            f.close()
            jieba.load_userdict(self.filename2)
        except:
            self.saveas1()
    
    def modify(self, event):
        self.texts = [x.strip() for x in self.t2.get('2.0', END).split('|')]
    
    def inputchar(self, event):
        if len(repr(event.char)) != 2:
            self.word += event.char
    
    def delete(self, event):
        self.word = self.word[:-1]
    
    def nexterm(self, event):
        if len(repr(event.char)) != 2:
            content = self.texts[self.i]+' -----> '+self.tags[self.word]
            self.t4.insert(INSERT, content+'\n')
            self.t4.see(END)
            self.t4.update()
            p = str(int(self.t4.index(INSERT).split('.')[0])-1)+'.0'
            taged = open('tagdata/taged_position.txt', 'a+', encoding='utf8')
            taged.write(self.t4.get(p, END)[:-1])
            if self.i+1 < len(self.texts):
                self.t2.delete('1.0', END)
                self.t2.insert(INSERT, '\n')
                self.t2.insert(INSERT, '|'.join(self.texts[:self.i+1])+'|')
                self.t2.insert(END, self.texts[self.i+1], 'color')
                self.t2.insert(END, '|'+'|'.join(self.texts[self.i+2:]))
            elif self.i+1 >= len(self.texts):
                if self.j+1 < len(self.items[self.k]):
                    self.t1.delete('1.0', END)
                    self.t1.insert(INSERT, ''.join(self.items[self.k][:self.j+1]))
                    self.t1.insert(INSERT, self.items[self.k][self.j+1], 'color')
                    self.t1.insert(INSERT, ''.join(self.items[self.k][self.j+2:]))
                    cut = list(jieba.cut(self.items[self.k][self.j+1]))[:-1]
                    red_word = [x for x in cut if x != ' ']
                    self.t2.delete('1.0', END)
                    self.t2.insert(INSERT, '\n')
                    self.t2.insert(END, red_word[0], 'color')
                    self.t2.insert(END, '|'+'|'.join(red_word[1:]))
                elif self.j+1 >= len(self.items[self.k]):
                    if self.k+1 < len(self.items):
                        self.t1.delete('1.0', END)
                        self.t1.insert(INSERT, self.items[self.k+1][0], 'color')
                        self.t1.insert(INSERT, self.items[self.k+1][1:])
                        cut = list(jieba.cut(self.items[self.k+1][0]))[:-1]
                        red_word = [x for x in cut if x != ' ']
                        self.t2.delete('1.0', END)
                        self.t2.insert(INSERT, '\n')
                        self.t2.insert(END, red_word[0], 'color')
                        self.t2.insert(END, '|'+'|'.join(red_word[1:]))
            self.i += 1
            if self.i >= len(self.texts):
                self.j += 1
                if self.j < len(self.items[self.k]):
                    cut = list(jieba.cut(self.items[self.k][self.j]))[:-1]
                    self.texts = [x for x in cut if x != ' ']
                    self.i = 0
                    taged.write('[EOS]\n')
                elif self.j >= len(self.items[self.k]):
                    self.k += 1
                    if self.k < len(self.items):
                        cut = list(jieba.cut(self.items[self.k][0]))[:-1]
                        self.texts = [x for x in cut if x != ' ']
                        self.t1.delete('1.0', END)
                        self.t1.insert(END, ''.join(self.items[self.k]))
                        self.j = 0
                        self.i = 0
                        taged.write('[EOS]\n')
            confile = open('src/config.json', 'w+', encoding='utf8')
            conjson = {'i': self.i, 'j': self.j, 'k': self.k}
            jdump = json.dumps(conjson, ensure_ascii=False)
            confile.write(jdump)
            confile.close()
            taged.close()
        self.word = ''
    
    def load_dict(self, event):
        jieba.load_userdict('src/wordsSet.txt')
        
    def popupmenu(self, event):
        self.menu.post(event.x_root, event.y_root)
        self.widget = event.widget
    
    def datag(self, root):
        
        
        self.widget = root
        self.menu = Menu(self.widget, tearoff=0)
        self.menu.add_command(label="剪切", command=self.cut)
        self.menu.add_command(label="复制", command=self.copy)
        self.menu.add_command(label="粘贴", command=self.paste)
        self.widget.bind("<Button-3>", self.popupmenu)
        
        # frame 1
        frame1 = Frame(root, bg='SkyBlue')
        frame1.place(relx=0.01, rely=0.01, relwidth=0.33, relheight=0.96)
        ## add display window
        self.t1 = Text(frame1, font=('TimeNews', 14), spacing1=5, wrap=NONE)
        self.t1.tag_config('color', foreground='red', background='yellow')
        self.t1.place(relx=0.01, rely=0.07, relwidth=0.98, relheight=0.52)
        ## add button
        b1 = Button(frame1, text = '打开', command = self.openfile1)
        b1.config(font=('黑体',12))
        b1.place(relx=0.01, rely=0.02,  relwidth=0.12, relheight=0.04)
        b2 = Button(frame1, text = '保存', command = self.save1)
        b2.config(font=('黑体',12))
        b2.place(relx=0.2, rely=0.02, relwidth=0.12, relheight=0.04)
        ## add scroll bar
        s1 = Scrollbar(self.t1, orient = 'horizontal', 
                       cursor='hand2', command=self.t1.xview) 
        s2 = Scrollbar(self.t1, orient = 'vertical',
                       cursor='hand2', command=self.t1.yview) 
        self.t1['xscrollcommand'] = s1.set
        self.t1['yscrollcommand'] = s2.set
        s1.pack(side='bottom', fill='x')
        s2.pack(side='right', fill='y')
        
        # frame 2
        frame2 = Frame(root, bg='#FFA54F')
        frame2.place(relx=0.35, rely=0.01, relwidth=0.33, relheight=0.4)
        ## add prompt message
        prompt = Text(frame2, bg='#FFA54F', font=('TimeNews', 14), spacing3=4.0)
        prompt.insert(INSERT, '\n'+self.ner)
        prompt.configure(state="disabled")
        prompt.place(relx=0, rely=0, relwidth=0.5, relheight=0.6)
        prompt = Text(frame2, bg='#FFA54F', font=('TimeNews', 14), spacing3=4.0)
        prompt.insert(INSERT, '\n'+self.relation)
        prompt.configure(state="disabled")
        prompt.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.6)
        prompt = Text(frame2, bg='#FFA54F', font=('TimeNews', 14))
        prompt.insert(INSERT, self.bio)
        prompt.configure(state="disabled")
        prompt.place(relx=0, rely=0.6, relwidth=1, relheight=0.4)
             
        # frame 3
        frame3 = Frame(root, bg='SkyBlue')
        frame3.place(relx=0.35, rely=0.42, relwidth=0.33, relheight=0.55)
        ## add segmented sentence display window
        self.t2 = Text(frame3, font=('宋体',14), wrap=WORD)
        self.t2.tag_config('color', foreground='red', background='yellow')
        self.t2.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.3)
        ## add input window
        self.t3 = Text(frame3, font=('宋体',14), wrap=NONE)
        self.t3.place(relx=0.01, rely=0.325, relwidth=0.98, relheight=0.66)
        ### t3 bind envent
        self.t3.bind('<Key>', self.inputchar)
        self.t3.bind('<Key-BackSpace>', self.delete)
        self.t3.bind('<Return>', self.nexterm)
        self.t3.bind('<ButtonRelease-1>', self.modify)
        self.t3.focus_set()
        
        # frame 4
        frame4 = Frame(root, bg='SkyBlue')
        frame4.place(relx=0.69, rely=0.01, relwidth=0.3, relheight=0.96)
        # add preview window
        self.t4 = Text(frame4, font=('宋体',14))
        s4 = Scrollbar(self.t4, orient = 'vertical', 
                       cursor='hand2', command=self.t4.yview) 
        self.t4['yscrollcommand'] = s4.set
        s4.pack(side='right', fill='y')
        self.t4.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)  
        
        # frame 5
        frame5 = Frame(root, bg='SkyBlue')
        frame5.place(relx=0.01, rely=0.6, relwidth=0.33, relheight=0.365)
        ## add jieba user dict display
        self.t5 = Text(frame5, font=('宋体', 14))
        self.t5.place(relx=0.01, rely=0.12, relwidth=0.98, relheight=0.87)
        ## add button
        b5 = Button(frame5,text = '打开',command = self.openfile2)
        b5.config(font=('黑体', 12))
        b5.place(relx=0.01, rely=0.,  relwidth=0.12, relheight=0.1)
        b5 = Button(frame5, text = '保存', command = self.save2)
        b5.config(font=('黑体', 12))
        b5.place(relx=0.2, rely=0., relwidth=0.12, relheight=0.1)
        ## add scroll bar
        s5 = Scrollbar(self.t5, orient = 'vertical',
                       cursor='hand2', command=self.t5.yview) 
        self.t5['yscrollcommand'] = s5.set
        s5.pack(side='right', fill=Y)
        
        
if __name__ == '__main__':
    tag = {'00': 'S-PER', 
           '01': 'S-ORG', 
           '02': 'S-LOC', 
           '10': 'B-PER',
           '11': 'B-ORG',
           '12': 'B-LOC', 
           '20': 'I-PER', 
           '21': 'I-ORG', 
           '22': 'I-LOC',
           '30': 'O'}
    ner = '''
    实体类别： \n
    0.  PER  - 人物
    1.  ORG  - 组织
    2.  LOC  - 地点'''
    relation = '''
    关系类别：\n
    0.  FAM  - 家庭关系
    1.  JOB  - 工作关系
    2.  FRI  - 朋友关系'''
    bio = '''
    BIO规则：
    0.  S - single    1.  B - begin
    2.  I - inside    3.  O - outside\n
    例子：
     小明  是   山西  人 。
    S-PER   O  S-LOC   O O'''
    # build window
    root = Tk()
    root.update()
    root.title('Data Tag')
    root.geometry('1920x1080')
    root.update()
    DataTag(tag, ner, relation, bio).datag(root)
    mainloop()
