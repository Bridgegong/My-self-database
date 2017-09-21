# -*- coding: utf-8 -*-
# @Time    : 2017/9/18 15:00
# @Author  : Bridge
# @Email   : 13722450120@163.com
# @File    : gupiao.py
# @Software: PyCharm

__name__="yxl"
#下载网页
import re, requests
from urllib import request
from bs4 import BeautifulSoup
html='http://www.xiaohuar.com/hua/'    #练习网址
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36'
        }
req=requests.get(url=html,headers=header)
req.encoding =req.apparent_encoding
soup=BeautifulSoup(req.text, 'lxml')

imgs=soup.find_all('img', src=re.compile(r'/d/file(.*?).jpg'))

n=5
for img in imgs:
    a= 'http://xiaohuar.com/hua%s'%img['src']
    print(a)
    d=request.Request(url=a,headers=header)
    result=request.urlopen(d).content()
    print(result)
    # n-=1
    #
    # with open('%s.jpg'% img['alt'],'wb') as f:
    #     f.write(result)




import re, requests, time, os
from urllib import request
from bs4 import BeautifulSoup
from gevent import monkey
monkey.patch_all()


def get_header(start_url):
    list1 = []
    try:
        html = requests.get(url=start_url)
        soup = BeautifulSoup(html.text, 'lxml')
        imgs = soup.find_all('img', src=re.compile(r'/d/file/\d+/\w+\.jpg'))
        for i in imgs:
            html_url = 'http://www.xiaohuar.com'+i['src'],i['alt']
            list1.append(html_url)
        return (list1)
    except Exception as a:
        print('in get_header error%s' %a)
        return None


def get_xiazai(url):
    one_time = time.time()
    for i in url:
        download = requests.get(i[0]).content
        path = (r'd:/xiaohua/')
        if not os.path.exists(path):
            os.makedirs(path)
        with open(path+i[1]+'.jpg', 'wb') as c:
            c.write(download)
    two_time = time.time()
    print('耗用%s秒'%(two_time-one_time))


def spider():
    start_url = 'http://www.xiaohuar.com/hua'
    url = get_header(start_url)
    get_xiazai(url)


if __name__ == '__main__':
    spider()
