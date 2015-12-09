import threading
import time
def test():
      print("<<<<<<")
      time.sleep(2)
      print(">>>>>>")
def fa():
      print("<<<<<<")
      time.sleep(2)
      print(">>>>>>")

s=time.time()
test()
fa()
print(time.time()-s)

s=time.time()
a=threading.Thread(target=test)
b=threading.Thread(target=fa)
a.start()
b.start()
a.join()
b.join()
print(time.time()-s)

      
