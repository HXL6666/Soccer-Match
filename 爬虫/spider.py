from urllib import request, parse


# 访问网站的链接，方式和超时时限
def askURL(url, method="get", t=0.5):
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35"}
    data = bytes(parse.urlencode({"hello": "word"}), encoding="utf-8")                # 需要发送给网页的form表单
    if method == "post":
        req = request.Request(url=url, data=data, headers=head, method="POST")
    elif method == "get":
        req = request.Request(url=url, headers=head, method="GET")
    response = request.urlopen(req, timeout=t)
    print(response.read().decode('utf-8'))


askURL("http://www.douban.com")
