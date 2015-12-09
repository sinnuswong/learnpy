
def subsets(S):
        n=len(S)
        con=[]
        for i in range(2**n):
            a=bin(i)[2:]
            a=a[-1::-1]
            print(a)
            res=[]
            for j in range(len(a)):
                  if a[j]=='1':
                        res.append(S[j])
            
            con.append(res)
        return con
print(subsets([1,2,3]))

def sub(S):
        n=len(S)
        res=[]
        for i in range(2**n):
            t=[]
            j=i
            count=0
            while(j):
                  if j%2==1:
                        t.append(S[count])
                  j=int(j/2)
                  count+=1
            res.append(t)
        return res
                  
print(sub([]))
