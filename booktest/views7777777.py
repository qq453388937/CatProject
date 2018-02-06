# coding=utf-8
from django.http import *

# Ctrl + W    选中增加的代码块
# Ctrl + Shift + V    从最近的缓冲区粘贴
# Ctrl+ SHIFT + `-`|'+' 折叠事所有
# Ctrl + +|- 展开或者折叠单个
# Ctrl + f  ++++ Ctrl + r
# Ctrl + E   当前文件弹出，打开最近使用的文件列表
# Shift + F11显示书签
# Ctrl + ]/[跳转到代码块结束、开始
# Ctrl+Shift+Backspace    导航到最近编辑区域 {差不多就是返回上次编辑的位置}
# Ctrl + F1    显示错误描述或警告信息
# Ctrl + Shift + F  或者连续2次敲击shift
# 全局查找{可以在整个项目中查找某个字符串什么的，如查找某个函数名字符串看之前是怎么使用这个函数的}
# Ctrl + Alt + R   运行manage.py任务
# alt+f9 运行游标至当前行(前提是循环)
# f8 跳过到断点.
# Ctrl+Alt+Left/Right   后退、前进
# Ctrl + ]/[跳转到代码块结束、开始
# Ctrl + F12弹出文件结构
# Ctrl + Shift + F12最大化编辑开关
# Shift + F11显示书签
# 光标移动至方法名　ｃｔｒｌ＋ｂ可以转到调用 光标移动至变量声明出可以查询所有用到该变量的位置
"""
4、调试(Debugging)
F8   跳过
F7   进入
Shift + F8   退出
Alt + F9    运行游标
Alt + F8    验证表达式
Ctrl + Alt + F8   快速验证表达式
F9    恢复程序
Ctrl + F8   断点开关
Ctrl + Shift + F8   查看断
"""

def index(request):
    return HttpResponse("hello views777777755")