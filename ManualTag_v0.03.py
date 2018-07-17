# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 15:24:33 2018

@author: Rogers
"""

from tkinter import *
import ManualTag.Baseframe as mbase
import ManualTag.toolbar as mtool
import ManualTag.menubar as mmenu
import ManualTag.highlight as mhigh
import ManualTag.utils as mutils
import ManualTag.modify as mmodify
import ManualTag.rightbutton as mright
import ManualTag.tag as mtag
import ManualTag.prompt as mprop


if __name__ == '__main__':
#    tag = {'00': 'S-DEGREE', 
#           '01': 'S-SPECIALTY', 
#           '02': 'S-EXPERIENCE', 
#           '03': 'S-DURATION',
#           '04': 'S-RESPONSE', 
#           '05': 'S-SKILL', 
#           '10': 'B-DEGREE',
#           '11': 'B-SPECIALTY',
#           '12': 'B-EXPERIENCE', 
#           '13': 'B-DURATION', 
#           '14': 'B-RESPONSE',
#           '15': 'B-SKILL',
#           '20': 'I-DEGREE', 
#           '21': 'I-SPECIALTY', 
#           '22': 'I-EXPERIENCE',
#           '23': 'I-DURATION', 
#           '24': 'I-RESPONSE', 
#           '25': 'I-SKILL', 
#           '30': 'O'}
    
    tag = {'0':'优秀',
           '1':'合格',
           '2':'不合格'}
    
    rela_tag = {'0': 'DO',
                '1': 'SKILL_LEVEL',
                '2': 'INCLUDE'}
    ner = '''
    实体类别： \n
    0.  DEGREE       - 学历
    1.  SPECIALTY    - 专业
    2.  EXPERIENCE   - 经验
    3.  DURATION     - 经验年限
    4.  RESPONSE     - 职责
    5.  SKILL        - 技能'''
    rela = '''
   关系类别：\n
   0.  DO           - 做
   2.  SKILL_LEVEL  - 技能等级
   3.  INCLUDE      - 包含
   4.  R5           - *****
   5.  R6           - *****'''
    bio = '''
    BIO规则：
    0.  S - single    1.  B - begin
    2.  I - inside    3.  O - outside\n
    例子：
    1 . 负责 桌面端 高精   数据可视化      引擎    研发 
    O O  O     O     O    B-RESPONSE  I-RESPONSE   O
    '''
    root = Tk()
    root.update()
    root.title('Data Tag')
    root.geometry('1920x1080')
    root.update()
    bf = mbase.BaseFrame(root)
    tm = mutils.ToolMenu(bf, root)
    t = mtool.Toolbar(bf, tm)
    t.addtoolbar()
    m = mmenu.Menubar(bf, tm, root)
    m.addmenubar()
    h = mhigh.HighLight(bf)
    h.highlight()
    mod = mmodify.Modify(bf, tm)
    mod.addmodify()
    r = mright.RightButton(bf, tm)
    r.rightbutton()
    tg = mtag.Tag(bf, tm, m, tag, rela_tag)
    tg.tag()
    pro = mprop.Prompt(bf, ner, bio, rela)
    pro.prompt()
    mainloop()