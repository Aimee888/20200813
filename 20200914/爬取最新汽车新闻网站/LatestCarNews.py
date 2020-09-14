#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : 20200913 -> LatestCarNews.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/9/14 14:24
@Desc    :
================================================="""
import requests
from bs4 import BeautifulSoup
import uuid


def main():
    url_cars_news = "https://www.autohome.com.cn/news/"
    response = requests.get(url_cars_news)
    # 返回什么格式，就编码成什么格式
    response.encoding = response.apparent_encoding
    # features代表以什么引擎转换, lxml比html.parser性能好
    soup = BeautifulSoup(response.text, features='lxml')
    target = soup.find(id="auto-channel-lazyload-article")
    # find是查找第一个出现的对象(是一个对象)，find_all查找所有满足条件的对象（是一个列表,列表中是对象）
    li_list = target.find_all("li")
    for i in li_list:
        a = i.find("a")
        if a:
            print(a.attrs.get('href'))
            txt = a.find("h3")
            print(txt.text)
            img_url = a.find('img').attrs.get('src')
            print(img_url)
            img_response = requests.get("http:" + img_url)
            file_name = str(uuid.uuid4()) + ".jpg"
            with open("./images/{}".format(file_name), "wb") as f:
                f.write(img_response.content)


if __name__ == '__main__':
    main()
