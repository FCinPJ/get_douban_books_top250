import re
import url_get
from bs4 import BeautifulSoup

#模拟网页url格式
url = 'https://book.douban.com/top250/?start='
urls = []
nums = [value*25 for value in range(0,10)]

for num in nums:
    urls.append(url+str(num))

for url in urls:

    html = url_get.get_html(url) # 豆瓣读书250第一页到做后一页

    #创建一个BeautifulSoup解析对象
    soup = BeautifulSoup(html,"html.parser",from_encoding = "utf-8")
    #获取所有链接

    # link_nodes = soup.find('a',href = re.compile(r'https://book.douban.com/subject/\d{1,}/')) 正则表达式

    links = soup.find_all('a') #找到所有的<a>标签

    for link in links:
        try:
            print(link['href'],link['title'])
            with open('top250.txt','a') as file_object:
                file_object.write(link['href'])
                file_object.write(link['title'])
                file_object.write("\n")
        except:
            pass
