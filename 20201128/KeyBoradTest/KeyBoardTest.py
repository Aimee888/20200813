#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200913 -> KeyBoardTest.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/11/27 11:27
@Desc    :此程序有个问题，当按键过快时，界面可能会卡住
================================================="""
import sys
import os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, QThread, Qt
from ui_keyboard import Ui_Form
import pythoncom
import pyHook


class kb_listener(QThread):
    keyname = pyqtSignal([str, int])

    def __init__(self):
        super(kb_listener, self).__init__()

    def run(self):  # 在启动线程后任务从这个函数里面开始执行
        hm = pyHook.HookManager()
        hm.KeyDown = self.onKeyboardEvent
        hm.HookKeyboard()
        pythoncom.PumpMessages()

    def onKeyboardEvent(self, event):
        print("Key:", event.Key)
        print("Extended:", event.Extended)
        self.keyname[str, int].emit(event.Key, event.Extended)
        return True


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_Form()  # 创建UI对象ab
        self.ui.setupUi(self)  # 构造UI
        self.mythread = kb_listener()
        self.mythread.keyname.connect(self.get_key)
        self.mythread.start()
        self.key_name0 = {
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
            'oem_minus': self.ui.btn_minus_,
            'oem_plus': self.ui.btn_plus_,
            'oem_comma': self.ui.btn_comma_,
            'oem_period': self.ui.btn_dot_,
            'oem_1': self.ui.btn_semicolon_,
            'oem_2': self.ui.btn_backslash_,
            'oem_3': self.ui.btn_waveline,
            'oem_4': self.ui.btn_left_bracket_,
            'oem_5': self.ui.btn_slash_,
            'oem_6': self.ui.btn_right_bracket_,
            "oem_7": self.ui.btn_quota_,
            'back': self.ui.btn_backspace_,
            'return': self.ui.btn_enter_,
            'lshift': self.ui.btn_shift_l_,
            'lcontrol': self.ui.btn_ctrl_l_,
            'lmenu': self.ui.btn_alt_l_,
            'space': self.ui.btn_space_,
            'capital': self.ui.btn_capslock_,
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
            'scroll': self.ui.btn_scrolllock_,
            'pause': self.ui.btn_pause_,
            'tab': self.ui.btn_tab_,
            'escape': self.ui.btn_esc_,
            'multiply': self.ui.btn_multiply_,
            'subtract': self.ui.btn_subtract_,
            'add': self.ui.btn_add_,
            'numpad9': self.ui.btn_numpad9_,
            'numpad8': self.ui.btn_numpad8_,
            'numpad7': self.ui.btn_numpad7_,
            'numpad6': self.ui.btn_numpad6_,
            'numpad5': self.ui.btn_numpad5_,
            'numpad4': self.ui.btn_numpad4_,
            'numpad3': self.ui.btn_numpad3_,
            'numpad2': self.ui.btn_numpad2_,
            'numpad1': self.ui.btn_numpad1_,
            'numpad0': self.ui.btn_numpad0_,
            'decimal': self.ui.btn_decimal_,
            'insert': self.ui.btn_numpad0_,
            'end': self.ui.btn_numpad1_,
            'down': self.ui.btn_numpad2_,
            'next': self.ui.btn_numpad3_,
            'left': self.ui.btn_numpad4_,
            'clear': self.ui.btn_numpad5_,
            'right': self.ui.btn_numpad6_,
            'home': self.ui.btn_numpad7_,
            'up': self.ui.btn_numpad8_,
            'prior': self.ui.btn_numpad9_,
            'delete': self.ui.btn_decimal_,
        }
        self.key_name1 = {
            'rshift': self.ui.btn_shift_r_,
            'snapshot': self.ui.btn_printscreen_,
            'insert': self.ui.btn_insert_,
            'home': self.ui.btn_home_,
            'prior': self.ui.btn_pageup_,
            'delete': self.ui.btn_delete_,
            'end': self.ui.btn_end_,
            'next': self.ui.btn_pagedown_,
            'rcontrol': self.ui.btn_ctrl_r_,
            'rmenu': self.ui.btn_alt_r_,
            'up': self.ui.btn_up_,
            'down': self.ui.btn_down_,
            'left': self.ui.btn_left_,
            'right': self.ui.btn_right_,
            'numlock': self.ui.btn_numlock_,
            'divide': self.ui.btn_divide_,
            'return': self.ui.btn_return_,
        }

        # self.key_set = []

    def closeEvent(self, event):
        pass

    def get_key(self, name, dic_num):
        if name.lower() == "lwin" or name.lower() == "rwin":
            pass
        elif name.lower() == "apps":
            pass
        else:
            if dic_num == 0:
                self.key_name0[name.lower()].setStyleSheet("QPushButton{background-color:rgb(170,200,50)}")
            elif dic_num == 1:
                self.key_name1[name.lower()].setStyleSheet("QPushButton{background-color:rgb(170,200,50)}")
        # else:
        #     key_name = {}
        #
        # for keyname in key_name.keys():
        #     if keyname == name.lower():
        #         return key_name[keyname]
        # return None

    # def do_keyname(self, name, extend):
        # self.get_key(name, extend)
        # print(name)
        # print(extend)
        # if extend == 0:
        #     button_object = self.get_key(name, 0)
        # elif extend == 1:
        #     button_object = self.get_key(name, 1)
        # else:
        #     button_object = None
        # if button_object is None:
        #     pass
        # else:
            # self.key_set.append(button_object)
            # list1 = sorted(set(self.key_set), key=self.key_set.index)
            # button_object.setStyleSheet("QPushButton{background-color:rgb(170,200,50)}")
            # if len(list1) == 101:
            #     self.close()


def start_window():
    app = QApplication(sys.argv)  # 创建app
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start_window()

