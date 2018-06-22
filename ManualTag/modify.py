# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 17:32:05 2018

@author: Rogerspy
"""

from tkinter import *


class Modify(object):
    def __init__(self, baseframe, toolmenu):
        self.bf = baseframe
        self.tm = toolmenu
    
    def setup(self):
        pass
    
    def modify(self, event):
        self.tm.texts = [x.strip() for x in self.bf.t2.get('2.0', END).split('|')]
        
    def addmodify(self):
        self.bf.t3.bind('<ButtonRelease-1>', self.modify)
