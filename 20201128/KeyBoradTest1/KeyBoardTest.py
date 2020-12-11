#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200913 -> bbbb.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/12/5 14:35
@Desc    :
================================================="""
import sys
import os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtWidgets import QApplication, QWidget, QShortcut
from PyQt5.QtCore import pyqtSignal, QThread, Qt
from ui_keyboard import Ui_Form
from pynput import keyboard


class kb_listener(QThread):
    keyname = pyqtSignal()

    def __init__(self):
        super(kb_listener, self).__init__()

    def run(self):  # 在启动线程后任务从这个函数里面开始执行
        with keyboard.Listener(
                on_press=self.on_press,
        ) as self.listener:
            self.listener.join()

    def on_press(self, key):
        key_name = "{0}".format(key)
        if key_name == "Key.print_screen":
            self.keyname.emit()


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_Form()  # 创建UI对象ab
        self.ui.setupUi(self)  # 构造UI

        self.color_pressed = "QPushButton{background-color:rgb(170,200,50)}"
        self.ui.label.setFocusPolicy(Qt.StrongFocus)

        self.key_name_normal = {
            1: self.ui.btn_esc_,
            59: self.ui.btn_f1_,
            60: self.ui.btn_f2_,
            61: self.ui.btn_f3_,
            62: self.ui.btn_f4_,
            63: self.ui.btn_f5_,
            64: self.ui.btn_f6_,
            65: self.ui.btn_f7_,
            66: self.ui.btn_f8_,
            67: self.ui.btn_f9_,
            68: self.ui.btn_f10_,
            87: self.ui.btn_f11_,
            88: self.ui.btn_f12_,
            41: self.ui.btn_waveline,
            2: self.ui.num_1_,
            3: self.ui.num_2_,
            4: self.ui.num_3_,
            5: self.ui.num_4_,
            6: self.ui.num_5_,
            7: self.ui.num_6_,
            8: self.ui.num_7_,
            9: self.ui.num_8_,
            10: self.ui.num_9_,
            11: self.ui.num_0_,
            12: self.ui.btn_minus_,
            13: self.ui.btn_plus_,
            14: self.ui.btn_backspace_,
            15: self.ui.btn_tab_,
            16: self.ui.char_q_,
            17: self.ui.char_w_,
            18: self.ui.char_e_,
            19: self.ui.char_r_,
            20: self.ui.char_t_,
            21: self.ui.char_y_,
            22: self.ui.char_u_,
            23: self.ui.char_i_,
            24: self.ui.char_o_,
            25: self.ui.char_p_,
            26: self.ui.btn_left_bracket_,
            27: self.ui.btn_right_bracket_,
            28: self.ui.btn_enter_,
            58: self.ui.btn_capslock_,
            30: self.ui.char_a_,
            31: self.ui.char_s_,
            32: self.ui.char_d_,
            33: self.ui.char_f_,
            34: self.ui.char_g_,
            35: self.ui.char_h_,
            36: self.ui.char_j_,
            37: self.ui.char_k_,
            38: self.ui.char_l_,
            39: self.ui.btn_semicolon_,
            40: self.ui.btn_quota_,
            43: self.ui.btn_slash_,
            42: self.ui.btn_shift_l_,
            44: self.ui.char_z_,
            45: self.ui.char_x_,
            46: self.ui.char_c_,
            47: self.ui.char_v_,
            48: self.ui.char_b_,
            49: self.ui.char_n_,
            50: self.ui.char_m_,
            51: self.ui.btn_comma_,
            52: self.ui.btn_dot_,
            53: self.ui.btn_backslash_,
            29: self.ui.btn_ctrl_l_,
            56: self.ui.btn_alt_l_,
            57: self.ui.btn_space_,

            70: self.ui.btn_scrolllock_,
            69: self.ui.btn_pause_,
            55: self.ui.btn_multiply_,
            74: self.ui.btn_subtract_,
            71: self.ui.btn_numpad7_,
            72: self.ui.btn_numpad8_,
            73: self.ui.btn_numpad9_,
            78: self.ui.btn_add_,
            75: self.ui.btn_numpad4_,
            76: self.ui.btn_numpad5_,
            77: self.ui.btn_numpad6_,
            79: self.ui.btn_numpad1_,
            80: self.ui.btn_numpad2_,
            81: self.ui.btn_numpad3_,
            82: self.ui.btn_numpad0_,
            83: self.ui.btn_decimal_,

            338: self.ui.btn_insert_,
            327: self.ui.btn_home_,
            329: self.ui.btn_pageup_,
            339: self.ui.btn_delete_,
            335: self.ui.btn_end_,
            337: self.ui.btn_pagedown_,
            54: self.ui.btn_shift_r_,
            312: self.ui.btn_alt_r_,
            285: self.ui.btn_ctrl_r_,
            325: self.ui.btn_numlock_,
            309: self.ui.btn_divide_,
            284: self.ui.btn_return_,
            328: self.ui.btn_up_,
            336: self.ui.btn_down_,
            331: self.ui.btn_left_,
            333: self.ui.btn_right_,
        }

        self.mythread = kb_listener()
        self.mythread.keyname.connect(self.do_keyname)
        self.mythread.start()
        self.screen_press = False

    def do_keyname(self):
        self.ui.btn_printscreen_.setStyleSheet(self.color_pressed)
        self.mythread.listener.stop()
        self.screen_press = True

    def keyReleaseEvent(self, event):
        # print("按下：" + str(event.key()))
        scancode = event.nativeScanCode()
        print(scancode)
        if scancode in self.key_name_normal.keys():
            self.key_name_normal[scancode].setStyleSheet(self.color_pressed)


def start_window():
    app = QApplication(sys.argv)  # 创建app
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start_window()
