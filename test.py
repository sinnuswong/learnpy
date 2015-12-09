class test():
      def __init__(self,a):
            self.a=a
      def fun(self,b):
            self.b=b
            return self.b
print(test(1).fun(2))
