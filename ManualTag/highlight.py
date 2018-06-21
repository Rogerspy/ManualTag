# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 17:19:44 2018

@author: Rogers
"""

class HighLight(object):
    def __init__(self, baseframe):
        self.bf = baseframe
    
    def setup(self):
        pass
    
    def highlight(self):
        self.bf.t1.tag_config('color', foreground='red', background='yellow')
        self.bf.t2.tag_config('color', foreground='red', background='yellow')