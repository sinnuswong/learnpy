import math
import sys
c=input("input:")
a=int(c)
for i in range(2,a):
    n=int(a**0.5)
    s=1
    for j in range(2,n):
        if(i%j==0):
            s=0
    if(s==1):
        print(i,sep=',',end=',',file=sys.stdout,flush=False)
