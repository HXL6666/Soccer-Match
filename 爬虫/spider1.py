# -*- coding : utf-8 -*-
from urllib import request, parse
from bs4 import BeautifulSoup


# 访问网站的链接，方式和超时时限
def askURL(url, method="get", t=0.5):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35"}
    data = {"hello": "word"}
    # 上传的数据
    data = parse.urlencode(data, encoding="utf-8")
    # 不同的访问方式
    if method == "post":
        req = request.Request(url, data=data, headers=head, method="POST")
    elif method == "get":
        req = request.Request(url, headers=head, method="GET")
    response = request.urlopen(req, timeout=t)
    return response


# 解析得到的网站
def getDATA(baseurl):
    # 解析得到的网站内容
    html = BeautifulSoup(askURL(baseurl), "html.parser")
    # 书名，章节，正文
    title = html.select(".desc-item a")[0].text
    titles = html.select('h1')[0].text
    contents = html.select(".muye-reader-content > div")[0]
    # --------------只返回第一个标签--------------
    # print(html.title)          标签加内容
    # print(html.title.string)   标签里面的内容
    # print(html.title.attrs)    标签里的属性
    # print(html.head.contents[0])
    # print(html.head.contents[1])
    return contents


a = getDATA("https://fanqien ovel.com/reader/6918707245094011405?enter_from=reader")
a = a.text
# 换行
# a = str(a).replace("</p>", "\n")
print(a)
# b = open(r"123.text", 'w+')
# b.write(a)
# b.close()

