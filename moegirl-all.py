#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import os
import time
from html import unescape
from urllib import request

def getHTML(url: str):
    """
    获取URL的HTML代码
    """
    headers = {
    'User-Agent': '''Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360SE'''
    }
    req = request.Request(url=url, headers=headers)
    page = request.urlopen(req)
    html = page.read().decode('utf-8')
    return html

def getTitles(html: str):
    """
    从HTML中获取所有词条标题
    """
    title = re.compile(r'<li.*title="(.*?)".*(?<!</span>)</a></li>')
    titles = title.findall(html)
    return titles

def getNext(html: str):
    """
    获取下一页的URL路径
    """
    nextPage = re.compile(r'<a href="(\S*)" \S*>下一页.*</a>')
    nextPageUrl = nextPage.search(html)
    try:
        nextPageUrl = unescape(nextPageUrl[1])    #处理html转义符
    except TypeError:
        return None
    return nextPageUrl

def saveTXT(data: str, path: str, name: str, mode='wb'):
    """
    保存字符串到文本文件
    """
    f = open(os.path.join(path, name), mode)
    f.write(data.encode('utf-8'))
    f.close()

def readTXT(path: str, name: str, mode='rb'):
    """
    从文本文件读取字符串
    """
    f = open(os.path.join(path, name), mode)
    s = f.read().decode('utf-8')
    f.close()
    return s

if __name__ == '__main__':
    # 配置
    moegirlUrl = 'https://zh.moegirl.icu'
    moegirlAllPageUrl = f'{moegirlUrl}/Special:%E6%89%80%E6%9C%89%E9%A1%B5%E9%9D%A2'
    url = moegirlAllPageUrl
    nextPageUrl = ''
    path = "out"  # 填写爬取的词条存放的文件夹

    # 运行
    if not os.path.isdir(path):
        os.makedirs(path)
    if os.path.isfile(os.path.join(path, 'nextPage')):
        nextPageUrl = readTXT(path, 'nextPage')
        if nextPageUrl != '':
            url = nextPageUrl
    tCount = 0
    titlesList = []
    while nextPageUrl != None:
        html = None
        while not html:
            try:
                html = getHTML(url)
            except HTTPError as e:
                print(e)
                print("HTTP错误！休息5秒……")
                time.sleep(5)
        #saveTXT(html, path, 'AllPage.html')
        titles = getTitles(html)
        print(titles)
        nextPageUrl = getNext(html)
        if nextPageUrl != None:
            url = moegirlUrl + nextPageUrl
        saveTXT(url, path, 'nextPage')
        print(nextPageUrl)
        tCount += len(titles)
        print('当前页词条数%s\t累计词条数%s'%(len(titles), tCount))
        titlesList.extend(titles)
        saveTXT(unescape('\n'.join(titles)), path, '萌娘词条a.txt', 'ab')

    # 保存
    allTitles = unescape('\n'.join(titlesList))
    saveTXT(allTitles, path, 'moegirl-all-titles.txt')
    print('完成！！！')
    #清除nextPage
    saveTXT('', path, 'nextPage')
