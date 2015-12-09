# -*- coding: utf-8 -*-
import requests

url = 'http://bbs.byr.cn/board/Friends'

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, compress',
           'Accept-Language': 'en-us;q=0.5,en;q=0.3',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           
           'X-Requested-With': 'XMLHttpRequest',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36' }
s = requests.Session()
s.headers.update(headers)
s.get(url)

_URL = 'http://bbs.byr.cn/user/ajax_session.json'
s.post(_URL,data={'id':'sinnus',
                  'passwd':'69011138wk',
                  'isajax':'yes'})

r = s.get(url)
r.encoding = 'gb2312'
cnt = r.text
import re

regex = '<a href="/article/Friends/(\d+?)">(.+?)</a>'
res = re.findall(regex,cnt)
for t in res:
       print t[0],t[1]
