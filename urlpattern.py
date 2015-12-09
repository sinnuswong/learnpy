from urllib.request import urlopen
def get_page(url):
      'return content of url'
      if not isinstance(url,str):
            return 'invalid url type'
      elif url.startswith('http://'):
            url_info=urlopen(url).read()
            return url_info
      else:
            return 'recheck you url pattern and start with http://'

print(get_page('http://www.baidu.com'))
assert get_page('www.baidu.com')=='recheck you url pattern and start with http://'
assert get_page(123) =='invalid url type'
