# -*- coding:utf-8 -*-

def adjust(a,k,n):
       i = k
       temp=a[k]
       while True:
              if i>n:
                     break
              child = 2*i
              if child>n:
                     break
              if child+1<=n and a[child]<a[child+1]:
                     child+=1
              if temp<a[child]:
                     a[i]=a[child]
                     i=child
              else:
                     break
              
       a[i]=temp
       
def heapSort(a,n):
       start = n//2
       stop = 0
       for i in range(start,stop,-1):
              adjust(a,i,n)
       for i in range(1,n):
              a[1],a[n-i+1]=a[n-i+1],a[1]
              adjust(a,1,n-i)
if __name__=="__main__":
       a=[1,12,44,22,11,9,3,4,7,18,39,47,34,28,13]
       heapSort(a,len(a)-1)
       print a[1:]
              
