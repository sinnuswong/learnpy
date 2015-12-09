import requests 
url = 'http://bbs.byr.cn/default'
header = {"X-Requested-With":"XMLHttpRequest"}
r = requests.get(url,headers=header) 
 
print r.status_code
print r.text


