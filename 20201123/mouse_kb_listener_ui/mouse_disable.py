#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200913 -> mouse_disable.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/11/23 15:18
@Desc    :禁用鼠标键盘10s，在打开
================================================="""
import time
from ctypes import *

# 禁用鼠标
disable_mouse = windll.user32.BlockInput(True)
# 等待10S
time.sleep(10)
# 开启鼠标
enable_mouse = windll.user32.BlockInput(False)

