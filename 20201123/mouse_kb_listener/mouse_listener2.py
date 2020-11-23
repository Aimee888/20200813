#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200913 -> mouse_listener2.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/11/23 8:43
@Desc    :就一次
================================================="""
import pynput


def main():
    with pynput.mouse.Events() as event:
        for i in event:
            if isinstance(i, pynput.mouse.Events.Move):
                print("aaa", i.x, i.y)
            elif isinstance(i, pynput.mouse.Events.Click):
                print(i.x, i.y, i.button, i.pressed)
            elif isinstance(i, pynput.mouse.Events.Scroll):
                print(i.x, i.y, i.dx, i.dy)

            break

        i = event.get(1)
        # 另一种用法
        # 默认值是None。
        # 这个`1`就是最长等待时间，超过这个时间没有事件
        # 就会报错。错误类型是queue模块的Empty，而非TimeoutError。


if __name__ == '__main__':
    main()
