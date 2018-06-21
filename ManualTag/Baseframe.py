# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 13:38:06 2018

@author: Rogers
"""

from tkinter import *
from tkinter.messagebox import *


class BaseFrame(object):
    """
    Manual text annotation tool.
    """
    def __init__(self, root):
        # build basic frame
        self.root = root
        self.widget = self.root
        # frame 1
        self.frame1 = Frame(self.root, bg='SkyBlue')
        self.frame1.place(relx=0.01, rely=0.01, relwidth=0.33, relheight=0.96)
        ## add display window
        self.t1 = Text(self.frame1, font=('TimeNews', 14), spacing1=5, wrap=NONE, undo=True)
        self.t1.bind('<Button-1>', self.get_widget)
        self.t1.place(relx=0.01, rely=0.07, relwidth=0.98, relheight=0.52)
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
        self.frame2 = Frame(self.root, bg='#FFA54F')
        self.frame2.place(relx=0.35, rely=0.01, relwidth=0.33, relheight=0.4)
        ## add prompt message
        self.prompt1 = Text(self.frame2, bg='#FFA54F', font=('TimeNews', 14), spacing3=4.0)
        self.prompt1.place(relx=0, rely=0, relwidth=0.5, relheight=0.6)
        self.prompt2 = Text(self.frame2, bg='#FFA54F', font=('TimeNews', 14), spacing3=4.0)
        self.prompt2.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.6)
        self.prompt3 = Text(self.frame2, bg='#FFA54F', font=('TimeNews', 14))
        self.prompt3.place(relx=0, rely=0.6, relwidth=1, relheight=0.4)
        
        # frame 3
        self.frame3 = Frame(self.root, bg='SkyBlue')
        self.frame3.place(relx=0.35, rely=0.42, relwidth=0.33, relheight=0.55)
        ## add segmented sentence display window
        self.t2 = Text(self.frame3, font=('宋体',14), wrap=WORD)
        self.t2.bind('<Button-1>', self.get_widget)
        self.t2.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.3)
        ## add input window
        self.t3 = Text(self.frame3, font=('宋体',14), wrap=NONE)
        self.t3.bind('<Button-1>', self.get_widget)
        self.t3.place(relx=0.01, rely=0.325, relwidth=0.98, relheight=0.66)
        s3 = Scrollbar(self.t3, orient = 'vertical', 
                       cursor='hand2', command=self.t3.yview) 
        self.t3['yscrollcommand'] = s3.set
        s3.pack(side='right', fill='y')

        # frame 4
        self.frame4 = Frame(self.root, bg='SkyBlue')
        self.frame4.place(relx=0.69, rely=0.01, relwidth=0.3, relheight=0.96)
        ## add preview window
        self.t4 = Text(self.frame4, font=('宋体',14))
        self.t4.bind('<Button-1>', self.get_widget)
        self.t4.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
        ## add scroll bar
        s4 = Scrollbar(self.t4, orient = 'vertical', 
                       cursor='hand2', command=self.t4.yview) 
        self.t4['yscrollcommand'] = s4.set
        s4.pack(side='right', fill='y')
        
        # frame 5
        self.frame5 = Frame(self.root, bg='SkyBlue')
        self.frame5.place(relx=0.01, rely=0.6, relwidth=0.33, relheight=0.365)
        ## add jieba user dict display
        self.t5 = Text(self.frame5, font=('宋体', 14), undo=True)
        self.t5.bind('<Button-1>', self.get_widget)
        self.t5.place(relx=0.01, rely=0.12, relwidth=0.98, relheight=0.87)
        ## add scroll bar
        s5 = Scrollbar(self.t5, orient = 'vertical',
                       cursor='hand2', command=self.t5.yview) 
        self.t5['yscrollcommand'] = s5.set
        s5.pack(side='right', fill=Y)
        
        self.setup()
    
    def setup(self):
        # get start position
#        try:
#            num = open('src/config.json')
#            nums = json.load(num)
#            num.close()
#            self.i, self.j, self.k = nums['i'], nums['j'], nums['k']
#        except:
#            self.i, self.j, self.k = 0, 0, 0
        pass
            
    def get_widget(self, event):
        self.widget = event.widget
        
        
if __name__ == '__main__':
    root = Tk()
    root.update()
    root.title('Data Tag')
    root.geometry('1920x1080')
    root.update()
    BaseFrame(root)
    mainloop()