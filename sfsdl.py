from urllib.request import urlopen

content=urlopen("http://money.163.com/special/pinglun/").read();
s=content.decode('unicode')
print(s)
