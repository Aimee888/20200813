#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200913 -> color_set.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/11/9 17:20
@Desc    :控制台打印不同颜色字符串，使用方法：python color_set 3E，python color_set 07
            通过控制后面数值来控制前景色和背景色。一般控制台默认颜色是07。
            3E是天蓝色背景黄字，具体可以参考define_color_number里面的定义，第一位3对应的是背景色，第二位E对应的是前景色
================================================="""
import ctypes
import sys

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


def define_color_number():
    STD_INPUT_HANDLE = -10
    STD_OUTPUT_HANDLE = -11
    STD_ERROR_HANDLE = -12

    # 字体颜色定义 ,关键在于颜色编码，由2位十六进制组成，分别取0~f，前一位指的是背景色，后一位指的是字体色
    # 由于该函数的限制，应该是只有这16种，可以前景色与背景色组合。也可以几种颜色通过或运算组合，组合后还是在这16种颜色中

    # Windows CMD命令行 字体颜色定义 text colors
    FOREGROUND_BLACK = 0x00  # black.
    FOREGROUND_DARKBLUE = 0x01  # dark blue.
    FOREGROUND_DARKGREEN = 0x02  # dark green.
    FOREGROUND_DARKSKYBLUE = 0x03  # dark skyblue.
    FOREGROUND_DARKRED = 0x04  # dark red.
    FOREGROUND_DARKPINK = 0x05  # dark pink.
    FOREGROUND_DARKYELLOW = 0x06  # dark yellow.
    FOREGROUND_DARKWHITE = 0x07  # dark white.
    FOREGROUND_DARKGRAY = 0x08  # dark gray.
    FOREGROUND_BLUE = 0x09  # blue.
    FOREGROUND_GREEN = 0x0a  # green.
    FOREGROUND_SKYBLUE = 0x0b  # skyblue.
    FOREGROUND_RED = 0x0c  # red.
    FOREGROUND_PINK = 0x0d  # pink.
    FOREGROUND_YELLOW = 0x0e  # yellow.
    FOREGROUND_WHITE = 0x0f  # white.

    # Windows CMD命令行 背景颜色定义 background colors
    BACKGROUND_BLUE = 0x10  # dark blue.
    BACKGROUND_GREEN = 0x20  # dark green.
    BACKGROUND_DARKSKYBLUE = 0x30  # dark skyblue.
    BACKGROUND_DARKRED = 0x40  # dark red.
    BACKGROUND_DARKPINK = 0x50  # dark pink.
    BACKGROUND_DARKYELLOW = 0x60  # dark yellow.
    BACKGROUND_DARKWHITE = 0x70  # dark white.
    BACKGROUND_DARKGRAY = 0x80  # dark gray.
    BACKGROUND_BLUE = 0x90  # blue.
    BACKGROUND_GREEN = 0xa0  # green.
    BACKGROUND_SKYBLUE = 0xb0  # skyblue.
    BACKGROUND_RED = 0xc0  # red.
    BACKGROUND_PINK = 0xd0  # pink.
    BACKGROUND_YELLOW = 0xe0  # yellow.
    BACKGROUND_WHITE = 0xf0  # white.


def get_color_num(choose_num, color_str):
    back_dic = {
        "0": 0x00,
        "1": 0x10,
        "2": 0x20,
        "3": 0x30,
        "4": 0x40,
        "5": 0x50,
        "6": 0x60,
        "7": 0x70,
        "8": 0x80,
        "9": 0x90,
        "a": 0xa0,
        "b": 0xb0,
        "c": 0xc0,
        "d": 0xd0,
        "e": 0xe0,
        "f": 0xf0
    }

    fore_dic = {
        "0": 0x00,
        "1": 0x01,
        "2": 0x02,
        "3": 0x03,
        "4": 0x04,
        "5": 0x05,
        "6": 0x06,
        "7": 0x07,
        "8": 0x08,
        "9": 0x09,
        "a": 0x0a,
        "b": 0x0b,
        "c": 0x0c,
        "d": 0x0d,
        "e": 0x0e,
        "f": 0x0f
    }

    color_key = color_str.lower()

    if choose_num == 0:
        return back_dic[color_key]
    elif choose_num == 1:
        return fore_dic[color_key]
    else:
        return None


def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool


# reset white
def resetColor():
    set_cmd_text_color(0x0c | 0x0a | 0x09)


def main(color_num, mess):
    back_num = get_color_num(0, color_num[0])
    fore_num = get_color_num(1, color_num[1])
    if fore_num is not None and back_num is not None:
        set_cmd_text_color(fore_num | back_num)
        sys.stdout.write(mess)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == "07":
            resetColor()
        else:
            main(sys.argv[1], "message")
