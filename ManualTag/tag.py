# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 18:59:26 2018

@author: Rogerspy
"""

import json
import jieba
from tkinter import *


class Tag(object):
    def __init__(self, baseframe, toolmenu, menubar, tags=None, rela_tag=None):
        self.bf = baseframe
        self.tm = toolmenu
        self.mn = menubar
        self.word = ''
        self.tags = tags
        self.rela_tag = rela_tag
    
    def setup(self):
        pass
    
    def inputchar(self, event):
        if len(repr(event.char)) != 2:
            self.word += event.char
    
    def delete(self, event):
        self.word = self.word[:-1]
    
    def ner(self, event):
        if len(repr(event.char)) != 2:
            # preview taged data
            content = self.mn.texts[self.mn.i]+' -----> '+self.tags[self.word]
            self.bf.t4.insert(INSERT, content+'\n')
            self.bf.t4.see(END)
            self.bf.t4.update()
            # wirte to file
            p = str(int(self.bf.t4.index(INSERT).split('.')[0])-1)+'.0'
            taged = open('tagdata/taged_position.txt', 'a+', encoding='utf8')
            taged.write(self.bf.t4.get(p, END)[:-1])
            # highlight tagging word or char
            if self.mn.i+1 < len(self.mn.texts):
                self.bf.t2.delete('1.0', END)
                self.bf.t2.insert(INSERT, '\n')
                self.bf.t2.insert(INSERT, '|'.join(self.mn.texts[:self.mn.i+1])+'|')
                self.bf.t2.insert(END, self.mn.texts[self.mn.i+1], 'color')
                self.bf.t2.insert(END, '|'+'|'.join(self.mn.texts[self.mn.i+2:]))
            elif self.mn.i+1 >= len(self.mn.texts):
                if self.mn.j+1 < len(self.tm.items[self.mn.k]):
                    self.bf.t1.delete('1.0', END)
                    self.bf.t1.insert(INSERT, ''.join(self.tm.items[self.mn.k][:self.mn.j+1]))
                    self.bf.t1.insert(INSERT, self.tm.items[self.mn.k][self.mn.j+1], 'color')
                    self.bf.t1.insert(INSERT, ''.join(self.tm.items[self.mn.k][self.mn.j+2:]))
                    if self.mn.char_or_word == 'word':
                        cut = list(jieba.cut(self.tm.items[self.mn.k][self.mn.j+1]))[:-1]
                    elif self.mn.char_or_word == 'char':
                        cut = list(self.tm.items[self.mn.k][self.mn.j+1])[:-1]
                    red_word = [x for x in cut if x != ' ']
                    self.bf.t2.delete('1.0', END)
                    self.bf.t2.insert(INSERT, '\n')
                    self.bf.t2.insert(END, red_word[0], 'color')
                    self.bf.t2.insert(END, '|'+'|'.join(red_word[1:]))
                elif self.mn.j+1 >= len(self.tm.items[self.mn.k]):
                    if self.mn.k+1 < len(self.tm.items):
                        self.bf.t1.delete('1.0', END)
                        self.bf.t1.insert(INSERT, self.tm.items[self.mn.k+1][0], 'color')
                        self.bf.t1.insert(INSERT, ''.join(self.tm.items[self.mn.k+1][1:]))
                        if self.mn.char_or_word == 'word':
                            cut = list(jieba.cut(self.tm.items[self.mn.k+1][0]))[:-1]
                        elif self.mn.char_or_word == 'char':
                            cut = list(self.tm.items[self.mn.k+1][0])[:-1]
                        red_word = [x for x in cut if x != ' ']
                        self.bf.t2.delete('1.0', END)
                        self.bf.t2.insert(INSERT, '\n')
                        self.bf.t2.insert(END, red_word[0], 'color')
                        self.bf.t2.insert(END, '|'+'|'.join(red_word[1:]))
            self.mn.i += 1
            # skip the tag pointer to the next
            if self.mn.i >= len(self.mn.texts):
                self.mn.j += 1
                if self.mn.j < len(self.tm.items[self.mn.k]):
                    if self.mn.char_or_word == 'word':
                        cut = list(jieba.cut(self.tm.items[self.mn.k][self.mn.j]))[:-1]
                    elif self.mn.char_or_word == 'char':
                        cut = list(self.tm.items[self.mn.k][self.mn.j])[:-1]
                    self.mn.texts = [x for x in cut if x != ' ']
                    self.mn.i = 0
                    taged.write('[EOS]\n')
                elif self.mn.j >= len(self.tm.items[self.mn.k]):
                    self.mn.k += 1
                    if self.mn.k < len(self.tm.items):
                        if self.mn.char_or_word == 'word':
                            cut = list(jieba.cut(self.tm.items[self.mn.k][0]))[:-1]
                        elif self.mn.char_or_word == 'char':
                            cut = list(self.tm.items[self.mn.k][0])[:-1]
                        self.mn.texts = [x for x in cut if x != ' ']
                        self.mn.j = 0
                        self.mn.i = 0
                        taged.write('[EOS]\n')
            # save the position of tagging word or char
            if self.mn.char_or_word == 'word' and self.mn.ner_or_rela == 'ner':
                confile = open('src/word_ner_config.json', 'w+', encoding='utf8')
            elif self.mn.char_or_word == 'word' and self.mn.ner_or_rela == 'rela':
                confile = open('src/word_rela_config.json', 'w+', encoding='utf8')
            elif self.mn.char_or_word == 'char' and self.mn.ner_or_rela == 'ner':
                confile = open('src/char_ner_config.json', 'w+', encoding='utf8')
            elif self.mn.char_or_word == 'char' and self.mn.ner_or_rela == 'rela':
                confile = open('src/char_rela_config.json', 'w+', encoding='utf8')
            conjson = {'i': self.mn.i, 'j': self.mn.j, 'k': self.mn.k}
            jdump = json.dumps(conjson, ensure_ascii=False)
            confile.write(jdump)
            confile.close()
            taged.close()
        self.word = ''

    def relation(self, event):
        pre_text = self.mn.texts.copy()
        if self.word == '':
            self.bf.t4.insert(INSERT, ' '.join(self.mn.texts)+'\n')
            self.bf.t4.see(END)
            self.bf.t4.update()
            self.mn.j += 1
            if self.mn.j < len(self.tm.items[self.mn.k]):
                # update t1 text
                self.bf.t1.delete(1.0, END)
                self.bf.t1.insert(INSERT, ''.join(self.tm.items[self.mn.k][:self.mn.j]))
                self.bf.t1.insert(INSERT, self.tm.items[self.mn.k][self.mn.j], 'color')
                self.bf.t1.insert(INSERT, ''.join(self.tm.items[self.mn.k][self.mn.j+1:]))
                self.bf.t2.delete(1.0, END)
                if self.mn.char_or_word == 'word':
                    cut = list(jieba.cut(self.tm.items[self.mn.k][self.mn.j]))[:-1]
                elif self.mn.char_or_word == 'char':
                    cut = list(self.tm.items[self.mn.k][self.mn.j])[:-1]
                self.mn.texts = [x for x in cut if x != ' ']
                # update word id dict
                self.mn.word2id = {str(x):self.mn.texts[x] for x in range(len(self.mn.texts))}
                # update t2 text
                self.bf.t2.insert(INSERT, '\n')
                disp = [self.mn.texts[n]+'/'+str(n) for n in range(len(self.mn.texts))]
                self.bf.t2.insert(INSERT, ' '.join(disp))
            elif self.mn.j >= len(self.tm.items[self.mn.k]):
                self.mn.k += 1
                if self.mn.k < len(self.tm.items):
                    self.bf.t1.delete(1.0, END)
                    self.bf.t1.insert(INSERT, self.tm.items[self.mn.k][0], 'color')
                    self.bf.t1.insert(INSERT, ''.join(self.tm.items[self.mn.k][1:]))
                    if self.mn.char_or_word == 'word':
                        cut = list(jieba.cut(self.tm.items[self.mn.k][0]))[:-1]
                    elif self.mn.char_or_word == 'char':
                        cut = list(self.tm.items[self.mn.k][0])[:-1]
                    self.mn.texts = [x for x in cut if x != ' ']
                    # update word id dict
                    self.mn.word2id = {str(x):self.mn.texts[x] for x in range(len(self.mn.texts))}
                    # update t2 text
                    self.bf.t2.delete(1.0, END)
                    self.bf.t2.insert(INSERT, '\n')
                    disp = [self.mn.texts[n]+'/'+str(n) for n in range(len(self.mn.texts))]
                    self.bf.t2.insert(INSERT, ' '.join(disp))
                    self.mn.j = 0
        else:
            ws = [x.split('+') for x in self.word.split('/')]
            words = [[x.split(' ') for x in y] for y in ws]
            word_left = []
            word_righ = []
            rela_class = []
            e_dict = {}
            total = []
            for seq in words:
                wl = []
                wr = []
                for number in seq[0]:
                    wl.append(self.mn.word2id[number]+'+'+str(number))
                word_left.append(wl)
                if wl not in total:
                    total.append(wl)
                for number in seq[1]:
                    wr.append(self.mn.word2id[number]+'+'+str(number))
                word_righ.append(wr)
                if wr not in total:
                    total.append(wr)
                for number in seq[2]:
                    rela_class.append(self.rela_tag[number])
            
            wn = [[int(x.split('+')[1]) for x in y] for y in total]
            # wirte to file
            f = open('tagdata/relation_tag.txt', 'a+', encoding='utf8')
            # build e-tag dict
            for m, l in enumerate(total):
                e_dict[' '.join(l)] = str(m+1)
            # update pre_text
            for n, ids in enumerate(wn):
                if len(ids) == 1:
                    pre_text[ids[0]] = '<e%s>' %(n+1) + pre_text[ids[0]] + '</e%s>' %(n+1)
                elif len(ids) > 1:
                    pre_text[ids[0]] = '<e%s>' %(n+1) + pre_text[ids[0]]
                    pre_text[ids[-1]] = pre_text[ids[-1]] + '</e%s>' %(n+1)
            self.bf.t4.insert(INSERT, ' '.join(pre_text)+'\n')
            f.write(' '.join(pre_text)+'\n')
            for m in range(len(rela_class)):
                self.bf.t4.insert(INSERT, rela_class[m]+'('+'e%s' %e_dict[' '.join(word_left[m])]
                                  +', '+ 'e%s' %e_dict[' '.join(word_righ[m])]+')'+'\n')
                f.write(rela_class[m]+'('+'e%s' %e_dict[' '.join(word_left[m])]
                        +', '+ 'e%s' %e_dict[' '.join(word_righ[m])]+')'+'\n')
            f.write('='*100)
            f.close()
            # skip the tag pointer to the next
            self.mn.j += 1
            if self.mn.j < len(self.tm.items[self.mn.k]):
                # update t1 text
                self.bf.t1.delete(1.0, END)
                self.bf.t1.insert(INSERT, ''.join(self.tm.items[self.mn.k][:self.mn.j]))
                self.bf.t1.insert(INSERT, self.tm.items[self.mn.k][self.mn.j], 'color')
                self.bf.t1.insert(INSERT, ''.join(self.tm.items[self.mn.k][self.mn.j+1:]))
                
                self.bf.t2.delete(1.0, END)
                if self.mn.char_or_word == 'word':
                    cut = list(jieba.cut(self.tm.items[self.mn.k][self.mn.j]))[:-1]
                elif self.mn.char_or_word == 'char':
                    cut = list(self.tm.items[self.mn.k][self.mn.j])[:-1]
                self.mn.texts = [x for x in cut if x != ' ']
                # update word id dict
                self.mn.word2id = {str(x):self.mn.texts[x] for x in range(len(self.mn.texts))}
                # update t2 text
                self.bf.t2.insert(INSERT, '\n')
                disp = [self.mn.texts[n]+'/'+str(n) for n in range(len(self.mn.texts))]
                self.bf.t2.insert(INSERT, ' '.join(disp))
            elif self.mn.j >= len(self.tm.items[self.mn.k]):
                self.mn.k += 1
                if self.mn.k < len(self.tm.items):
                    self.bf.t1.delete(1.0, END)
                    self.bf.t1.insert(INSERT, self.tm.items[self.mn.k][0], 'color')
                    self.bf.t1.insert(INSERT, ''.join(self.tm.items[self.mn.k][1:]))
                    if self.mn.char_or_word == 'word':
                        cut = list(jieba.cut(self.tm.items[self.mn.k][0]))[:-1]
                    elif self.mn.char_or_word == 'char':
                        cut = list(self.tm.items[self.mn.k][0])[:-1]
                    self.mn.texts = [x for x in cut if x != ' ']
                    # update word id dict
                    self.mn.word2id = {str(x):self.mn.texts[x] for x in range(len(self.mn.texts))}
                    # update t2 text
                    self.bf.t2.delete(1.0, END)
                    self.bf.t2.insert(INSERT, '\n')
                    disp = [self.mn.texts[n]+'/'+str(n) for n in range(len(self.mn.texts))]
                    self.bf.t2.insert(INSERT, ' '.join(disp))
                    self.mn.j = 0
            # save the position of tagging word or char
            if self.mn.char_or_word == 'word' and self.mn.ner_or_rela == 'ner':
                confile = open('src/word_ner_config.json', 'w+', encoding='utf8')
            elif self.mn.char_or_word == 'word' and self.mn.ner_or_rela == 'rela':
                confile = open('src/word_rela_config.json', 'w+', encoding='utf8')
            elif self.mn.char_or_word == 'char' and self.mn.ner_or_rela == 'ner':
                confile = open('src/char_ner_config.json', 'w+', encoding='utf8')
            elif self.mn.char_or_word == 'char' and self.mn.ner_or_rela == 'rela':
                confile = open('src/char_rela_config.json', 'w+', encoding='utf8')
            conjson = {'i': self.mn.i, 'j': self.mn.j, 'k': self.mn.k}
            jdump = json.dumps(conjson, ensure_ascii=False)
            confile.write(jdump)
            confile.close()
            self.word = ''
    
    def classify(self, event):
        if len(repr(event.char)) != 2:
            content = self.tm.items[self.mn.k].strip()+'====='+self.tags[self.word]
            self.bf.t4.insert(INSERT, content+'\n')
            self.bf.t4.see(END)
            self.bf.t4.update()
            p = str(int(self.bf.t4.index(INSERT).split('.')[0])-1)+'.0'
            taged = open('tagdata/label_data.txt', 'a+', encoding='utf8')
            taged.write(self.bf.t4.get(p, END)[:-1])
            if self.mn.k+1 < len(self.tm.items):
                self.bf.t1.delete('1.0', END)
                self.bf.t1.insert(INSERT, ''.join(self.tm.items[:self.mn.k+1]))
                self.bf.t1.insert(INSERT, self.tm.items[self.mn.k+1], 'color')
                self.bf.t1.see(INSERT)
                self.bf.t1.update()
                self.bf.t1.insert(INSERT, ''.join(self.tm.items[self.mn.k+2:]))
                self.bf.t2.delete('1.0', END)
                self.bf.t2.insert(END, self.tm.items[self.mn.k+1])
            self.mn.k += 1
            confile = open('src/class_config.json', 'w+', encoding='utf8')
            conjson = {'k': self.mn.k}
            jdump = json.dumps(conjson, ensure_ascii=False)
            confile.write(jdump)
            confile.close()
            taged.close()
        self.word = ''
    
    def choose(self, event):
        c = self.mn.ner_or_rela
        if c == 'ner':
            self.bf.t3.bind('<Return>', self.ner)
        elif c == 'rela':
            self.bf.t3.bind('<Return>', self.relation)
    
    def tag(self):
        self.bf.t3.bind('<Key>', self.inputchar)
        self.bf.t3.bind('<Key-BackSpace>', self.delete)
        self.bf.t3.bind('<Enter>', self.choose)

