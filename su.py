from math import sqrt
def f(a):
      n=int(a**0.5)
      for i in range(2,n+1):
            if a%i==0:return False
      else:return True
a=int(input("please input a:"))
for i in range(2,a):
      if f(i):
            print(i,end=' ')
            
      
