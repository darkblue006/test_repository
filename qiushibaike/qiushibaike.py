# -*- coding:utf-8 -*-
import urllib
import urllib2
from lxml import etree
import os


dir_path = 'C:\\Users\\Administrator\\Desktop'
file_name ='qi'
page = 1


def save(number,name, content):
    file_path_name = dir_path + "\\" +file_name+".txt"
    f = open(file_path_name, "a+")
    f.write(name)
    f.write(content +'\n')
    f.close()


def code(data):
    if isinstance(data,unicode):
        datacode = data.encode('utf-8')
        return datacode
    else:
        datacode =  data.decode('gbk').encode('utf-8')
        return datacode

pages = range(1,page+1)
m = 0

for page_number in pages:
    url ="http://www.qiushibaike.com/hot/page/" + str(page_number)
    print url
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}

    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    data = response.read()
    html = etree.HTML(data)

    name_html = html.xpath('//*/a/h2')
    ies =  range(len(name_html))
    #content = html.xpath('//*/div/div/div[1]/div/div[2]')
    content_html = html.xpath("//*[@class='content']")

    for i in ies:
        name_1 = name_html[i].text
        content_1 = content_html[i].text

        name = code(name_1)
        content= code(content_1)
        m=m+1

        sss =str(m)
        save(sss,name, content)
        ##print m,name,content
        #Creating a new branch is quick & simple.
        ##print m,name,
