from urllib.request import urlretrieve,urlopen
import re,random

pageurl='http://imgsrc.baidu.com/forum/w%3D580/sign=1886489006087bf47dec57e1c2d2575e/d4e282025aafa40f4ee8b906af64034f79f019d4.jpg'
localdir='c:\\Users\\sinnus\\Desktop\\re\\'

def callbackfunc(blocknum,blocksize,totalsize):
      
      '''回调函数
    @blocknum: 已经下载的数据块数
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
      percent=100.0*blocknum*blocksize/totalsize
      if percent > 100:
            percent=100
      print("%.2f%%"%percent)


def get_content(url):
      return urlopen(url).read().decode('utf8')

def find_pageurls(page):
      reg = r'src="(.+?\.jpg)" pic_ext'
      imgre = re.compile(reg)
      imglist = re.findall(imgre,page)
      return imglist

def load_from_pageurls(pageurls):
      
      print(pageurls)
      for pageurl in pageurls:
            urlretrieve(pageurl,localdir+str(random.randrange(10000))+".jpg")
            

def download():
      l=['3699213395','3698042377','3700352088','3697356808','3501406031']
      for n in l:
            url="http://tieba.baidu.com/p/"+n
            print(url)
            content=get_content(url)
            pageurls=find_pageurls(content)
            load_from_pageurls(pageurls)

download()
      


