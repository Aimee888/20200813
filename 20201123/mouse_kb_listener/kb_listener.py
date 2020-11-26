#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200913 -> kb_listener.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/11/23 9:08
@Desc    :特殊按键在pynput.keyboard.Key“模块”中可以直接找到。比如ctrl对应pynput.keyboard.Key.ctrl还有.ctrl_l以及.ctrl_r。
        普通按键可以通过pynput.keyboard.KeyCode.from_char取得（特殊按键不可以，使用时会出现ArgumentError）。
        如a可以运行pynput.keyboard.KeyCode.from_char('a')获得。
        二者都可以用pynput.keyboard.KeyCode.from_vk通过按键的映射码取得。
================================================="""
from pynput import keyboard


def on_press(key):
    # 通过属性判断按键类型
    print(key)
    try:
        print("alphanumeric key {0} pressed".format(
            key.char))
    except AttributeError:
        print("special key {0} pressed".format(
            key))


def on_release(key):
    print("{0} released".format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


def main():
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    ) as listener:
        listener.join()


if __name__ == '__main__':
    main()
