#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200913 -> myUI_mouse.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/11/23 9:35
@Desc    :
================================================="""
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui_mouse import Ui_Form
from PyQt5.QtGui import QImage, QPixmap
import cv2


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        self.loadimage("./pic/default.bmp", self.ui.label_left)
        self.loadimage("./pic/default.bmp", self.ui.label_right)

    def loadimage(self, path, object):
        self.image = cv2.imread(path)
        self.showimage(object)

    def showimage(self, object):
        print(self.image.shape)
        qimageformat = QImage.Format_Indexed8
        if len(self.image.shape) == 3:
            if self.image.shape[2] == 4:
                qimageformat = QImage.Format_RGBA8888
            else:
                qimageformat = QImage.Format_RGB888
        img = QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.strides[0], qimageformat)
        img = img.rgbSwapped()
        object.setPixmap(QPixmap.fromImage(img))


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建app
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())

