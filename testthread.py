from threading import Thread
import time

class myThread(Thread):
      def __init__(self,id):
            Thread.__init__(self)
            self.id=id
      def run(self):
            x = 0
            
            print(self.id)

if __name__ == '__main__':
      t=myThread(12345)
      t.setDaemon(False)
      t.start()
      
      print("i am the main thread")
            
