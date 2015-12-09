import requests
import re
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, compress',
           'Accept-Language': 'en-us;q=0.5,en;q=0.3',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           
           'X-Requested-With': 'XMLHttpRequest',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36' }

index = 'bbs.byr.cn'

def setup():
       s = requests.Session()
       s.headers.update(headers)
       _URL = 'http://bbs.byr.cn/user/ajax_session.json'
       s.post(_URL,data={'id':'sinnus',
                  'passwd':'69011138wk',
                  'isajax':'yes'})
       return s

def loads(url,page=1):
       s = setup()
       r = s.get(url+'?p='+str(page))
       r.encoding = 'gb2312'
       return r.text

def grap(cnt):
       regex = '<a href="/article/Friends/(\d+?)">(.+?)</a>'
       p = re.compile(regex)
       res = p.findall(cnt)
       urls = []
       for t in res:
              print t[1],index+"/article/Friends/"+t[0]
              urls.append(index+"/article/Friends/"+t[0])
       return urls

def article_regex():
        #'<a href=".+?">(.+)</a></span>.*'
       regex='<div class="a-content-wrap">(.+?)<font class="f000"></font>'
       return re.compile(regex)
if __name__=="__main__":
       url = 'http://bbs.byr.cn/board/Friends'
       for i in range(1,2):
              cnt = loads(url,i)
              urls = grap(cnt)
              print 'http://'+urls[5]
              cnt =  loads('http://'+urls[5])
              p = article_regex()
              res = p.findall(cnt)
              
              for t in res:
                     print t
                     print '*'*16
       
