#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200913 -> keyboard_listener.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/11/30 14:34
@Desc    :https://blog.csdn.net/weixin_42487713/article/details/104167605
================================================="""
import pygame
from pygame.locals import *

SCREEN_SIZE = 1000, 500  # 屏幕大小

# 一些常用颜色
WHITE = 255, 255, 255
GRAY = 190, 190, 190
BLACK = 0, 0, 0
LINEN = 250, 240, 230
DARKSLATEGRAY = 47, 79, 79

PAD = 10  # 各物块，按钮之间的 padding
FPS = 60  # pygame显示的fps

DISPLAY_FONT = (None, 40)  # 显示打印文字的字体
DISPLAY_BG_COLOR = LINEN  # 显示打印文字区域的背景色
DISPLAY_TEXT_COLOR = DARKSLATEGRAY  # 打印文字的颜色

KEYBOARD_FONT = (None, 30)  # 按钮字体
KEYBOARD_BUTTON_SIZE = 40, 40  # 按钮大小
KEYBOARD_BG_COLOR = WHITE  # 按钮背景色
KEYBOARD_BG_COLOR_CLICKED = GRAY  # 按钮被选中时的背景色
KEYBOARD_TEXT_COLOR = BLACK  # 按钮文字颜色


class KeyboardButton(pygame.sprite.Sprite):
    def __init__(self, **kwargs):
        # 创建按钮时需要有多个参数
        # size ：按钮的大小
        # value ：按钮的显示值
        # id : 按钮的id
        pygame.sprite.Sprite.__init__(self)
        self.size = kwargs.get('size')
        self.value = kwargs.get('value')
        if kwargs.get('id'):
            self.id = kwargs.get('id')
        else:
            # 若没有id，则我们默认self.value为按钮的self.id
            self.id = self.value
        self.clicked = False  # 按钮是否被选中
        self.render_image()  # 渲染按钮显示图像

    def render_image(self):
        # 主要渲染两个图像：
        # self.image_org为原始图像
        # self.image_clicked为选中时的图像
        font = pygame.font.Font(*KEYBOARD_FONT)
        w, h = font.size(self.value)
        # 初始化Surface
        self.rect = Rect(0, 0, *self.size)
        self.image_org = pygame.Surface(self.size).convert()
        self.image_org.fill(KEYBOARD_BG_COLOR)
        # 居中渲染self.value
        self.image_org.blit(font.render(self.value, True, KEYBOARD_TEXT_COLOR),
                            ((self.size[0] - w) // 2, (self.size[1] - h) // 2))
        self.image_clicked = self.image_org.copy()
        self.image_clicked.fill(KEYBOARD_BG_COLOR_CLICKED)
        self.image_clicked.blit(font.render(self.value, True, KEYBOARD_TEXT_COLOR),
                                ((self.size[0] - w) // 2, (self.size[1] - h) // 2))
        self.image = self.image_org

    def update(self):
        # 根据该按钮是否被选中决定显示图像
        if self.clicked:
            self.image = self.image_clicked
        else:
            self.image = self.image_org


class KeyboardButtonGroup(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)

    def update(self, *args):
        mouse_x, mouse_y, mouse_clicked = args
        for s in self.sprites():
            if s.rect.collidepoint(mouse_x, mouse_y):
                # 鼠标触碰按钮
                # 若鼠标按下
                if mouse_clicked == True:
                    s.clicked = True
                # 若鼠标按上
                elif mouse_clicked == False:
                    if s.clicked:
                        # 若鼠标按上且之前按下时点击的该按钮
                        s.clicked = False
                        add_input(s.id)
            else:
                if mouse_clicked == False:
                    s.clicked = False
            s.update()  # 更新按钮的显示


class Keyboard():
    keyboard_input = [] # 存放input
    output = False # 是否最终输出


def empty_keyboard():
    # 初始化Keyboard中的变量
    Keyboard.keyboard_input = []
    Keyboard.output = False


def add_input(value):
    # 新的输入
    if value == 'del':  # 删除
        if Keyboard.keyboard_input:
            Keyboard.keyboard_input.pop()
    elif value == 'end':  # 输入完毕
        Keyboard.output = True
    else:  # 普通输入
        Keyboard.keyboard_input.append(value)


def get_keyboard_input():
    return Keyboard.keyboard_input


def end_of_input():
    return Keyboard.output


def keyboard(screen):
    empty_keyboard()
    mouse_x, mouse_y, mouse_clicked = 0, 0, None

    keyboard_button_grp = KeyboardButtonGroup()  # 初始化按钮
    for value in [str(i) for i in range(10)] + [chr(i) for i in range(ord('a'), ord('a') + 26)] + ['del', 'end']:
        keyboard_button_grp.add(KeyboardButton(size=KEYBOARD_BUTTON_SIZE, value=value))

    KEYBOARD_BUTTON_PER_ROW = 10  # 每行的按钮数量
    keyboard_rows = (len(keyboard_button_grp) - 1) // KEYBOARD_BUTTON_PER_ROW + 1  # 按钮的总行数
    KEYBOARD_SIZE = KEYBOARD_BUTTON_SIZE[0] * KEYBOARD_BUTTON_PER_ROW + PAD * (KEYBOARD_BUTTON_PER_ROW - 1), \
                    KEYBOARD_BUTTON_SIZE[1] * keyboard_rows + PAD * (keyboard_rows - 1)  # 按钮区域的总大小
    DISPLAY_POSITION = (SCREEN_SIZE[0] - KEYBOARD_SIZE[0]) // 2, SCREEN_SIZE[1] // 10  # 显示输入区域的位置
    display_font = pygame.font.Font(*DISPLAY_FONT)  # 显示输入区域字体
    display_height = display_font.get_height() + 2 * PAD  # 显示输入区域高度

    x, y = DISPLAY_POSITION[0], DISPLAY_POSITION[1] + display_height + PAD  # 按钮区域的位置
    start_x = x
    # 对每个按钮位置进行排列
    for i, button in enumerate(keyboard_button_grp):
        button.rect.topleft = x, y
        if (i + 1) % KEYBOARD_BUTTON_PER_ROW:
            x += KEYBOARD_BUTTON_SIZE[0] + PAD
        else:
            x = start_x
            y += KEYBOARD_BUTTON_SIZE[1] + PAD

    def draw_area_display(screen):
        # 绘显示输入区域
        img = pygame.Surface((KEYBOARD_SIZE[0], display_height)).convert()
        img.fill(DISPLAY_BG_COLOR)
        img.blit(display_font.render(''.join(get_keyboard_input()), True, DISPLAY_TEXT_COLOR), (PAD, PAD))
        screen.blit(img, DISPLAY_POSITION)

    def draw_area_keyboard(screen, keyboard_button_grp):
        # 绘按钮区域
        keyboard_button_grp.draw(screen)

    fps_clock = pygame.time.Clock()
    while True:
        # 判断是否最终输出
        if end_of_input():
            return get_keyboard_input()

        mouse_clicked = None
        # 获取 mouse_x, mouse_y, mouse_clicked
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_clicked = True
            elif event.type == MOUSEBUTTONUP:
                mouse_clicked = False
            elif event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos

        screen.fill(BLACK)
        draw_area_display(screen)
        keyboard_button_grp.update(mouse_x, mouse_y, mouse_clicked)
        draw_area_keyboard(screen, keyboard_button_grp)
        fps_clock.tick(FPS)
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    result = keyboard(screen)
    print(result)
    pygame.quit()
