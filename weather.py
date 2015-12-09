from urllib.request import urlopen
from xml.dom import minidom
import sys
def change_code(location):
      if not isinstance(location,bytes):return ""
      res=""
      for l in location:
            res+=hex(l)
      res=res.replace('0x','%')
      #print(res)
      return res

output="xml"
print("查询地区天气预报")
city_name=input("请输入地区名字:")

#city_name="北京"
location=city_name.encode("utf8")
location=change_code(location)
ak="uWACw4pr4jWmp4YsRzRrtpAh"
base_url="http://api.map.baidu.com/telematics/v3/weather?"
url=base_url+"location="+location+"&output="+output+"&ak="+ak

#print(url)

content=urlopen(url).read().decode("utf8")
doc=minidom.parseString(content)
#print(doc.firstChild.tagName)

root=doc.firstChild
results=root
weather_data=root
index=root
for child in root.childNodes:
      if child.nodeType== doc.ELEMENT_NODE:
            if child.tagName=='date':
                  pass
                 # print(child.firstChild.nodeValue)#date
                  
            elif child.tagName=='results':
                  results=child
for rnode in results.childNodes:
      if rnode.nodeType== doc.ELEMENT_NODE:
            if rnode.tagName=='currentCity':
                  print('*'*40)
                  print("cityname: "+rnode.firstChild.nodeValue)#cityname
                  print('*'*40)
            elif rnode.tagName=='weather_data':
                  weather_data=rnode
            elif rnode.tagName=='index':
                  index=rnode
for node in weather_data.childNodes:
      if node.nodeType== doc.ELEMENT_NODE:
            if node.tagName=='date':
                  print(node.firstChild.nodeValue)
#         elif node.tagName=='dayPictureUrl':
  #                print("day picture url "+node.firstChild.nodeValue)
#            elif node.tagName=='nightPictureUrl':
 #                 print("night picture url "+node.firstChild.nodeValue)
            elif node.tagName=='weather':
                  print("weather: "+node.firstChild.nodeValue)
            elif node.tagName=='wind':
                  print("wind: "+node.firstChild.nodeValue)
            elif node.tagName=='temperature':
                  print("temperature: "+node.firstChild.nodeValue)
                  print()
                  
for node in index.childNodes:
      
      if node.nodeType==doc.ELEMENT_NODE:
            if node.tagName=='title':
                  sys.stdout.write(node.firstChild.nodeValue+":")
            elif node.tagName=='zs':
                  sys.stdout.write(node.firstChild.nodeValue+"\n")
            elif node.tagName=='tipt':
                  sys.stdout.write(node.firstChild.nodeValue+":")
            elif node.tagName=='des':
                  sys.stdout.write(node.firstChild.nodeValue+"\n")
            
input()
input()
