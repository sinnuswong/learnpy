def twoSum(num, target):
        d=num.copy()
        num.sort()
        res=2**31-1
        for i in num:
            if i<= target:
                if target-i in num:
                    res=i
                    break
            elif i>target:
                break
        a,b=0,0
        if res!=2**31-1:
            for i in range(len(d)):
                if d[i]==res:
                    break
            a=i
            for i in range(len(d)):
                if i!=a and d[i]==target-res:
                    break
            b=i
            return (a,b)
print(twoSum([0,4,3,0], 0))
print(twoSum([-1,-2,-3,-4,-5], -8))
