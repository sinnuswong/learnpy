def ra( m, n):
        d=2**31
        while(d & m == d & n and d):
            d=d>>1
        print(d)
        if d==0:
              return m
        d=2**31-2*d
        
        return d & m
print(ra(1,1))
            
