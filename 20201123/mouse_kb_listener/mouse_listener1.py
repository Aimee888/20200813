#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200913 -> mouse_listener1.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/11/23 8:27
@Desc    :Reference: https://blog.csdn.net/u011367482/article/details/106173994/
================================================="""
import pynput, time


def on_move(x, y):
    print("Pointer moved to {0}".format((x, y)))


def on_click(x, y, button, pressed):
    print("{0} at {1}".format(
        "Pressed" if pressed else "Released", (x, y)
    ))
    if not pressed:
        # Stop listener
        return False


def on_scroll(x, y, dx, dy):
    print("Scrolled {0} at {1}".format(
        "down" if dy < 0 else "up", (x, y)
    ))


def main():
    with pynput.mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll
    ) as listener:
        listener.join()


if __name__ == '__main__':
    main()
