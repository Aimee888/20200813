#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200913 -> myUI_keyboard.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/11/24 15:02
@Desc    :
================================================="""
import sys
import os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, QThread
from ui_keyboard import Ui_Form
from pynput import keyboard


class kb_listener(QThread):
    keyname = pyqtSignal(str)

    def __init__(self):
        super(kb_listener, self).__init__()

    def run(self):  # 在启动线程后任务从这个函数里面开始执行
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release
        ) as self.listener:
            self.listener.join()

    def on_press(self, key):
        # 通过属性判断按键类型
        try:
            # print("alphanumeric key {0} pressed".format(
            #     key.char))
            print("{0}".format(key))
            if "{0}".format(key)[0] == "<":
                self.keyname[str].emit("{0}".format(key))
            else:
                print(key.char)
                self.keyname[str].emit(key.char)
        except AttributeError:
            # print("special key {0} pressed".format(
            #     key))
            key_special = "{0}".format(key)[4:]
            print(key_special)
            self.keyname[str].emit(key_special)

    def on_release(self, key):
        # self.keyname[str].emit(key)
        pass
        # print("{0} released".format(
        #     key))
        # if key == keyboard.Key.esc:
            # Stop listener
            # self.listener.stop()
            # return False


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_Form()  # 创建UI对象ab
        self.ui.setupUi(self)  # 构造UI
        self.mythread = kb_listener()
        self.mythread.keyname.connect(self.do_keyname)
        self.mythread.start()
        self.key_set = []

    def closeEvent(self, event):
        self.mythread.listener.stop()

    def get_key(self, name):
        key_name = {
            'a': self.ui.char_a_,
            'b': self.ui.char_b_,
            'c': self.ui.char_c_,
            'd': self.ui.char_d_,
            'e': self.ui.char_e_,
            'f': self.ui.char_f_,
            'g': self.ui.char_g_,
            'h': self.ui.char_h_,
            'i': self.ui.char_i_,
            'j': self.ui.char_j_,
            'k': self.ui.char_k_,
            'l': self.ui.char_l_,
            'm': self.ui.char_m_,
            'n': self.ui.char_n_,
            'o': self.ui.char_o_,
            'p': self.ui.char_p_,
            'q': self.ui.char_q_,
            'r': self.ui.char_r_,
            's': self.ui.char_s_,
            't': self.ui.char_t_,
            'u': self.ui.char_u_,
            'v': self.ui.char_v_,
            'w': self.ui.char_w_,
            'x': self.ui.char_x_,
            'y': self.ui.char_y_,
            'z': self.ui.char_z_,
            '0': self.ui.num_0_,
            '1': self.ui.num_1_,
            '2': self.ui.num_2_,
            '3': self.ui.num_3_,
            '4': self.ui.num_4_,
            '5': self.ui.num_5_,
            '6': self.ui.num_6_,
            '7': self.ui.num_7_,
            '8': self.ui.num_8_,
            '9': self.ui.num_9_,
            '-': self.ui.btn_dec_,
            '=': self.ui.btn_add_,
            '[': self.ui.btn_left_bracket_,
            ']': self.ui.btn_right_bracket_,
            '\\': self.ui.btn_slash_,
            ';': self.ui.btn_semicolon_,
            "'": self.ui.btn_quota_,
            ',': self.ui.btn_comma_,
            '.': self.ui.btn_dot_,
            '/': self.ui.btn_backslash_,
            'backspace': self.ui.btn_backspace_,
            'enter': self.ui.btn_enter_,
            'shift': self.ui.btn_shift_l_,
            'shift_r': self.ui.btn_shift_r_,
            'ctrl_l': self.ui.btn_ctrl_l_,
            'ctrl_r': self.ui.btn_ctrl_r_,
            'alt_l': self.ui.btn_alt_l_,
            'alt_r': self.ui.btn_alt_r_,
            'space': self.ui.btn_space_,
            'up': self.ui.btn_up_,
            'down': self.ui.btn_down_,
            'left': self.ui.btn_left_,
            'right': self.ui.btn_right_,
            'caps_lock': self.ui.btn_capslock_,
            'f1': self.ui.btn_f1_,
            'f2': self.ui.btn_f2_,
            'f3': self.ui.btn_f3_,
            'f4': self.ui.btn_f4_,
            'f5': self.ui.btn_f5_,
            'f6': self.ui.btn_f6_,
            'f7': self.ui.btn_f7_,
            'f8': self.ui.btn_f8_,
            'f9': self.ui.btn_f9_,
            'f10': self.ui.btn_f10_,
            'f11': self.ui.btn_f11_,
            'f12': self.ui.btn_f12_,
            'print_screen': self.ui.btn_printscreen_,
            'scroll_lock': self.ui.btn_scrolllock_,
            'pause': self.ui.btn_pause_,
            '`': self.ui.btn_waveline,
            'insert': self.ui.btn_insert_,
            'home': self.ui.btn_home_,
            'page_up': self.ui.btn_pageup_,
            'tab': self.ui.btn_tab_,
            'delete': self.ui.btn_delete_,
            'end': self.ui.btn_end_,
            'page_down': self.ui.btn_pagedown_,
            'esc': self.ui.btn_esc_,
            '<105>': self.ui.num_9_,
            '<104>': self.ui.num_8_,
            '<103>': self.ui.num_7_,
            '<102>': self.ui.num_6_,
            '<101>': self.ui.num_5_,
            '<100>': self.ui.num_4_,
            '<99>': self.ui.num_3_,
            '<98>': self.ui.num_2_,
            '<97>': self.ui.num_1_,
            '<96>': self.ui.num_0_,
            '<110>': self.ui.btn_dot_,
            '+': self.ui.btn_add_,
            '*': self.ui.num_8_,
        }
        for i, keyname in enumerate(key_name.keys()):
            if keyname == name:
                self.key_set.append(i)
                return key_name[name]
        return None

    def do_keyname(self, name):
        button_object = self.get_key(name)
        if button_object is None:
            pass
        else:
            self.get_key(name).setStyleSheet("QPushButton{background-color:rgb(170,200,50)}")
            list1 = sorted(set(self.key_set), key=self.key_set.index)
            if len(list1) == 84:
                self.close()


def start_window():
    app = QApplication(sys.argv)  # 创建app
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start_window()

