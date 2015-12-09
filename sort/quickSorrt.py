


def partition(a,left,right):#small to large
       key = a[left]
       while left<right:
              while a[right]>=key and left<right:
                     right-=1
              a[left]=a[right]
              while a[left]<key and left<right:
                     left+=1
              a[right]=a[left]
       a[left]=key
       return left

def quickSort(a,left,right):
       if left<=right:
              k = partition(a,left,right)
              quickSort(a,left,k-1)
              quickSort(a,k+1,right)
       
if __name__=="__main__":
       a = [12,44,22,11,9,3,4,7,18,39,47,34,28,13]
       quickSort(a,0,len(a)-1)
       print a
