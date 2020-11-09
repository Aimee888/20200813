#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200913 -> monitor_keyboard.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/9/21 15:39
@Desc    :
================================================="""
from pynput.keyboard import Controller, Key, Listener
import threading
from threading import Timer
import time

close_timer = False


# 监听按压
def on_press(key):
    try:
        print("正在按压:", format(key.char))
    except AttributeError:
        print("正在按压:", format(key))


# 监听释放
def on_release(key):
    global close_timer
    print("已经释放:", format(key))

    if key == Key.esc:
        # 关闭定时器
        close_timer = True
        # 停止监听
        return False


# 开始监听
def start_listen():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


def auto_press_keybord():
    kb.type("1 ")
    # 开启定时器
    if not close_timer:
        t = Timer(60, auto_press_keybord, args=None, kwargs=None)
        t.start()


if __name__ == '__main__':
    # 实例化键盘
    kb = Controller()

    # # 使用键盘输入一个字母
    # kb.press('a')
    # kb.release('a')
    #
    # # 使用键盘输入字符串,注意当前键盘调成英文
    # kb.type("hello world")
    #
    # # 使用Key.xxx输入1
    # kb.press(Key.space)

    # 开始监听,按esc退出监听
    t1 = threading.Thread(target=start_listen)
    # start_listen()
    t1.start()

    time.sleep(5)
    auto_press_keybord()



