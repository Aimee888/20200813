#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200913 -> myUI_mouse1.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/11/23 13:19
@Desc    :还有问题就是关于双击数量问题，万一两次都点第一个图片
================================================="""
import sys
import os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from ui_mouse import Ui_Form
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, QTimer, Qt


class QmyLabel(QLabel):
    left_double_clicked = pyqtSignal()  # 自定义信号
    right_double_clicked = pyqtSignal()  # 自定义信号

    def mouseDoubleClickEvent(self, event):  # 双击事件的处理
        if event.button() == Qt.LeftButton:
            self.left_double_clicked.emit()
        elif event.button() == Qt.RightButton:
            self.right_double_clicked.emit()


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        # Remove title
        self.setWindowFlags(Qt.CustomizeWindowHint)
        # Initial interface
        self.init_interface()

        # Initial variable
        self.number_left_mouse = 0
        self.number_right_mouse = 0
        self.timer_numer = 0

        # Define label of left mouse
        self.mylabel = QmyLabel(self)
        self.init_mylabel()
        self.mylabel.left_double_clicked.connect(self.do_mylabel_left_double_clicked)

        # Define label of left mouse text
        self.mylabel_text = QmyLabel(self)
        self.init_mylabel_text()

        # Define label of right mouse
        self.mylabel_right = QmyLabel(self)
        self.init_mylabel_right()
        self.mylabel_right.right_double_clicked.connect(self.do_mylabel_right_double_clicked)

        # Define label of right mouse text
        self.mylabel_right_text = QmyLabel(self)
        self.init_mylabel_right_text()

        # Create a timer
        self.timer = QTimer()  # 创建定时器
        self.timer.setInterval(1000)  # 定时周期1000ms
        self.timer.timeout.connect(self.do_timer_timeout)
        self.timer.start()

        # Remove all usb driver
        os.system("devcon.exe remove *USB*")

    def init_interface(self):
        self.ui.label.setText("The test will exit in 20s")

    def init_mylabel(self):
        self.mylabel.setGeometry(10, 60, 300, 300)
        pixmap_left = QPixmap("./pic/default.bmp")
        self.mylabel.setPixmap(pixmap_left)
        self.mylabel.setScaledContents(True)

    def init_mylabel_text(self):
        self.mylabel_text.setText("Please double click mouse left key")
        font = self.mylabel_text.font()
        font.setPointSize(14)
        self.mylabel_text.setFont(font)
        label_size = self.mylabel_text.sizeHint()
        self.mylabel_text.setGeometry(10, 370, label_size.width(), label_size.height())

    def init_mylabel_right(self):
        width_widget = self.width()
        height_widget = self.height()
        self.mylabel_right.setGeometry(int(width_widget - 330), int(height_widget - 330), 300, 300)
        pixmap_right = QPixmap("./pic/default.bmp")
        self.mylabel_right.setPixmap(pixmap_right)
        self.mylabel_right.setScaledContents(True)

    def init_mylabel_right_text(self):
        width_widget = self.width()
        height_widget = self.height()
        self.mylabel_right_text.setText("Please double click mouse right key")
        font = self.mylabel_right_text.font()
        font.setPointSize(14)
        self.mylabel_right_text.setFont(font)
        label_size_right = self.mylabel_right_text.sizeHint()
        self.mylabel_right_text.setGeometry(int(width_widget - 330), int(height_widget - 30), label_size_right.width(),
                                            label_size_right.height())

    def do_timer_timeout(self):
        time_end = 20
        self.timer_numer = self.timer_numer + 1
        self.ui.label.setText("The test will exit in {}s".format(time_end - self.timer_numer))
        if self.timer_numer == time_end:
            self.timer.stop()
            with open("timeout.txt", "w") as f:
                f.write("timeout")
            # Recovery all USB driver
            os.system("devcon.exe rescan")
            os.system(r"""reg add HKLM\SYSTEM\CurrentControlSet\Services\UsbStor /v "Start" /t REG_DWORD /d "3" /f""")
            self.close()

    def do_mylabel_left_double_clicked(self):
        pixmap = QPixmap("./pic/left.bmp")
        self.mylabel.setPixmap(pixmap)
        self.number_left_mouse = self.number_left_mouse + 1
        if self.number_left_mouse >= 1 and self.number_right_mouse >= 1:
            self.timer.stop()
            os.system("devcon.exe rescan")
            os.system(r"""reg add HKLM\SYSTEM\CurrentControlSet\Services\UsbStor /v "Start" /t REG_DWORD /d "3" /f""")
            self.close()

    def do_mylabel_right_double_clicked(self):
        pixmap_right = QPixmap("./pic/right.bmp")
        self.mylabel_right.setPixmap(pixmap_right)
        self.number_right_mouse = self.number_right_mouse + 1
        if self.number_left_mouse >= 1 and self.number_right_mouse >= 1:
            self.timer.stop()
            os.system("devcon.exe rescan")
            os.system(r"""reg add HKLM\SYSTEM\CurrentControlSet\Services\UsbStor /v "Start" /t REG_DWORD /d "3" /f""")
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建app
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())
