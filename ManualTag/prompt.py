# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 14:22:51 2018

@author: Rogerspy
"""

from tkinter import *


class Prompt(object):
    def __init__(self, baseframe, ner, bio, rela):
        self.bf = baseframe
        self.ner = ner
        self.bio = bio
        self.rela = rela
    
    def setup(self):
        pass
    
    def prompt(self):
        self.bf.prompt1.insert(INSERT, '\n'+self.ner)
        self.bf.prompt1.configure(state="disabled")
        self.bf.prompt2.insert(INSERT, '\n'+self.rela)
        self.bf.prompt2.configure(state="disabled")
        self.bf.prompt3.insert(INSERT, self.bio)
        self.bf.prompt3.configure(state="disabled")
