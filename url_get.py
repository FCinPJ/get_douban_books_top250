# 简单页面获取

#coding:utf-8
import urllib.request

def get_html(url):

    page = urllib.request.urlopen(url) # 打开网页
    
    htmlcode = page.read() # 读取页面源码

    #if page.getcode()==200:
    #    print("读取成功") # 获取状态码，200表示成功

    return htmlcode



