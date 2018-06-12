![](https://github.com/Rogerspy/ManualTag/blob/master/img/3.PNG)

<p align="center">
<a href="https://github.com/Rogerspy/ManualTag"><img src="https://img.shields.io/badge/release-v0.01-brightgreen.svg"></a>
<a href="https://github.com/Rogerspy/ManualTag"><img src="https://img.shields.io/badge/Python-v3.5.2-brightgreen.svg"></a>
<a href="https://github.com/Rogerspy/ManualTag"><img src="https://img.shields.io/badge/tkinter-v8.6-brightgreen.svg"></a>
<a href="https://github.com/Rogerspy/ManualTag"><img src="https://img.shields.io/badge/jieba-v0.39-brightgreen.svg"></a>
</p>
<br>

<h1 align="center"> ManualTag </h1>

# ManualTag简介

ManualTag是一个用于自然语言数据集手动标记的工具。随着以机器学习，深度学习为代表的人工智能算法在越来越广泛的领域里得到应用，其应用瓶颈也日益显现：这些算法需要大量人工标记数据，而目前学术界的实验数据集远远不能满足工业界的需求，所以在实际工业应用中还是要根据业务需求进行人工数据标注。时间就是金钱，纯手工代表着低效，如果能有一个辅助软件能大大提高标记效率那必是极好的。

ManualTag就是以提高人工标记效率为目标而诞生的工具。在实际测试过程中，对于命名实体的标注任务而言，每天可标记**10k**以上的词。
    
# 功能介绍

ManualTag目前是第一版测试版，只能进行命名实体标注（可以是字级别，也可以是词级别）。

## 项目结构

本项目主要包括三个文件夹和一个主文件：

    ManualTag
        |rawdata/
            |data.txt
        |src/
            |config.json
            |wordset.txt
        |tagdata/
            |tagdata.txt
        |datag.py

- rawdata文件夹用于存放待标记数据。
- src文件夹用于存放配置文件：config.json首次标记之前是不存在的，有过标记操作之后会自动生成。其主要作用是用于记录目前标记到的位置，第几篇文档第几行第几个字，方便关闭页面后再次打开时能继续上次操作；wordset.txt是jieba分词用户自定义词库。
- tagdata文件夹用于保存标记后的数据。
- datag.py是ManualTag主程序。

## ManualTag界面介绍

从左到右从上到下的顺序分别是①②③④⑤⑥：

    ① 用于显示需要标记的文档；
    ② 用于显示jieba分词的用户自定义词库（jieba.load_userdict词库）；
    ③ 用于展示需要标记的实体类别和对应的代码；
    ④ 用于显示分词后的句子；
    ⑤ 输入框，简单输入tag对应的代码，回车即可完成一次标注；
    ⑥ 用于预览标记结果。

标记的结果会自动保存在tagdata文件夹下，如果有标记失误或想更改标记可以直接去该文件夹下直接修改标记文件。ManualTag可以自动换行和跳转文档。ManualTag还支持高亮，即对正在标记的行和词进行高亮，方便用户快速进行定位。用户在使用时唯一需要的操作就是输入标记代码、回车（如果有分词不准确的情况可以直接修改，并记录到wordset.txt中，详细用法下面介绍），所以十分高效。

# 使用方法

首先是原始数据的准备：
- 尽量保持存放在同一个.txt文件中，文档间用‘======================================’隔开（参见rawdata中的实例）；
- 尽量保证一句话一行，有助于提高标记质量；
- 将原始数据存放在rawdata文件夹下。

数据准备好后就可以在①界面点击打开按钮，导入数据。此时③界面也会同步导入待标记的句子和高亮正在标记的词。

然后打开主程序代码，自定义实体类别标记与对应的代码，建议与实例保持一致，即“数字+实体”，例如：“1. PER”表示数字键“1”表示PER实体。具体可参见实例。

然后在②界面打开jieba户用自定义词库文件。

在⑤界面输入标注代码，回车就可以进行标注了。

如果标注过程中发现在④界面中分词不准确可以直接在④界面修改（注意保证仍使用“|”进行分割）即可，并记录到②界面保存，可自动更新jieba词库。

**注意：**⑤界面和⑥界面的光标要保持在最后新行。

# 未来计划

短期计划：下一步将加入实体关系标记功能，然后是事件标记。
长期计划：目前该项目是我个人维护，我是以个人在工作中遇到的问题来进行开发，所以长期计划的话要根据工作内容而定，但我希望能将自然语言处理的数据集标注问题全部纳入进来，如果有人有兴趣可与我联系。可issue，可邮箱：rogerspy@163.com

# 关于ManualTag

之所以会想起来开发这个工具，主要是最近的工作中遇到需要手动标记数据的问题，尝试了一下纯手工做，但是效率太低，而且对手和眼睛伤害太大，所以希望能开发一个辅助工具，ManualTag就应运而生了。使用的是Python3.5 + tkinter，我本人这是第一次使用tkinter或者说，我是第一次写图形界面软件，期间看过一些视频教程和一些博客在此对他们表示感谢。从设计界面到设计功能，到功能的实现大概用了2天时间，然后就是各种改bug，改界面，改功能，再改bug，到今天发布第一版，前前后后大概5天时间，如此仓促的时间和完全从零开始，必然会使这个版本代码冗余很大，而且bug也会很多，还希望有兴趣的朋友多提意见，或者也可以和我一起维护。
