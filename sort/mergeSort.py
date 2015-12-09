# -*- coding:utf-8 -*-

def merge(a,s,k,t):
       c = []
       i,j=s,k+1
       while i<=k and j<=t:
              if a[i]<a[j]:
                     c.append(a[i])
                     i+=1
              else:
                     c.append(a[j])
                     j+=1
       while i<=k:
              c.append(a[i])
              i+=1
       while j<=t:
              c.append(a[j])
              j+=1
       for i in range(s,t+1):
              a[i] = c[i-s]

def mergeSort(a,left,right):
       if left<right:
              mid = (left+right)//2
              mergeSort(a,left,mid)
              mergeSort(a,mid+1,right)
              merge(a,left,mid,right)
if __name__=="__main__":
       a = [12,44,22,11,9,3,4,7,18,39,47,34,28,13]
       mergeSort(a,0,len(a)-1)
       print a
