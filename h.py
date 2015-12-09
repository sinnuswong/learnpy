class dictclass():
      def __init__(self,d):
            self.a=d
      def __str__(self):
            return str(self.a)
      def del_dict(self,key):
            if key in self.a.keys():
                  return self.a.pop(key)
      def get_dict(self,key):
            if key in self.a.keys():
                  return self.a.get(key)
            else :
                  return "not found"
      def get_key(self):
            res=[]
            for i in self.a.keys():
                  res.append(i)
            return res
      def update_dict(self,b):
            b_keys=list(b.keys())
            for b_key in b_keys:
                  self.a[b_key]=b[b_key]
            return list(self.a.values())

d=dictclass({'a':1,'b':2,'c':3})
print(d)
print(d.get_dict('a'))
print(d.del_dict('a'))
print(d.get_dict('a'))
print(d.get_key())
print(d.update_dict({'a':4,'d':9}))

