# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 19:23:38 2018

@author: Rogers
"""

from tkinter import *

class RightButton(object):
    def __init__(self, baseframe, toolmenu):
        self.bf = baseframe
        self.tm = toolmenu
    
    def setup(self):
        pass
    
    def popupmenu(self, event):
        self.menu.post(event.x_root, event.y_root)
    
    def rightbutton(self):
        self.bf.widget = self.bf.root
        self.menu = Menu(self.bf.widget, tearoff=0)
        self.menu.add_command(label="剪切", accelerator = "Ctrl + X", command=self.tm.cut)
        self.menu.add_command(label="复制", accelerator = "Ctrl + C", command=self.tm.copy)
        self.menu.add_command(label="粘贴", accelerator = "Ctrl + V", command=self.tm.paste)
        self.menu.add_separator()
        self.menu.add_command(label='撤销', accelerator='Ctrl + Z', command=self.tm.undo)
        self.menu.add_command(label='恢复', accelerator='Ctrl + Y', command=self.tm.redo)
        self.menu.add_separator()
        self.menu.add_command(label="查找", accelerator = "Ctrl + F", command=self.tm.search)
        self.menu.add_command(label="全选", accelerator = "Ctrl + A", command=self.tm.selectAll)
        self.bf.widget.bind("<Button-3>", self.popupmenu)